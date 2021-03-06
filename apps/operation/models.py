from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from chart.models import Chart

# Create your models here.

User = get_user_model()


class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name="用户", db_column="用户", null=True, blank=True)
    chart = models.ForeignKey(Chart, verbose_name="图片", db_column="图片", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = '用户收藏'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        # 不要返回user.user,它有可能为空
        return self.user.username


class FeedBack(models.Model):
    """
    用户留言
    """
    MESSAGE_CHOICES = (
        (1, "留言"),
        (2, "投诉"),
        (3, "询问"),
        (4, "建议"),
    )
    user = models.ForeignKey(User, verbose_name="用户", db_column="用户", null=True, blank=True)
    subject = models.CharField(max_length=100, default="", verbose_name="主题", db_column="主题")
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="留言类型", db_column="留言类型")
    message = models.TextField(default="", verbose_name="留言内容", help_text="留言内容", db_column="留言内容")
    file = models.FileField(upload_to="message/images/", verbose_name="上传的文件", help_text="上传的文件", db_column="上传的文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = "用户留言"
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class DataShare(models.Model):
    """
    数据共享
    """
    CHOICES = (
        (1, "txt"),
        (2, "pdf"),
        (3, "caj"),
        (4, "csv"),
        (5, "json"),
        (6, "excel"),
        (7, "图片"),
    )
    id = models.IntegerField(auto_created=True, primary_key=True, default=1)
    user = models.ForeignKey(User, verbose_name="用户", db_column="用户", null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='标题', db_column="标题", null=False, blank=False)
    desc = models.TextField(verbose_name='文件描述', db_column="文件描述", null=True, blank=True)
    type = models.IntegerField(choices=CHOICES, verbose_name="文件类型", db_column="文件类型")
    click_nums = models.IntegerField(default=0, verbose_name="点击数", db_column="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数", db_column="收藏数")
    down_nums = models.IntegerField(default=0, verbose_name="下载数", db_column="下载数")
    file = models.FileField(upload_to="datashare/file", verbose_name="上传文件", db_column="上传文件")
    resource = models.CharField(max_length=50, verbose_name='数据来源', db_column="数据来源", null=True, blank=True)
    size = models.CharField(max_length=50, verbose_name='文件大小', db_column="文件大小", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = "数据共享"
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name="接收用户")
    message = models.TextField(verbose_name="消息内容", default='')
    has_read = models.BooleanField(default=False, verbose_name="是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = "用户消息"
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


class ChartComments(models.Model):
    """图表评论"""
    user = models.ForeignKey(User, verbose_name="用户", null=True, blank=True)
    chart = models.ForeignKey(Chart, verbose_name="图表", null=True, blank=True)
    comments = models.CharField(max_length=200, verbose_name="评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = '图表评论'
        verbose_name = "图表评论"
        verbose_name_plural = verbose_name
