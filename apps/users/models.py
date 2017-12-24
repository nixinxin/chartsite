from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserProfile(AbstractUser):
    """
    用户
    """
    choice = (
        ("1", '高校'),
        ("2", '科研单位'),
        ("3", '企业单位'),
        ("4", '事业单位'),
        ("5", '政府相关'),
        ("6", '其他')
    )

    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="male", verbose_name="性别")
    image = models.ImageField(upload_to="users/image/%Y/%m", default="users/image/default.png", max_length=100, verbose_name="头像")
    desc = models.TextField(verbose_name='个人介绍', default="这个家伙很懒，什么也没有留下～～！")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    work = models.CharField(max_length=60, null=True, blank=True, verbose_name='职位')
    city = models.CharField(max_length=30, verbose_name='所在城市', null=True, blank=True,)
    unit = models.CharField(max_length=50, verbose_name='单位名称', null=True, blank=True,)
    unit_nature = models.CharField(max_length=60, null=True, blank=True, verbose_name='单位性质', choices=choice, default='高校')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        # 不要返回name,它可能为空，导致登陆报错
        return self.username

    def unread_nums(self):
        # 获取用户未读消息的数量
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id, has_read=False).count()


class PhoneCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=4, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话号码")
    # 不要写datetime.now()，这是系统编译时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


class EmailCode(models.Model):
    """
    邮箱验证码
    """
    code = models.CharField(max_length=16, verbose_name="验证码")
    email = models.CharField(max_length=20, verbose_name="邮箱")
    send_type = models.CharField(verbose_name="验证码类型",
                                 choices=(("register", "注册账号"),
                                          ("forget", "找回密码"),
                                          ("update_email", "修改邮箱")),
                                 max_length=30,
                                 default='register')

    # 不要写datetime.now()，这是系统编译时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class ImageCode(models.Model):
    """
    图片验证码
    """
    code = models.CharField(max_length=4, verbose_name="验证码", null=True, blank=True)
    image = models.ImageField(upload_to="chartsite/captcha", verbose_name="图片", null=True, blank=True)
    # 不要写datetime.now()，这是系统编译时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "图片验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code

