from datetime import datetime
from django.db import models

# Create your models here.
from DjangoUeditor.models import UEditorField


class ChartCategory(models.Model):
    """
    图表类别
    """
    CATEGORY_TYPE = (
        (1, "农业"),
        (2, "林业"),
        (3, "牧业"),
        (3, "牧业"),
        (4, "渔业"),
        (5, "农村"),
        (6, "产业"),
        (7, "农民"),
        (7, "其他"),
    )

    name = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="图表类别", help_text="图表类别")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = "图表类别"
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Chart(models.Model):
    """
    图表
    """
    category = models.ForeignKey(ChartCategory, verbose_name="图表类别", db_column="图表类别")
    chart_sn = models.CharField(max_length=50, default="", verbose_name="图表编号", db_column="图表编号")
    name = models.CharField(max_length=100, verbose_name="图表名", db_column="图表名")
    click_num = models.IntegerField(default=0, verbose_name="点击数", db_column="点击数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数", db_column="收藏数")
    brief = models.TextField(max_length=500, verbose_name="简述", db_column="简述")
    desc = UEditorField(verbose_name="内容", imagePath="chart/images/", width=1000, height=300,
                              filePath="chart/files/", default='', db_column="内容")
    surface = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图", db_column="封面图")
    is_new = models.BooleanField(default=False, verbose_name="是否新图", db_column="是否新图")
    is_hot = models.BooleanField(default=False, verbose_name="是否热搜", db_column="是否热搜")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = "图表展示"
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ChartImage(models.Model):
    """
    图表图片
    """
    chart = models.ForeignKey(Chart, verbose_name="图片名", related_name="images", db_column="图片名")
    image = models.ImageField(upload_to="chart/images/", verbose_name="图片", null=True, blank=True, db_column="图片")
    link = models.CharField(max_length=100, verbose_name="链接", db_column="链接", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = "图表图片"
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.chart.name


class Banner(models.Model):
    """
    轮播图片
    """
    chart = models.ForeignKey(Chart, verbose_name="图片", db_column="图片")
    image = models.ImageField(upload_to='chartsite/banner/', verbose_name="轮播图片", db_column="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序", db_column="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = "轮播图片"
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.chart.name


class HotSearch(models.Model):
    """
    热搜排行
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="热搜")
    index = models.IntegerField(default=0, verbose_name="排序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = "热搜排行"
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords


class YearBooks(models.Model):
    """
    统计年鉴目录
    """
    id = models.IntegerField(verbose_name="同级顺序")
    title = models.CharField(max_length=60, verbose_name="标题")
    category = models.CharField(max_length=60, verbose_name="父类")
    page = models.CharField(max_length=20, verbose_name="页码")
    identify = models.CharField(max_length=20, primary_key=True, verbose_name="唯一编号")
    year = models.CharField(max_length=4, verbose_name="唯一编号")

    class Meta:
        db_table = "统计年鉴目录"
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
