from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

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
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    work_unit = models.CharField(max_length=60, null=True, blank=True, verbose_name='工作单位')
    unit_nature = models.CharField(max_length=60, null=True, blank=True, verbose_name='单位性质', choices=choice)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        # db_table = "用户信息"
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        # 不要返回name,它可能为空，导致登陆报错
        return self.username


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=4, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话号码")
    # 不要写datetime.now()，这是系统编译时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        # db_table = "短信验证码"
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


