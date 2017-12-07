from datetime import datetime

from django.db import models

# Create your models here.


class News(models.Model):
    """
    新闻动态
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=1)
    title = models.CharField(max_length=100, verbose_name='标题', db_column="标题")
    content = models.TextField(null=True, blank=True, verbose_name='内容', db_column="内容")
    resource = models.CharField(max_length=100, null=True, blank=True, verbose_name='来源', db_column="来源")
    display = models.BooleanField(default=False, verbose_name="是否展示", db_column="是否展示")
    is_hot = models.BooleanField(default=False, verbose_name="是否热点", db_column="是否热点")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", db_column="添加时间")

    class Meta:
        db_table = "新闻动态"
        verbose_name = "新闻动态"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class SiteInfo(models.Model):
    """
    网站信息
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=1)
    title = models.CharField(max_length=100, verbose_name='标题', db_column="标题")
    content = models.TextField(null=True, blank=True, verbose_name='内容', db_column="内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", db_column="添加时间")

    class Meta:
        db_table = "网站信息"
        verbose_name = "网站信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class RelatedSite(models.Model):
    """
    相关链接
    """
    index = models.IntegerField(null=True, blank=True, verbose_name='顺序', db_column="顺序")
    name = models.CharField(max_length=60, null=True, blank=True, verbose_name='名称', db_column="名称")
    link = models.CharField(max_length=100, null=True, blank=True, verbose_name='链接', db_column="链接")
    display = models.BooleanField(default=False, verbose_name='是否显示', db_column="是否显示")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", db_column="添加时间")

    class Meta:
        db_table = "相关链接"
        verbose_name = "相关链接"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
