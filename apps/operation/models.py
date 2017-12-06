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
    user = models.ForeignKey(User, verbose_name="用户", db_column="用户")
    chart = models.ForeignKey(Chart, verbose_name="图片", db_column="图片")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = '用户收藏'
        verbose_name = db_table
        verbose_name_plural = verbose_name
        unique_together = ("user", "chart")

    def __str__(self):
        # 不要返回user.user，它有可能为空
        return self.user.username


class FeedBack(models.Model):
    """
    用户留言
    """
    MESSAGE_CHOICES = (
        (1, "留言"),
        (2, "投诉"),
        (3, "询问"),
        (4, "售后"),
        (5, "求购")
    )
    user = models.ForeignKey(User, verbose_name="用户", db_column="用户")
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="留言类型", db_column="留言类型")
    subject = models.CharField(max_length=100, default="", verbose_name="主题", db_column="主题")
    message = models.TextField(default="", verbose_name="留言内容", help_text="留言内容", db_column="留言内容")
    file = models.FileField(upload_to="message/images/", verbose_name="上传的文件", help_text="上传的文件", db_column="上传的文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = "用户留言"
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


