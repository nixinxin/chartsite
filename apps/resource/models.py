from datetime import datetime

from django.db import models


# Create your models here.
from DjangoUeditor.models import UEditorField


class ResourceList(models.Model):
    """
    数据资源列表
    """
    title = models.CharField(max_length=30, blank=False, null=False, db_column='标题', verbose_name='标题')
    CATEGORY_TYPE = (
                        (1, "农业"),
                        (2, "林业"),
                        (3, "牧业"),
                        (4, "渔业"),
                        (5, "农村"),
                        (6, "农民"),
                        (7, "植物"),
                        (7, "动物"),
                    )
    type = models.IntegerField(blank=False, null=False, choices=CATEGORY_TYPE, db_column='类别', verbose_name='类别')
    desc = UEditorField(verbose_name="数据描述", db_column="数据描述", imagePath="resource/images/",
                        width=800, height=300, filePath="resource/files/", default='')
    image = models.ImageField(upload_to='resource/images', blank=True, null=True, verbose_name="数据封面", db_column="数据封面")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", db_column="是否导航")
    is_new = models.BooleanField(default=False, verbose_name="是否最新", db_column="是否最新")
    is_hot = models.BooleanField(default=False, verbose_name="是否热门", db_column="是否热门")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", db_column="添加时间")

    class Meta:
        db_table = "数据资源列表"
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class GwyjzwzzzyDb(models.Model):
    """
    国外引进作物资源数据库
    """
    id = models.IntegerField(auto_created=True, null=False, primary_key=True, default=1)
    total_id = models.IntegerField(null=True, blank=True, verbose_name="总编号", db_column="总编号")
    import_id = models.IntegerField(null=True, blank=True, verbose_name="引种编号", db_column="引种编号")
    copes_category = models.CharField(max_length=12, null=True, blank=True, verbose_name="作物类别", db_column="作物类别")
    copes_type = models.CharField(max_length=12, null=True, blank=True, verbose_name="作物种类", db_column="作物种类")
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name="作物名称", db_column="作物名称")
    category_name = models.CharField(max_length=110, null=True, blank=True, verbose_name="品种名称", db_column="品种名称")
    translated_name = models.CharField(max_length=40, null=True, blank=True, verbose_name="译名", db_column="译名")
    source = models.CharField(max_length=40, null=True, blank=True, verbose_name="来源地", db_column="来源地")
    source_area = models.CharField(max_length=40, null=True, blank=True, verbose_name="原产地", db_column="原产地")
    total_way = models.CharField(max_length=40, null=True, blank=True, verbose_name="总途径", db_column="总途径")
    import_way = models.CharField(max_length=40, null=True, blank=True, verbose_name="引入途径", db_column="引入途径")
    import_year = models.CharField(max_length=4, null=True, blank=True, verbose_name="引入年份", db_column="引入年份")
    import_time = models.CharField(max_length=100, null=True, blank=True, verbose_name="引入时间", db_column="引入时间")
    distribution_unit = models.CharField(max_length=60, null=True, blank=True, verbose_name="分发单位", db_column="分发单位")
    feature = models.CharField(max_length=40, null=True, blank=True, verbose_name="特征特性", db_column="特征特性")
    Save_unit = models.CharField(max_length=40, null=True, blank=True, verbose_name="保存单位", db_column="保存单位")
    comment = models.CharField(max_length=100, null=True, blank=True, verbose_name="备注", db_column="备注")

    class Meta:
        db_table = "国外引进作物资源数据库"
        verbose_name = "国外引进作物资源数据库"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class XzqhList(models.Model):
    """
    行政区划清单
    """
    id = models.IntegerField(auto_created=True, null=False, primary_key=True, default=1)
    province = models.CharField(max_length=20, null=True, blank=True, verbose_name='省份', db_column="省份")
    city = models.CharField(max_length=20, null=True, blank=True, verbose_name='城市', db_column="城市")
    district = models.CharField(max_length=20, null=True, blank=True, verbose_name='区县', db_column="区县")
    provincecode = models.IntegerField(null=True, blank=True, verbose_name='省份编码', db_column="省份编码")
    citycode = models.IntegerField(null=True, blank=True, verbose_name='城市编码', db_column="城市编码")
    districtcode = models.IntegerField(null=True, blank=True, verbose_name='区县编码', db_column="区县编码")
    alias = models.CharField(max_length=10, null=True, blank=True, verbose_name='别名', db_column="别名")
    bound = models.CharField(max_length=60, blank=True, null=True, verbose_name='面源坐标', db_column="面源坐标")
    formatted_address = models.CharField(max_length=60, blank=True, null=True, verbose_name='绝对地址', db_column="绝对地址")

    class Meta:
        db_table = "行政区划清单"
        verbose_name = "行政区划清单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.district


class NcpjgDb(models.Model):
    """
    农产品价格行情数据库
    """
    category = models.CharField(max_length=20, null=True, blank=True, verbose_name='类别', db_column="类别")
    product = models.CharField(max_length=20, verbose_name='产品', null=False, db_column="产品")
    price = models.FloatField(max_length=6,  verbose_name="价格", null=False, db_column="价格")
    market = models.CharField(max_length=40, verbose_name='市场', db_column="市场")
    datetime = models.DateField(verbose_name='日期', null=False, db_column="日期")

    class Meta:
        db_table = "农产品价格行情数据库"
        verbose_name = "农产品价格行情数据库"
        verbose_name_plural = verbose_name
        unique_together = ("product", 'price', 'market', 'datetime')

    def __str__(self):
        return self.product


class NcpjgHqzdcode(models.Model):
    """
    农产品价格行情字段编码
    """
    code = models.IntegerField(primary_key=True, null=False, verbose_name='编码', db_column="编码")
    product = models.CharField(max_length=40, null=False, blank=True, verbose_name="名称", db_column="名称")
    category = models.CharField(max_length=40, null=False, blank=True, verbose_name='父级', db_column="父级")
    bound = models.CharField(max_length=60, blank=True, null=True, verbose_name='面源坐标', db_column="面源坐标")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name='城市', db_column="城市")
    district = models.CharField(max_length=20, blank=True, null=True, verbose_name='区县', db_column="区县")
    formatted_address = models.CharField(max_length=60, blank=True, null=True, verbose_name='绝对地址', db_column="绝对地址")
    location = models.CharField(max_length=60, blank=True, null=True, verbose_name='位置', db_column="位置")
    province = models.CharField(max_length=30, blank=True, null=True, verbose_name='省份', db_column="省份")

    class Meta:
        db_table = "农产品价格行情字段编码"
        verbose_name = "农产品价格行情字段编码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.product


class AgriIndex(models.Model):
    """
    农业统计指标
    """
    index = models.CharField(max_length=40, null=False, verbose_name="指标", db_column="指标")
    values = models.CharField(max_length=20, null=False, verbose_name="数值", db_column="数值")
    location = models.CharField(max_length=40, null=False, verbose_name='省份', db_column="省份")
    year = models.IntegerField(null=False, verbose_name='年份', db_column="年份")

    class Meta:
        db_table = "农业统计指标"
        verbose_name = db_table
        verbose_name_plural = verbose_name
        unique_together = (("index", 'values', 'location', 'year'), )

    def __str__(self):
        return self.index


class MytxDb(models.Model):
    """
    农作物名优特新品种数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    category = models.CharField(max_length=128, null=True, blank=True, verbose_name="作物种类", db_column="作物种类")
    brands = models.CharField(max_length=128, null=True, blank=True, verbose_name="作物品种", db_column="作物品种")
    pzname = models.CharField(max_length=128, null=True, blank=True, verbose_name="品种名称", db_column="品种名称")
    desc = models.TextField(verbose_name='基本情况', null=True, blank=True, db_column="基本情况")
    feature = models.TextField(verbose_name='特征特性', null=True, blank=True, db_column="特征特性")
    raiser = models.CharField(max_length=256,  null=True, blank=True, verbose_name="培育者", db_column="培育者")
    location_T = models.TextField(verbose_name='地区及技术', null=True, blank=True, db_column="地区及技术")
    brands_category = models.CharField(max_length=128, null=True, blank=True, verbose_name="品种类别", db_column="品种类别")
    examine = models.TextField(null=True, blank=True, verbose_name="审定情况", db_column='审定情况')
    get_day = models.CharField(max_length=10, null=True, blank=True, verbose_name="资源采集日", db_column="资源采集日")

    class Meta:
        db_table = "农作物名优特新品种数据库"
        verbose_name = "农作物名优特新品种数据库"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pzname


class ZgnytdkcDb(models.Model):
    """
    中国农业天敌昆虫数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    function_class = models.CharField(max_length=20, blank=True, null=True,  verbose_name="功能类别", db_column="功能类别")
    jizhu_insect = models.TextField(blank=True, null=True, db_column='寄主昆虫', verbose_name="寄主昆虫")
    jizhu_hazard = models.CharField(max_length=40, blank=True, null=True, db_column='寄主危害作物', verbose_name="寄主危害作物")
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    feature = models.TextField(blank=True, null=True, db_column='生物学特性', verbose_name="生物学特性")
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    gang = models.CharField(max_length=20, blank=True, null=True, db_column='纲', verbose_name="纲")
    mu = models.CharField(max_length=20, blank=True, null=True, db_column='目', verbose_name="目")
    ke = models.CharField(max_length=20, blank=True, null=True, db_column='科', verbose_name="科")
    type_feature = models.TextField(blank=True, null=True, db_column='形态特征', verbose_name="形态特征")
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    xuename = models.CharField(max_length=90, blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '中国农业天敌昆虫数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgnyyhswDbTp(models.Model):
    """
    中国农业有害生物图片数据库
    """
    name = models.CharField(max_length=40, blank=True, null=True, db_column='名称', verbose_name="名称")
    species = models.CharField(max_length=40, blank=True, null=True, db_column='种类', verbose_name="种类")
    link = models.ImageField(upload_to='agridata/images', db_column='链接', verbose_name="链接")

    class Meta:

        db_table = '中国农业有害生物图片数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ZgnttdzzDb(models.Model):
    """
    中国农业天敌蜘蛛数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    function_class = models.CharField(max_length=20, blank=True, null=True, db_column="功能类别", verbose_name="功能类别")
    jizhu_insect = models.TextField(blank=True, null=True, db_column='寄主昆虫', verbose_name="寄主昆虫")
    jizhu_hazard = models.CharField(max_length=40, blank=True, null=True, db_column='寄主危害作物', verbose_name="寄主危害作物")
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    feature = models.TextField(blank=True, null=True, db_column='生物学特性', verbose_name="生物学特性")
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    gang = models.CharField(max_length=20, blank=True, null=True, db_column='纲', verbose_name="纲")
    mu = models.CharField(max_length=20, blank=True, null=True, db_column='目', verbose_name="目")
    ke = models.CharField(max_length=20, blank=True, null=True, db_column='科', verbose_name="科")
    type_feature = models.TextField(blank=True, null=True, db_column='形态特征', verbose_name="形态特征")
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    xuename = models.CharField(max_length=60, blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '中国农业天敌蜘蛛数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgnthsDb(models.Model):
    """
    中国农业害鼠数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    enemy = models.CharField(max_length=100, blank=True, null=True, db_column='天敌', verbose_name='天敌')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    alias = models.CharField(max_length=40, blank=True, null=True, db_column='别名', verbose_name='别名')
    feature = models.TextField(blank=True, null=True, db_column='生物学特征', verbose_name="生物学特征")
    hazard_feature = models.TextField(blank=True, null=True, db_column='危害特点', verbose_name="危害特点")
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    gang = models.CharField(max_length=20, blank=True, null=True, db_column='纲', verbose_name="纲")
    mu = models.CharField(max_length=20, blank=True, null=True, db_column='目', verbose_name="目")
    ke = models.CharField(max_length=20, blank=True, null=True, db_column='科', verbose_name="科")
    govern_way = models.TextField(blank=True, null=True, db_column='综合治理策略', verbose_name="综合治理策略")
    type_feature = models.TextField(blank=True, null=True, db_column='形态特征', verbose_name="形态特征")
    regular = models.TextField(blank=True, null=True, db_column='发生消长规律', verbose_name="发生消长规律")
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    xuename = models.CharField(max_length=40, blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '中国农业害鼠数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgyclschcDb(models.Model):
    """
    中国叶菜类蔬菜害虫数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    enemy = models.CharField(max_length=100, blank=True, null=True, db_column='天敌', verbose_name='天敌')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    type_feature = models.TextField(blank=True, null=True, db_column='形态特征', verbose_name="形态特征")
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    gang = models.CharField(max_length=20, blank=True, null=True, db_column='纲', verbose_name="纲")
    mu = models.CharField(max_length=20, blank=True, null=True, db_column='目', verbose_name="目")
    ke = models.CharField(max_length=20, blank=True, null=True, db_column='科', verbose_name="科")
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    desc = models.TextField(blank=True, null=True, db_column='生物学特性及发生消长规律', verbose_name="生物学特性及发生消长规律")
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    xuename = models.CharField(max_length=100, blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    control_method = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '中国叶菜类蔬菜害虫数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class WlyhwswDb(models.Model):
    """
    外来有害微生物数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    control_way = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    hazard_feature = models.TextField(blank=True, null=True, db_column='危害特点', verbose_name="危害特点")
    desc = models.TextField(blank=True, null=True, db_column='生物学特征及发生消长规律', verbose_name="生物学特征及发生消长规律")
    pathway = models.TextField(blank=True, null=True, db_column='传播途径', verbose_name="传播途径")
    men = models.CharField(max_length=20, blank=True, null=True, db_column='门', verbose_name="门")
    yamen = models.CharField(max_length=20, blank=True, null=True, db_column='亚门', verbose_name="亚门")
    gang = models.CharField(max_length=20, blank=True, null=True, db_column='纲', verbose_name="纲")
    mu = models.CharField(max_length=20, blank=True, null=True, db_column='目', verbose_name="目")
    ke = models.CharField(max_length=20, blank=True, null=True, db_column='科', verbose_name="科")
    shu = models.CharField(max_length=20, blank=True, null=True, db_column='属', verbose_name="属")
    ruqindi = models.TextField(blank=True, null=True, db_column='入侵地', verbose_name="入侵地")
    jizhu = models.TextField(blank=True, null=True, db_column='寄主', verbose_name="寄主")
    xuename = models.CharField(max_length=100, blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    rqsjdd = models.TextField(blank=True, null=True, db_column='入侵时间及地点', verbose_name="入侵时间及地点")
    alias = models.CharField(max_length=30, blank=True, null=True, db_column='别名', verbose_name='别名')
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    english = models.TextField(blank=True, null=True, db_column='英文名', verbose_name="英文名")
    source = models.CharField(max_length=60, blank=True, null=True, db_column='原产地', verbose_name="原产地")
    type_feature = models.TextField(blank=True, null=True, db_column='形态特征', verbose_name="形态特征")
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")

    class Meta:
        db_table = '外来有害微生物数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class WlyhkcDb(models.Model):
    """
    外来有害昆虫数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    rqsjddd = models.TextField(blank=True, null=True, db_column='入侵时间及地点', verbose_name="入侵时间及地点")
    control_way = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    alias = models.CharField(max_length=30, blank=True, null=True, db_column='别名', verbose_name='别名')
    hazard_feature = models.TextField(blank=True, null=True, db_column='危害特点', verbose_name="危害特点")
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    desc = models.TextField(blank=True, null=True, db_column='生物学特征及发生消长规律', verbose_name="生物学特征及发生消长规律")
    gang = models.CharField(max_length=20, blank=True, null=True, db_column='纲', verbose_name="纲")
    mu = models.CharField(max_length=20, blank=True, null=True, db_column='目', verbose_name="目")
    ke = models.CharField(max_length=20, blank=True, null=True, db_column='科', verbose_name="科")
    shu = models.CharField(max_length=20, blank=True, null=True, db_column='属', verbose_name="属")
    english = models.CharField(max_length=100, blank=True, null=True, db_column='英文名', verbose_name="英文名")
    pathway = models.TextField(blank=True, null=True, db_column='传播途径', verbose_name="传播途径")
    ruqidi = models.TextField(blank=True, null=True, db_column='入侵地', verbose_name="入侵地")
    men = models.CharField(max_length=20, blank=True, null=True, db_column='门', verbose_name="门")
    source = models.CharField(max_length=80, blank=True, null=True, db_column='原产地', verbose_name="原产地")
    jizhu = models.TextField(blank=True, null=True, db_column='寄主', verbose_name="寄主")
    type_feature = models.TextField(blank=True, null=True, db_column='形态特征', verbose_name="形态特征")
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    xuename = models.CharField(max_length=60, blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")


    class Meta:
        db_table = '外来有害昆虫数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class WlyhzwDb(models.Model):
    """
    外来有害植物数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    ruqintl = models.TextField(blank=True, null=True, db_column='入侵时间及地点', verbose_name='入侵时间及地点')
    control_way = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    alias = models.CharField(max_length=40, blank=True, null=True, db_column='别名', verbose_name='别名')
    hazard_feature = models.TextField(blank=True, null=True, db_column='危害特点', verbose_name="危害特点")
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    desc = models.TextField(blank=True, null=True, db_column='生物学特征及发生消长规律', verbose_name='生物学特征及发生消长规律')
    gang = models.CharField(max_length=20, blank=True, null=True, db_column='纲', verbose_name="纲")
    mu = models.CharField(max_length=20, blank=True, null=True, db_column='目', verbose_name="目")
    ke = models.CharField(max_length=20, blank=True, null=True, db_column='科', verbose_name="科")
    shu = models.CharField(max_length=20, blank=True, null=True, db_column='属', verbose_name="属")
    english = models.CharField(max_length=80, blank=True, null=True, db_column='英文名', verbose_name="英文名")
    pathway = models.TextField(blank=True, null=True, db_column='传播途径', verbose_name="传播途径")
    ruqindi = models.TextField(blank=True, null=True, db_column='入侵地', verbose_name='入侵地')
    men = models.CharField(max_length=20, blank=True, null=True, db_column='门', verbose_name="门")
    source = models.CharField(max_length=60, blank=True, null=True, db_column='原产地', verbose_name="原产地")
    type_feature = models.TextField(blank=True, null=True, db_column='形态特征', verbose_name="形态特征")
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    xuename = models.TextField(blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '外来有害植物数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZghdzcDb(models.Model):
    """
    中国旱地杂草数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    happen_hazard = models.TextField(blank=True, null=True, db_column='发生与危害', verbose_name='发生与危害')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    gang = models.CharField(max_length=20, blank=True, null=True, db_column='纲', verbose_name="纲")
    mu = models.CharField(max_length=20, blank=True, null=True, db_column='目', verbose_name="目")
    ke = models.CharField(max_length=20, blank=True, null=True, db_column='科', verbose_name="科")
    shu = models.CharField(max_length=20, blank=True, null=True, db_column='属', verbose_name="属")
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    govern_way = models.TextField(blank=True, null=True, db_column='综合治理策略', verbose_name='综合治理策略')
    type_feature = models.TextField(blank=True, null=True, db_column='形态特征', verbose_name="形态特征")
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    xuename = models.TextField(blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    alias = models.CharField(max_length=30, blank=True, null=True, db_column='别名', verbose_name='别名')
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '中国旱地杂草数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZghlzwhcDb(models.Model):
    """
    中国旱粮作物害虫数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    enemy = models.TextField(blank=True, null=True, db_column='天敌', verbose_name='天敌')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    type_feature = models.TextField(blank=True, null=True, db_column='形态特征', verbose_name="形态特征")
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    gang = models.CharField(max_length=20, blank=True, null=True, db_column='纲', verbose_name="纲")
    mu = models.CharField(max_length=20, blank=True, null=True, db_column='目', verbose_name="目")
    ke = models.CharField(max_length=20, blank=True, null=True, db_column='科', verbose_name="科")
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    desc = models.TextField(blank=True, null=True, db_column='生物学特性及发生消长规律', verbose_name='生物学特性及发生消长规律')
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    xuename = models.TextField(blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    control_method = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '中国旱粮作物害虫数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZggslschcDb(models.Model):
    """
    中国果菜类蔬菜害虫数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    enemy = models.CharField(max_length=100, blank=True, null=True, db_column='天敌', verbose_name='天敌')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    type_feature = models.TextField(blank=True, null=True, db_column='形态特征', verbose_name="形态特征")
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    gang = models.CharField(max_length=20, blank=True, null=True, db_column='纲', verbose_name="纲")
    mu = models.CharField(max_length=20, blank=True, null=True, db_column='目', verbose_name="目")
    ke = models.CharField(max_length=20, blank=True, null=True, db_column='科', verbose_name="科")
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    desc = models.TextField(blank=True, null=True, db_column='生物学特性及发生消长规律', verbose_name='生物学特性及发生消长规律')
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    xuename = models.CharField(max_length=100, blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    control_method = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")


    class Meta:
        db_table = '中国果菜类蔬菜害虫数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZggjhcDb(models.Model):
    """
    中国柑桔害虫数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    enemy = models.TextField(blank=True, null=True, db_column='天敌', verbose_name='天敌')
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    type_feature = models.TextField(blank=True, null=True, db_column='形态特征', verbose_name="形态特征")
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    gang = models.CharField(max_length=20, blank=True, null=True, db_column='纲', verbose_name="纲")
    mu = models.CharField(max_length=20, blank=True, null=True, db_column='目', verbose_name="目")
    ke = models.CharField(max_length=20, blank=True, null=True, db_column='科', verbose_name="科")
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    desc = models.TextField(blank=True, null=True, db_column='生物学特性及发生消长规律', verbose_name='生物学特性及发生消长规律')
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    xuename = models.CharField(max_length=80, blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    control_method = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '中国柑桔害虫数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgmhhcDb(models.Model):
    """
    中国棉花害虫数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    enemy = models.CharField(max_length=100, blank=True, null=True, db_column='天敌', verbose_name='天敌')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    type_feature = models.TextField(blank=True, null=True, db_column='形态特征', verbose_name="形态特征")
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    gang = models.CharField(max_length=20, blank=True, null=True, db_column='纲', verbose_name="纲")
    mu = models.CharField(max_length=20, blank=True, null=True, db_column='目', verbose_name="目")
    ke = models.CharField(max_length=20, blank=True, null=True, db_column='科', verbose_name="科")
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    desc = models.TextField(blank=True, null=True, db_column='生物学特性及发生消长规律', verbose_name='生物学特性及发生消长规律')
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    xuename = models.CharField(max_length=80, blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    control_way = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '中国棉花害虫数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgstzcDb(models.Model):
    """
    中国水田杂草数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    happen_hazard = models.TextField(blank=True, null=True, db_column='发生与危害', verbose_name='发生与危害')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    gang = models.CharField(max_length=20, blank=True, null=True, db_column='纲', verbose_name="纲")
    mu = models.CharField(max_length=20, blank=True, null=True, db_column='目', verbose_name="目")
    ke = models.CharField(max_length=20, blank=True, null=True, db_column='科', verbose_name="科")
    shu = models.CharField(max_length=20, blank=True, null=True, db_column='属', verbose_name="属")
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    govern_way = models.TextField(blank=True, null=True, db_column='综合治理策略', verbose_name='综合治理策略')
    type_feature = models.TextField(blank=True, null=True, db_column='形态特征', verbose_name="形态特征")
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    xuename = models.CharField(max_length=110, blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    alias = models.CharField(max_length=30, blank=True, null=True, db_column='别名', verbose_name='别名')
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '中国水田杂草数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgsdhcDb(models.Model):
    """
    中国水稻害虫数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    enemy = models.TextField(blank=True, null=True, db_column='天敌', verbose_name='天敌')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    type_feature = models.TextField(blank=True, null=True, db_column='形态特征', verbose_name="形态特征")
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    gang = models.CharField(max_length=20, blank=True, null=True, db_column='纲', verbose_name="纲")
    mu = models.CharField(max_length=20, blank=True, null=True, db_column='目', verbose_name="目")
    ke = models.CharField(max_length=20, blank=True, null=True, db_column='科', verbose_name="科")
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    desc = models.TextField(blank=True, null=True, db_column='生物学特性及发生消长规律', verbose_name='生物学特性及发生消长规律')
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    xuename = models.CharField(max_length=70, blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    control_method = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")


    class Meta:
        db_table = '中国水稻害虫数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgtsNcp(models.Model):
    """
    中国特色农产品
    """
    id = models.IntegerField(auto_created=True, primary_key=True, null=False, default=1)
    title = models.CharField(max_length=60, db_column='标题', verbose_name='标题')
    location = models.CharField(max_length=60, blank=True, null=True, db_column='地点', verbose_name='地点')
    feature = models.CharField(max_length=100, blank=True, null=True, db_column='特征', verbose_name='特征')
    brands = models.CharField(max_length=60, blank=True, null=True, db_column='地理标志', verbose_name='地理标志')
    desc = models.TextField(blank=True, null=True, db_column='基本介绍', verbose_name='基本介绍')
    layout = models.TextField(blank=True, null=True, db_column='产业布局', verbose_name='产业布局')
    history = models.TextField(blank=True, null=True, db_column='历史', verbose_name='历史')
    province = models.CharField(max_length=60, blank=True, null=True, db_column='省份', verbose_name='省份')
    city = models.CharField(max_length=60, blank=True, null=True, db_column='市级', verbose_name='市级')
    district = models.CharField(max_length=60, blank=True, null=True, db_column='区县', verbose_name='区县')

    class Meta:
        db_table = '中国特色农产品'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ZglszwbdbhDb(models.Model):
    """
    中国粮食作物病毒病害数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    hazard_buwei = models.TextField(blank=True, null=True, db_column='主要危害部位', verbose_name='主要危害部位')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    symptom = models.TextField(blank=True, null=True, db_column='为害症状', verbose_name='为害症状')
    disease_type = models.CharField(max_length=20, blank=True, null=True, db_column='病害类型', verbose_name='病害类型')
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    byzhname = models.CharField(max_length=40, blank=True, null=True, db_column='病原中文名', verbose_name='病原中文名')
    byxuename = models.TextField(blank=True, null=True, db_column='病原拉丁学名', verbose_name='病原拉丁学名')
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    byfldw = models.CharField(max_length=60, blank=True, null=True, db_column='病原分类地位', verbose_name='病原分类地位')
    byxttz = models.TextField(blank=True, null=True, db_column='病原形态特征', verbose_name='病原形态特征')
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    control_way = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    alias = models.CharField(max_length=30, blank=True, null=True, db_column='别名', verbose_name='别名')
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    pathway_fbtj = models.TextField(blank=True, null=True, db_column='传播途径和发病条件', verbose_name='传播途径和发病条件')
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '中国粮食作物病毒病害数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZglszwzjbhDb(models.Model):
    """
    中国粮食作物真菌病害数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    hazard_buwei = models.TextField(blank=True, null=True, db_column='主要危害部位', verbose_name='主要危害部位')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    symptom = models.TextField(blank=True, null=True, db_column='为害症状', verbose_name='为害症状')
    disease_type = models.CharField(max_length=20, blank=True, null=True, db_column='病害类型', verbose_name='病害类型')
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    byzhname = models.CharField(max_length=60, blank=True, null=True, db_column='病原中文名', verbose_name='病原中文名')
    byxuename = models.TextField(blank=True, null=True, db_column='病原拉丁学名', verbose_name="病原拉丁学名")
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    byfldw = models.CharField(max_length=30, blank=True, null=True, db_column='病原分类地位', verbose_name='病原分类地位')
    byxttz = models.TextField(blank=True, null=True, db_column='病原形态特征', verbose_name='病原形态特征')
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    pathway_fbtj = models.TextField(blank=True, null=True, db_column='传播途径和发病条件', verbose_name='传播途径和发病条件')

    control_way = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    alias = models.CharField(max_length=30, blank=True, null=True, db_column='别名', verbose_name='别名')
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '中国粮食作物真菌病害数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZglszwxjbhDb(models.Model):
    """
    中国粮食作物细菌病害数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    hazard_buwei = models.TextField(blank=True, null=True, db_column='主要危害部位', verbose_name='主要危害部位')
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    symptom = models.TextField(blank=True, null=True, db_column='为害症状', verbose_name='为害症状')
    disease_type = models.CharField(max_length=20, blank=True, null=True, db_column='病害类型', verbose_name='病害类型')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    byzhname = models.CharField(max_length=60, blank=True, null=True, db_column='病原中文名', verbose_name='病原中文名')
    byxuename = models.TextField(blank=True, null=True, db_column='病原拉丁学名', verbose_name='病原拉丁学名')
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    byfldw = models.CharField(max_length=60, blank=True, null=True, db_column='病原分类地位', verbose_name='病原分类地位')
    byxttz = models.TextField(blank=True, null=True, db_column='病原形态特征', verbose_name='病原形态特征')
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    alias = models.CharField(max_length=40, blank=True, null=True, db_column='别名', verbose_name='别名')
    control_way = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    pathway_fbtj = models.TextField(blank=True, null=True, db_column='传播途径和发病条件', verbose_name='传播途径和发病条件')
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '中国粮食作物细菌病害数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgjjzwbdbhDb(models.Model):
    """
    中国经济作物病毒病害数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    hazard_buwei = models.TextField(blank=True, null=True, db_column='主要危害部位', verbose_name='主要危害部位')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    symptom = models.TextField(blank=True, null=True, db_column='为害症状', verbose_name='为害症状')
    disease_type = models.CharField(max_length=30, blank=True, null=True, db_column='病害类型', verbose_name='病害类型')
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    byzhname = models.CharField(max_length=60, blank=True, null=True, db_column='病原中文名', verbose_name='病原中文名')
    byxuename = models.TextField(blank=True, null=True, db_column='病原拉丁学名', verbose_name='病原拉丁学名')
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    alias = models.CharField(max_length=30, blank=True, null=True, db_column='别名', verbose_name='别名')
    byfldw = models.CharField(max_length=30, blank=True, null=True, db_column='病原分类地位', verbose_name='病原分类地位')
    byxttz = models.TextField(blank=True, null=True, db_column='病原形态特征', verbose_name='病原形态特征')
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    control_way = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    english = models.CharField(max_length=60, blank=True, null=True, db_column='英文名', verbose_name="英文名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    pathway_fbtj = models.TextField(blank=True, null=True, db_column='传播途径和发病条件', verbose_name='传播途径和发病条件')
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '中国经济作物病毒病害数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgjjzwzjbhDb(models.Model):
    """
    中国经济作物真菌病害数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    hazard_buwei = models.TextField(blank=True, null=True, db_column='主要危害部位', verbose_name='主要危害部位')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    symptom = models.TextField(blank=True, null=True, db_column='为害症状', verbose_name='为害症状')
    disease_type = models.CharField(max_length=20, blank=True, null=True, db_column='病害类型', verbose_name='病害类型')
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    byzhname = models.CharField(max_length=60, blank=True, null=True, db_column='病原中文名', verbose_name='病原中文名')
    byxuename = models.TextField(blank=True, null=True, db_column='病原拉丁学名', verbose_name='病原拉丁学名')
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    alias = models.CharField(max_length=30, blank=True, null=True, db_column='别名', verbose_name='别名')
    byfldw = models.CharField(max_length=30, blank=True, null=True, db_column='病原分类地位', verbose_name='病原分类地位')
    byxttz = models.TextField(blank=True, null=True, db_column='病原形态特征', verbose_name='病原形态特征')
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    control_way = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    english = models.CharField(max_length=80, blank=True, null=True, db_column='英文名', verbose_name="英文名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    pathway_fbtj = models.TextField(blank=True, null=True, db_column='传播途径和发病条件', verbose_name='传播途径和发病条件')
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '中国经济作物真菌病害数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgjjzwxjbhDb(models.Model):
    """
    中国经济作物细菌病害数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    hazard_buwei = models.TextField(blank=True, null=True, db_column='主要危害部位', verbose_name='主要危害部位')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    symptom = models.TextField(blank=True, null=True, db_column='为害症状', verbose_name='为害症状')
    disease_type = models.CharField(max_length=30, blank=True, null=True, db_column='病害类型', verbose_name='病害类型')
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    byzhname = models.CharField(max_length=60, blank=True, null=True, db_column='病原中文名', verbose_name='病原中文名')
    byxuename = models.TextField(max_length=60, blank=True, null=True, db_column='病原拉丁学名', verbose_name='病原拉丁学名')
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    alias = models.CharField(max_length=30, blank=True, null=True, db_column='别名', verbose_name='别名')
    byfldw = models.CharField(max_length=30, blank=True, null=True, db_column='病原分类地位', verbose_name='病原分类地位')
    byxttz = models.TextField(blank=True, null=True, db_column='病原形态特征', verbose_name='病原形态特征')
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    control_method = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    english = models.CharField(max_length=80, blank=True, null=True, db_column='英文名', verbose_name="英文名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    pathway_fbtj = models.TextField(blank=True, null=True, db_column='传播途径和发病条件', verbose_name='传播途径和发病条件')
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '中国经济作物细菌病害数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgpgtlhcDb(models.Model):
    """
    中国苹果桃梨害虫数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    enemy = models.TextField(blank=True, null=True, db_column='天敌', verbose_name='天敌')
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    type_feature = models.TextField(blank=True, null=True, db_column='形态特征', verbose_name="形态特征")
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    gang = models.CharField(max_length=20, blank=True, null=True, db_column='纲', verbose_name="纲")
    mu = models.CharField(max_length=20, blank=True, null=True, db_column='目', verbose_name="目")
    ke = models.CharField(max_length=20, blank=True, null=True, db_column='科', verbose_name="科")
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    desc = models.TextField(blank=True, null=True, db_column='生物学特性及发生消长规律', verbose_name='生物学特性及发生消长规律')
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    xuename = models.CharField(max_length=70, blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    control_method = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    image = models.ImageField(upload_to='agridata/images', blank=True, null=True, db_column='图片', verbose_name="图片")

    class Meta:
        db_table = '中国苹果桃梨害虫数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgxzqhDb(models.Model):
    """
    中国行政区划数据库
    """
    citycode = models.IntegerField(blank=True, null=True, db_column='城市编码', verbose_name='城市编码')
    adcode = models.CharField(max_length=6, db_column='地址编码',  verbose_name='地址编码')
    name = models.CharField(max_length=20, db_column='位置名称', verbose_name='位置名称')
    center = models.CharField(max_length=30, db_column='中心坐标', verbose_name='中心坐标')
    level = models.CharField(max_length=10, blank=True, null=True, db_column='位置级别', verbose_name='位置级别')

    class Meta:
        db_table = '中国行政区划数据库'
        unique_together = (('name', 'adcode', 'center'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ZgzynywhYc(models.Model):
    """
    中国重要农业文化遗产
    """
    title = models.CharField(max_length=100, blank=True, null=True, db_column='标题', verbose_name='标题')
    pici = models.CharField(max_length=10, blank=True, null=True, db_column='批次', verbose_name='批次')
    content = UEditorField(verbose_name="内容", db_column="内容", width=800, height=300, default="",
                           toolbars="full", imagePath="resource/images", filePath="resource/file")
    link = models.CharField(max_length=80, blank=True, null=True, db_column='链接', verbose_name='链接')
    source = models.CharField(max_length=60, blank=True, null=True, db_column='来源', verbose_name='来源')
    clicks = models.CharField(max_length=10, blank=True, null=True, db_column='点击次数', verbose_name='点击次数')
    datetime = models.CharField(max_length=20, blank=True, null=True, db_column='日期', verbose_name='日期')

    class Meta:
        db_table = '中国重要农业文化遗产'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ZgzynywhycTp(models.Model):
    """
    中国重要农业文化遗产图片
    """
    title = models.ForeignKey(ZgzynywhYc, blank=True, null=True, db_column='标题', verbose_name='标题', related_name="image")
    image_num = models.IntegerField(blank=True, null=True, db_column='图片号', verbose_name='图片号')
    pici = models.CharField(max_length=20, blank=True, null=True, db_column='批次', verbose_name='批次')
    path = models.ImageField(upload_to='agridata/culture', db_column='路径', verbose_name='路径')

    class Meta:
        db_table = '中国重要农业文化遗产图片'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title.title


class ZwwzfbDb(models.Model):
    """
    作物物种分布数据库
    """
    title = models.CharField(max_length=50, blank=True, null=True, db_column='标题', verbose_name='标题')
    category = models.CharField(max_length=30, blank=True, null=True, db_column='种类', verbose_name='种类')
    path = models.ImageField(max_length=80, blank=True, null=True, db_column='路径', verbose_name='路径')

    class Meta:
        db_table = '作物物种分布数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class XmzzzzhxzzDb(models.Model):
    """
    小麦作物核心种质数据库
    """
    id = models.AutoField(primary_key=True)
    total_id = models.CharField(max_length=10, blank=True, null=True, db_column='统一编号', verbose_name='统一编号')
    unit = models.CharField(max_length=20, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    name = models.CharField(max_length=40, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    xipu = models.CharField(max_length=60, blank=True, null=True, db_column='系谱', verbose_name='系谱')
    source = models.CharField(max_length=40, blank=True, null=True, db_column='来源', verbose_name='来源')
    mang = models.CharField(max_length=10, blank=True, null=True, db_column='芒', verbose_name='芒')
    kese = models.CharField(max_length=10, blank=True, null=True, db_column='壳色', verbose_name='壳色')
    lise = models.CharField(max_length=10, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    dongchun = models.CharField(max_length=10, blank=True, null=True, db_column='冬春性', verbose_name='冬春性')
    mature = models.CharField(max_length=10, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    huilishu = models.IntegerField(blank=True, null=True, db_column='穗粒数', verbose_name='穗粒数')
    huichang = models.IntegerField(blank=True, null=True, db_column='穗长', verbose_name='穗长')
    height = models.IntegerField(blank=True, null=True, db_column='株高', verbose_name='株高')
    qianlizhong = models.FloatField(blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    crude_danbai = models.CharField(max_length=6, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    province = models.CharField(max_length=30, blank=True, null=True, db_column='省份', verbose_name='省份')

    class Meta:
        db_table = '小麦作物核心种质数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class XmxpDb(models.Model):
    """
    小麦系谱数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    unit_id = models.IntegerField(blank=True, null=True, db_column='品资所编号', verbose_name='品资所编号')
    name = models.CharField(max_length=40, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    xipu = models.CharField(max_length=100, blank=True, null=True, db_column='系谱', verbose_name='系谱')
    original_name = models.CharField(max_length=40, blank=True, null=True, db_column='原名', verbose_name='原名')
    source = models.CharField(max_length=40, blank=True, null=True, db_column='来源', verbose_name='来源')
    original_addr = models.CharField(max_length=40, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    unit = models.CharField(max_length=40, blank=True, null=True, db_column='选育单位', verbose_name='选育单位')
    height = models.IntegerField(blank=True, null=True, db_column='株高', verbose_name='株高')
    qian_weight = models.CharField(max_length=6, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    year = models.CharField(max_length=6, blank=True, null=True, db_column='选育年限', verbose_name='选育年限')
    comment = models.CharField(max_length=40, null=True, blank=True, verbose_name="备注", db_column="备注")

    class Meta:
        db_table = '小麦系谱数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class XmxcpzjqxpDb(models.Model):
    """
    小麦育成品种及其系谱数据库
    """
    kucode = models.CharField(max_length=10, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    total_id = models.CharField(max_length=10, blank=True, null=True, db_column='统一编号', verbose_name='统一编号')
    unit = models.CharField(max_length=20, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    name = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    translated_name = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    ke = models.CharField(max_length=30, blank=True, null=True, db_column='科', verbose_name='科')
    shu = models.CharField(max_length=30, blank=True, null=True, db_column='属', verbose_name='属于')
    xuename = models.CharField(max_length=40, blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    xipu = models.CharField(max_length=80, blank=True, null=True, db_column='系谱', verbose_name='系谱')
    xuchengnian = models.CharField(max_length=20, blank=True, null=True, db_column='育成年限', verbose_name='育成年限')
    source = models.CharField(max_length=20, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    altitude = models.CharField(max_length=20, blank=True, null=True, db_column='高程', verbose_name='高程')
    longitude = models.CharField(max_length=10, blank=True, null=True, db_column='东经', verbose_name='东经')
    latitude = models.CharField(max_length=10, blank=True, null=True, db_column='北纬', verbose_name='北纬')
    source_country = models.CharField(max_length=20, blank=True, null=True, db_column='来源国', verbose_name='来源国')
    mang = models.CharField(max_length=10, blank=True, null=True, db_column='芒', verbose_name='芒')
    kese = models.CharField(max_length=10, blank=True, null=True, db_column='壳色', verbose_name='壳色')
    lise = models.CharField(max_length=10, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    dongchun = models.CharField(max_length=20, blank=True, null=True, db_column='冬春性', verbose_name='冬春性')
    mature = models.CharField(max_length=10, blank=True, null=True, db_column='成熟性', verbose_name='成熟性')
    seeds = models.CharField(max_length=10, blank=True, null=True, db_column='穗粒数', verbose_name='穗粒数')
    seedslong = models.CharField(max_length=10, blank=True, null=True, db_column='穗长', verbose_name='穗长')
    height = models.CharField(max_length=10, blank=True, null=True, db_column='株高', verbose_name='株高')
    qianlizhong = models.CharField(max_length=10, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    cudanbai = models.CharField(max_length=10, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    lysine = models.CharField(max_length=10, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    chendianzhi = models.CharField(max_length=10, blank=True, null=True, db_column='沉淀值', verbose_name='沉淀值')
    hardness = models.CharField(max_length=10, blank=True, null=True, db_column='硬度', verbose_name='硬度')
    rongzhong = models.CharField(max_length=10, blank=True, null=True, db_column='容重', verbose_name='容重')
    kanghanxing = models.CharField(max_length=10, blank=True, null=True, db_column='抗旱性', verbose_name='抗旱性')
    nainaoxing = models.CharField(max_length=10, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    yaqinaiyan = models.CharField(max_length=10, blank=True, null=True, db_column='芽期耐盐', verbose_name='芽期耐盐')
    miaoqinaiyan = models.CharField(max_length=10, blank=True, null=True, db_column='苗期耐盐', verbose_name='苗期耐盐')
    tianjiankanghan = models.CharField(max_length=10, blank=True, null=True, db_column='田间抗寒性', verbose_name='田间抗寒性')
    rengongkanghan = models.CharField(max_length=10, blank=True, null=True, db_column='人工抗寒性', verbose_name='人工抗寒性')
    tiaoxiuyzd = models.CharField(max_length=10, blank=True, null=True, db_column='条锈严重度', verbose_name='条锈严重度')
    tiaoxiufyx = models.CharField(max_length=10, blank=True, null=True, db_column='条锈反应型', verbose_name='条锈反应型')
    tiaoxiupbl = models.CharField(max_length=10, blank=True, null=True, db_column='条锈普遍率', verbose_name='条锈普遍率')
    yexiuyzd = models.CharField(max_length=10, blank=True, null=True, db_column='叶锈严重度', verbose_name='叶锈严重度')
    yexiufyx = models.CharField(max_length=10, blank=True, null=True, db_column='叶锈反应型', verbose_name='叶锈反应型')
    yexiuptl = models.CharField(max_length=10, blank=True, null=True, db_column='叶锈普遍率', verbose_name='叶锈普遍率')
    ganxiuyzd = models.CharField(max_length=20, blank=True, null=True, db_column='秆锈严重度', verbose_name='秆锈严重度')
    ganxiufyx = models.CharField(max_length=20, blank=True, null=True, db_column='秆锈反应型', verbose_name='秆锈反应型')
    ganxiuptl = models.CharField(max_length=20, blank=True, null=True, db_column='秆锈普遍率', verbose_name='秆锈普遍率')
    baidfenyzd = models.CharField(max_length=20, blank=True, null=True, db_column='白粉严重度', verbose_name='白粉严重度')
    baifenfyx = models.CharField(max_length=20, blank=True, null=True, db_column='白粉反应型', verbose_name='白粉反应型')
    huangyanbing = models.CharField(max_length=20, blank=True, null=True, db_column='黄矮病', verbose_name='黄矮病')
    chimeibingbh = models.CharField(max_length=20, blank=True, null=True, db_column='赤霉病病穗', verbose_name='赤霉病病穗')
    chimeibingzhi = models.CharField(max_length=20, blank=True, null=True, db_column='赤霉病病指', verbose_name='赤霉病病指')
    chimeibingzs = models.CharField(max_length=20, blank=True, null=True, db_column='赤霉病指数', verbose_name='赤霉病指数')
    chimeikx = models.CharField(max_length=20, blank=True, null=True, db_column='赤霉病抗性', verbose_name='赤霉病抗性')
    gengfuyebj = models.CharField(max_length=20, blank=True, null=True, db_column='根腐叶病级', verbose_name='根腐叶病级')
    gengfuhuibj = models.CharField(max_length=20, blank=True, null=True, db_column='根腐穗病级', verbose_name='根腐穗病级')
    wenkubingbj = models.CharField(max_length=20, blank=True, null=True, db_column='纹枯病病级', verbose_name='纹枯病病级')
    wenkubingpj = models.CharField(max_length=20, blank=True, null=True, db_column='纹枯病评价', verbose_name='纹枯病评价')
    changguanybj = models.CharField(max_length=20, blank=True, null=True, db_column='长管蚜病级', verbose_name='长管蚜病级')
    changguanypj = models.CharField(max_length=20, blank=True, null=True, db_column='长管蚜评价', verbose_name='长管蚜评价')
    erchayabj = models.CharField(max_length=20, blank=True, null=True, db_column='二叉蚜病级', verbose_name='二叉蚜病级')
    erchayapj = models.CharField(max_length=20, blank=True, null=True, db_column='二叉蚜评价', verbose_name='二叉蚜评价')
    other = models.CharField(max_length=20, blank=True, null=True, db_column='其它', verbose_name='其它')
    province = models.CharField(max_length=20, blank=True, null=True, db_column='省份', verbose_name='省份')
    yptype = models.CharField(max_length=20, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    yuanchan = models.CharField(max_length=20, blank=True, null=True, db_column='原产', verbose_name='原产')
    category = models.CharField(max_length=20, blank=True, null=True, db_column='种类', verbose_name='种类')
    qu = models.CharField(max_length=20, blank=True, null=True, db_column='区', verbose_name='区')

    class Meta:
        db_table = '小麦育成品种及其系谱数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SdzzzzhxzzDb(models.Model):
    """
    水稻作物核心种质数据库
    """
    total_id = models.CharField(max_length=10, blank=True, null=True, db_column='统一编号', verbose_name='统一编号')
    name = models.CharField(max_length=40, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    altitude = models.IntegerField(blank=True, null=True, db_column='高程', verbose_name='高程')
    longitude = models.IntegerField(blank=True, null=True, db_column='东经', verbose_name='东经')
    latitude = models.IntegerField(blank=True, null=True, db_column='北纬', verbose_name='北纬')
    source = models.CharField(max_length=40, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    save_unit = models.CharField(max_length=40, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    unit_id = models.CharField(max_length=20, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    indica = models.CharField(max_length=10, blank=True, null=True, db_column='籼粳', verbose_name='籼粳')
    one_early = models.CharField(max_length=10, blank=True, null=True, db_column='早中晚', verbose_name='早中晚')
    land_water = models.CharField(max_length=10, blank=True, null=True, db_column='水陆', verbose_name='水陆')
    sticky = models.CharField(max_length=10, blank=True, null=True, db_column='粘糯', verbose_name='粘糯')
    micolor = models.CharField(max_length=10, blank=True, null=True, db_column='米色', verbose_name='米色')
    mixiang = models.CharField(max_length=10, blank=True, null=True, db_column='米香', verbose_name='米香')
    mangchang = models.CharField(max_length=10, blank=True, null=True, db_column='芒长', verbose_name='芒长')
    litype = models.CharField(max_length=10, blank=True, null=True, db_column='粒形状', verbose_name='粒形状')
    lilong = models.CharField(max_length=10, blank=True, null=True, db_column='粒长度', verbose_name='粒长度')
    changguanbi = models.CharField(max_length=10, blank=True, null=True, db_column='长宽比', verbose_name='长宽比')
    yingjianse = models.CharField(max_length=10, blank=True, null=True, db_column='颖尖色', verbose_name='颖尖色')
    yingkese = models.CharField(max_length=10, blank=True, null=True, db_column='颖壳色', verbose_name='颖壳色')
    yingmaoyn = models.CharField(max_length=6, blank=True, null=True, db_column='颖毛有无', verbose_name='颖毛有无')
    huyingls = models.CharField(max_length=6, blank=True, null=True, db_column='护颖长短', verbose_name='护颖长短')
    yingjianwz = models.CharField(max_length=6, blank=True, null=True, db_column='颖尖弯直', verbose_name='颖尖弯直')
    height = models.IntegerField(blank=True, null=True, db_column='株高', verbose_name='株高')

    chuhuiqi = models.FloatField(blank=True, null=True, db_column='出穗期', verbose_name='出穗期')
    zaomilv = models.FloatField(blank=True, null=True, db_column='糙米率', verbose_name='糙米率')
    jinmilv = models.FloatField(blank=True, null=True, db_column='精米率', verbose_name='精米率')
    ebailv = models.CharField(max_length=8, blank=True, null=True, db_column='垩白率', verbose_name='垩白率')
    protein = models.FloatField(blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    lysine = models.FloatField(blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    starch = models.FloatField(blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    zhilian_starch = models.FloatField(blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    sublian_starch = models.FloatField(blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    huhua_temp = models.FloatField(blank=True, null=True, db_column='糊化温度', verbose_name='糊化温度')
    jiaochoudu = models.IntegerField(blank=True, null=True, db_column='胶稠度', verbose_name='胶稠度')
    miaowen = models.IntegerField(blank=True, null=True, db_column='苗瘟', verbose_name='苗瘟')
    baiyeku = models.IntegerField(blank=True, null=True, db_column='白叶枯', verbose_name='白叶枯')
    wenkubing = models.CharField(max_length=10, blank=True, null=True, db_column='纹枯病', verbose_name='纹枯病')
    hedaoshi = models.IntegerField(blank=True, null=True, db_column='褐稻虱', verbose_name='褐稻虱')
    baibeifeishi = models.IntegerField(blank=True, null=True, db_column='白背飞虱', verbose_name='白背飞虱')
    yaqinaihan = models.IntegerField(blank=True, null=True, db_column='芽期耐寒', verbose_name='芽期耐寒')
    miaoqinaihan = models.IntegerField(blank=True, null=True, db_column='苗期耐旱', verbose_name='苗期耐旱')
    naiyan = models.IntegerField(blank=True, null=True, db_column='耐盐', verbose_name='耐盐')
    pathway = models.CharField(max_length=20, blank=True, null=True, db_column='路径', verbose_name='路径')
    daoqu = models.CharField(max_length=20, blank=True, null=True, db_column='稻区', verbose_name='稻区')

    class Meta:
        db_table = '水稻作物核心种质数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SdycpzjqpxDb(models.Model):
    """
    水稻育成品种及其系谱数据库
    """
    kucode = models.CharField(max_length=10, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    total_id = models.CharField(primary_key=True, max_length=10, db_column='统一编号', verbose_name='统一编号')
    name = models.CharField(max_length=40, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    translanted_name = models.CharField(max_length=40, blank=True, null=True, db_column='译名', verbose_name='译名')
    ke = models.CharField(max_length=30, blank=True, null=True, db_column='科', verbose_name='科')
    shu = models.CharField(max_length=30, blank=True, null=True, db_column='属', verbose_name='属')
    xuename = models.CharField(max_length=40, blank=True, null=True, db_column='拉丁学名', verbose_name="拉丁学名")
    xuanyu_unit = models.CharField(max_length=40, blank=True, null=True, db_column='选育单位', verbose_name='选育单位')
    means_group = models.CharField(max_length=60, blank=True, null=True, db_column='方法及组合', verbose_name='方法及组合')
    unitcode = models.CharField(max_length=20, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    indica = models.CharField(max_length=10, blank=True, null=True, db_column='籼粳', verbose_name='籼粳')
    one_early = models.CharField(max_length=10, blank=True, null=True, db_column='早中晚', verbose_name='早中晚')
    land_water = models.CharField(max_length=10, blank=True, null=True, db_column='水陆', verbose_name='水陆')
    sticky = models.CharField(max_length=10, blank=True, null=True, db_column='粘糯', verbose_name='粘糯')
    micolor = models.CharField(max_length=10, blank=True, null=True, db_column='米色', verbose_name='米色')
    mangchang = models.CharField(max_length=10, blank=True, null=True, db_column='芒长', verbose_name='芒长')
    litype = models.CharField(max_length=10, blank=True, null=True, db_column='粒形状', verbose_name='粒形状')
    lilong = models.CharField(max_length=10, blank=True, null=True, db_column='粒长度', verbose_name='粒长度')
    yingjianse = models.CharField(max_length=10, blank=True, null=True, db_column='颖尖色', verbose_name='颖尖色')
    yingkese = models.CharField(max_length=10, blank=True, null=True, db_column='颖壳色', verbose_name='颖壳色')
    height = models.CharField(max_length=10, blank=True, null=True, db_column='株高', verbose_name='株高')
    chuhuiqi = models.CharField(max_length=10, blank=True, null=True, db_column='出穗期', verbose_name='出穗期')
    zaomilv = models.CharField(max_length=10, blank=True, null=True, db_column='糙米率', verbose_name='糙米率')
    jinmilv = models.CharField(max_length=10, blank=True, null=True, db_column='精米率', verbose_name='精米率')
    ebailv = models.CharField(max_length=10, blank=True, null=True, db_column='垩白率', verbose_name='垩白率')
    danbaizhi = models.CharField(max_length=10, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    lysine = models.CharField(max_length=10, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    total_starch = models.CharField(max_length=10, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    zhi_starch = models.CharField(max_length=10, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    sub_starch = models.CharField(max_length=10, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    temp = models.CharField(max_length=10, blank=True, null=True, db_column='糊化温度', verbose_name='糊化温度')

    jiaochoudu = models.CharField(max_length=10, blank=True, null=True, db_column='胶稠度', verbose_name='胶稠度')
    miaowen = models.CharField(max_length=10, blank=True, null=True, db_column='苗瘟', verbose_name='苗瘟')
    baiyeku = models.CharField(max_length=10, blank=True, null=True, db_column='白叶枯', verbose_name='白叶枯')
    jiaokubing = models.CharField(max_length=10, blank=True, null=True, db_column='纹枯病', verbose_name='纹枯病')
    hedaoshi = models.CharField(max_length=10, blank=True, null=True, db_column='褐稻虱', verbose_name='褐稻虱')
    baibeifeishi = models.CharField(max_length=10, blank=True, null=True, db_column='白背飞虱', verbose_name='白背飞虱')
    yaqinaihan = models.CharField(max_length=10, blank=True, null=True, db_column='芽期耐寒', verbose_name='芽期耐寒')
    miaoqinaihan = models.CharField(max_length=10, blank=True, null=True, db_column='苗期耐旱', verbose_name='苗期耐旱')
    naiyan = models.CharField(max_length=10, blank=True, null=True, db_column='耐盐', verbose_name='耐盐')
    comment = models.CharField(max_length=60, blank=True, null=True, db_column='备注', verbose_name='备注')
    province = models.CharField(max_length=10, blank=True, null=True, db_column='省份', verbose_name='省份')
    yp_type = models.CharField(max_length=10, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')

    class Meta:
        db_table = '水稻育成品种及其系谱数据库'
        unique_together = (('total_id', 'name'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class YmxpzbhDb(models.Model):
    """
    玉米新品种保护数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    name = models.CharField(max_length=20, blank=True, null=True,  db_column='品种名称', verbose_name='品种名称')
    daibiao_breed = models.CharField(max_length=60, blank=True, null=True,  db_column='代表品种', verbose_name='代表品种')
    source = models.CharField(max_length=120, blank=True, null=True,  db_column='来源', verbose_name='来源')

    class Meta:
        db_table = '玉米新品种保护数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class YmzzzzhxzzDb(models.Model):
    """
    玉米作物核心种质数据库
    """
    total_id = models.CharField(max_length=10, blank=True, null=True, db_column='统一编号', verbose_name='统一编号')
    name = models.CharField(max_length=40, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    source = models.CharField(max_length=20, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    qingbenyuan = models.CharField(max_length=40, blank=True, null=True, db_column='亲本来源', verbose_name='亲本来源')
    unit = models.CharField(max_length=40, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    save_id = models.CharField(max_length=20, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    bozhongqi = models.CharField(max_length=20, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    height = models.CharField(max_length=6, blank=True, null=True, db_column='株高', verbose_name='株高')
    huiweigao = models.CharField(max_length=6, blank=True, null=True, db_column='穗位高', verbose_name='穗位高')
    zhujinyeshu = models.CharField(max_length=6, blank=True, null=True, db_column='主茎叶片数', verbose_name='主茎叶片数')
    xionghuifenzishu = models.CharField(max_length=10, blank=True, null=True, db_column='雄穗分枝数', verbose_name='雄穗分枝数')
    chousirishu = models.CharField(max_length=10, blank=True, null=True, db_column='抽丝日数', verbose_name='抽丝日数')
    shengyurishu = models.CharField(max_length=10, blank=True, null=True, db_column='生育日数', verbose_name='生育日数')
    shuanghuilv = models.CharField(max_length=6, blank=True, null=True, db_column='双穗率', verbose_name='双穗率')
    huixing = models.CharField(max_length=10, blank=True, null=True, db_column='穗形', verbose_name='穗形')
    lixing = models.CharField(max_length=10, blank=True, null=True, db_column='粒型', verbose_name='粒型')
    lise = models.CharField(max_length=10, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    youse = models.CharField(max_length=10, blank=True, null=True, db_column='轴色', verbose_name='轴色')
    huichang = models.CharField(max_length=6, blank=True, null=True, db_column='穗长', verbose_name='穗长')
    huicu = models.CharField(max_length=6, blank=True, null=True, db_column='穗粗', verbose_name='穗粗')
    huihangshu = models.CharField(max_length=20, blank=True, null=True, db_column='穗行数', verbose_name='穗行数')
    qianlizhong = models.CharField(max_length=6, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    location = models.CharField(max_length=20, blank=True, null=True, db_column='地点', verbose_name='地点')
    bozhongday = models.CharField(max_length=20, blank=True, null=True, db_column='播种日期', verbose_name='播种日期')
    zhuxing = models.CharField(max_length=20, blank=True, null=True, db_column='株型', verbose_name='株型')
    dzlz = models.CharField(max_length=20, blank=True, null=True, db_column='单株粒重', verbose_name='单株粒重')
    chuzilv = models.CharField(max_length=20, blank=True, null=True, db_column='出籽率', verbose_name='出籽率')
    dabanbing = models.CharField(max_length=20, blank=True, null=True, db_column='大斑病', verbose_name='大斑病')
    xiaobanbing = models.CharField(max_length=20, blank=True, null=True, db_column='小斑病', verbose_name='小斑病')
    heihuibing = models.CharField(max_length=20, blank=True, null=True, db_column='黑穗病', verbose_name='黑穗病')
    huayebing = models.CharField(max_length=20, blank=True, null=True, db_column='花叶病', verbose_name='花叶病')
    cudanbai = models.CharField(max_length=20, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    cuzhifang = models.CharField(max_length=20, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    starch = models.CharField(max_length=20, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    lysine = models.CharField(max_length=20, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')

    class Meta:
        db_table = '玉米作物核心种质数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Xdnysfq(models.Model):
    """
    现代农业示范区
    """
    title = models.CharField(max_length=30, blank=True, null=True, db_column='标题', verbose_name='标题')
    href = models.CharField(max_length=80, blank=True, null=True, db_column='链接', verbose_name='链接')

    class Meta:
        db_table = '现代农业示范区'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ZwyyzyzzDb(models.Model):
    """
    作物优异种质数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=1)
    name = models.CharField(max_length=40, db_column='种质名称', verbose_name='种质名称')
    xiaolei = models.CharField(max_length=20, blank=True, null=True, db_column='种质小类', verbose_name='种质小类')
    dalei = models.CharField(max_length=20, blank=True, null=True, db_column='种质大类', verbose_name='种质大类')
    type = models.CharField(max_length=60, blank=True, null=True, db_column='种质类型', verbose_name='种质类型')
    source = models.TextField(blank=True, null=True, db_column='种质来源', verbose_name='种质来源')
    shape = models.TextField(blank=True, null=True, db_column='优异性状', verbose_name='优异性状')
    values = models.TextField(blank=True, null=True, db_column='利用价值', verbose_name='利用价值')
    evaluate_class = models.CharField(max_length=10, blank=True, null=True, db_column='评定等级', verbose_name='评定等级')
    unit = models.CharField(max_length=30, blank=True, null=True, db_column='联系单位', verbose_name='联系单位')

    class Meta:
        db_table = '作物优异种质数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Youdamai(models.Model):
    """
    大麦作物优异资源综合评价数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    hdhlz = models.CharField(max_length=30, blank=True, null=True, db_column='邯郸穗粒重', verbose_name='邯郸穗粒重')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    hadasulish = models.CharField(max_length=30, blank=True, null=True, db_column='邯郸穗粒数', verbose_name='邯郸穗粒数')
    hashsulish = models.CharField(max_length=30, blank=True, null=True, db_column='哈市穗粒数', verbose_name='哈市穗粒数')
    hazhchshxi = models.CharField(max_length=30, blank=True, null=True, db_column='杭州成熟型', verbose_name='杭州成熟型')
    nayayaqi = models.CharField(max_length=30, blank=True, null=True, db_column='耐盐芽期', verbose_name='耐盐芽期')
    huhuyebi = models.CharField(max_length=30, blank=True, null=True, db_column='黄花叶病', verbose_name='黄花叶病')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    toyibiha = models.CharField(max_length=30, db_column='统一编号', verbose_name='统一编号')
    bejichshxi = models.CharField(max_length=30, blank=True, null=True, db_column='北京成熟型', verbose_name='北京成熟型')
    hadaqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='邯郸千粒重', verbose_name='邯郸千粒重')
    tiwebi = models.CharField(max_length=30, blank=True, null=True, db_column='条纹病', verbose_name='条纹病')
    hazhqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='杭州千粒重', verbose_name='杭州千粒重')
    hashchshxi = models.CharField(max_length=30, blank=True, null=True, db_column='哈市成熟型', verbose_name='哈市成熟型')
    hashsulizh = models.CharField(max_length=30, blank=True, null=True, db_column='哈市穗粒重', verbose_name='哈市穗粒重')
    bejisulish = models.CharField(max_length=30, blank=True, null=True, db_column='北京穗粒数', verbose_name='北京穗粒数')
    hashzhlizh = models.CharField(max_length=30, blank=True, null=True, db_column='哈市株粒重', verbose_name='哈市株粒重')
    bafebi = models.CharField(max_length=30, blank=True, null=True, db_column='白粉病', verbose_name='白粉病')
    bejizhga = models.CharField(max_length=30, blank=True, null=True, db_column='北京株高', verbose_name='北京株高')
    bejizhlizh = models.CharField(max_length=30, blank=True, null=True, db_column='北京株粒重', verbose_name='北京株粒重')
    hadazhga = models.CharField(max_length=30, blank=True, null=True, db_column='邯郸株高', verbose_name='邯郸株高')
    yoyixizh = models.CharField(max_length=30, blank=True, null=True, db_column='优异性状', verbose_name='优异性状')
    hashqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='哈市千粒重', verbose_name='哈市千粒重')
    xinichshxi = models.CharField(max_length=30, blank=True, null=True, db_column='西宁成熟型', verbose_name='西宁成熟型')
    no = models.CharField(db_column='NO', max_length=30, blank=True, null=True, verbose_name='NO')
    hashzhga = models.CharField(max_length=30, blank=True, null=True, db_column='哈市株高', verbose_name='哈市株高')
    xinisulish = models.CharField(max_length=30, blank=True, null=True, db_column='西宁穗粒数', verbose_name='西宁穗粒数')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='棱型', verbose_name='棱型')
    pilu = models.CharField(max_length=30, blank=True, null=True, db_column='皮裸', verbose_name='皮裸')
    hazhzhga = models.CharField(max_length=30, blank=True, null=True, db_column='杭州株高', verbose_name='杭州株高')
    hazhsulish = models.CharField(max_length=30, blank=True, null=True, db_column='杭州穗粒数', verbose_name='杭州穗粒数')
    hadachshxi = models.CharField(max_length=30, blank=True, null=True, db_column='邯郸成熟型', verbose_name='邯郸成熟型')
    nayamiqi = models.CharField(max_length=30, blank=True, null=True, db_column='耐盐苗期', verbose_name='耐盐苗期')
    xinizhga = models.CharField(max_length=30, blank=True, null=True, db_column='西宁株高', verbose_name='西宁株高')
    bejiqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='北京千粒重', verbose_name='北京千粒重')
    chmebi = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病', verbose_name='赤霉病')
    bejisulizh = models.CharField(max_length=30, blank=True, null=True, db_column='北京穗粒重', verbose_name='北京穗粒重')
    hazhsulizh = models.CharField(max_length=30, blank=True, null=True, db_column='杭州穗粒重', verbose_name='杭州穗粒重')
    xinizhlizh = models.CharField(max_length=30, blank=True, null=True, db_column='西宁株粒重', verbose_name='西宁株粒重')
    xiniqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='西宁千粒重', verbose_name='西宁千粒重')
    hadazhlizh = models.CharField(max_length=30, blank=True, null=True, db_column='邯郸株粒重', verbose_name='邯郸株粒重')
    xinisulizh = models.CharField(max_length=30, blank=True, null=True, db_column='西宁穗粒重', verbose_name='西宁穗粒重')
    hazhzhlizh = models.CharField(max_length=30, blank=True, null=True, db_column='杭州株粒重', verbose_name='杭州株粒重')

    class Meta:
        db_table = '大麦作物优异资源综合评价数据库'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class YouYuMi(models.Model):
    """
    玉米作物优异资源综合评价数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    chdusuwega = models.CharField(max_length=30, blank=True, null=True, db_column='成都穗位高', verbose_name='成都穗位高')
    nifetusish = models.CharField(max_length=30, blank=True, null=True, db_column='年份吐丝数', verbose_name='年份吐丝数')
    bejiquchli = models.CharField(max_length=30, blank=True, null=True, db_column='北京区产量', verbose_name='北京区产量')
    yasuwega = models.CharField(max_length=30, blank=True, null=True, db_column='杨穗位高', verbose_name='杨穗位高')
    yalizhsucu = models.CharField(max_length=30, blank=True, null=True, db_column='杨陵镇穗粗', verbose_name='杨陵镇穗粗')
    nifequchli = models.CharField(max_length=30, blank=True, null=True, db_column='年份区产量', verbose_name='年份区产量')
    bejichxish = models.CharField(max_length=30, blank=True, null=True, db_column='北京抽雄数', verbose_name='北京抽雄数')
    pijusxsh = models.CharField(max_length=30, blank=True, null=True, db_column='平均穗行数', verbose_name='平均穗行数')
    pzname = models.CharField(max_length=30, db_column='品种名称', verbose_name='品种名称')
    nifechxish = models.CharField(max_length=30, blank=True, null=True, db_column='年份抽雄数', verbose_name='年份抽雄数')
    gosuwega = models.CharField(max_length=30, blank=True, null=True, db_column='公穗位高', verbose_name='公穗位高')
    pijusuwega = models.CharField(max_length=30, blank=True, null=True, db_column='平均穗位高', verbose_name='平均穗位高')
    chduchxish = models.CharField(max_length=30, blank=True, null=True, db_column='成都抽雄数', verbose_name='成都抽雄数')
    bejisuwega = models.CharField(max_length=30, blank=True, null=True, db_column='北京穗位高', verbose_name='北京穗位高')
    chdutusish = models.CharField(max_length=30, blank=True, null=True, db_column='成都吐丝数', verbose_name='成都吐丝数')
    chdusxsh = models.CharField(max_length=30, blank=True, null=True, db_column='成都穗行数', verbose_name='成都穗行数')
    pijusucu = models.CharField(max_length=30, blank=True, null=True, db_column='平均穗粗', verbose_name='平均穗粗')
    pijuchxish = models.CharField(max_length=30, blank=True, null=True, db_column='平均抽雄数', verbose_name='平均抽雄数')
    bejisxsh = models.CharField(max_length=30, blank=True, null=True, db_column='北京穗行数', verbose_name='北京穗行数')
    gochxish = models.CharField(max_length=30, blank=True, null=True, db_column='公抽雄数', verbose_name='公抽雄数')
    bejichshsh = models.CharField(max_length=30, blank=True, null=True, db_column='北京成熟数', verbose_name='北京成熟数')
    gochshsh = models.CharField(max_length=30, blank=True, null=True, db_column='公成熟数', verbose_name='公成熟数')
    gotusish = models.CharField(max_length=30, blank=True, null=True, db_column='公吐丝数', verbose_name='公吐丝数')
    nifesuwega = models.CharField(max_length=30, blank=True, null=True, db_column='年份穗位高', verbose_name='年份穗位高')
    chduchshsh = models.CharField(max_length=30, blank=True, null=True, db_column='成都成熟数', verbose_name='成都成熟数')
    yatusish = models.CharField(max_length=30, blank=True, null=True, db_column='杨吐丝数', verbose_name='杨吐丝数')
    bejisucu = models.CharField(max_length=30, blank=True, null=True, db_column='北京穗粗', verbose_name='北京穗粗')
    yasxsh = models.CharField(max_length=30, blank=True, null=True, db_column='杨穗行数', verbose_name='杨穗行数')
    goquchli = models.CharField(max_length=30, blank=True, null=True, db_column='公区产量', verbose_name='公区产量')
    chduquchli = models.CharField(max_length=30, blank=True, null=True, db_column='成都区产量', verbose_name='成都区产量')
    gosxsh = models.CharField(max_length=30, blank=True, null=True, db_column='公穗行数', verbose_name='公穗行数')
    yaquchli = models.CharField(max_length=30, blank=True, null=True, db_column='杨区产量', verbose_name='杨区产量')
    yachshsh = models.CharField(max_length=30, blank=True, null=True, db_column='杨成熟数', verbose_name='杨成熟数')
    pijuquchli = models.CharField(max_length=30, blank=True, null=True, db_column='平均区产量', verbose_name='平均区产量')
    bejitusish = models.CharField(max_length=30, blank=True, null=True, db_column='北京吐丝数', verbose_name='北京吐丝数')
    nifechshsh = models.CharField(max_length=30, blank=True, null=True, db_column='年份成熟数', verbose_name='年份成熟数')
    yachxish = models.CharField(max_length=30, blank=True, null=True, db_column='杨抽雄数', verbose_name='杨抽雄数')
    nifesxsh = models.CharField(max_length=30, blank=True, null=True, db_column='年份穗行数', verbose_name='年份穗行数')
    pijutusish = models.CharField(max_length=30, blank=True, null=True, db_column='平均吐丝数', verbose_name='平均吐丝数')
    nifesucu = models.CharField(max_length=30, blank=True, null=True, db_column='年份穗粗', verbose_name='年份穗粗')
    pijuchshsh = models.CharField(max_length=30, blank=True, null=True, db_column='平均成熟数', verbose_name='平均成熟数')
    gozhlisucu = models.CharField(max_length=30, blank=True, null=True, db_column='公主岭穗粗', verbose_name='公主岭穗粗')
    chdusucu = models.CharField(max_length=30, blank=True, null=True, db_column='成都穗粗', verbose_name='成都穗粗')

    class Meta:
        db_table = '玉米作物优异资源综合评价数据库'
        unique_together = (('id', 'pzname'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class sigua(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单瓜重', verbose_name='单瓜重')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    gumilafe = models.CharField(max_length=30, blank=True, null=True, db_column='瓜面腊粉', verbose_name='瓜面腊粉')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜皮色', verbose_name='商瓜皮色')
    lagucise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜次色', verbose_name='老瓜次色')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    lagubawe = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜斑纹', verbose_name='老瓜斑纹')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    lagupise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜皮色', verbose_name='老瓜皮色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='瓜形', verbose_name='瓜形')
    gucidush = models.CharField(max_length=30, blank=True, null=True, db_column='瓜刺多少', verbose_name='瓜刺多少')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    cishhujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='雌首花节位', verbose_name='雌首花节位')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    shgucise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜次色', verbose_name='商瓜次色')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shgubawe = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜斑纹', verbose_name='商瓜斑纹')
    gulexizh = models.CharField(max_length=30, blank=True, null=True, db_column='瓜棱形状', verbose_name='瓜棱形状')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_丝瓜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class yama(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='类型', verbose_name='类型')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    shyurish = models.CharField(max_length=30, blank=True, null=True, db_column='生育日数', verbose_name='生育日数')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    chyolv = models.CharField(max_length=30, blank=True, null=True, db_column='出油率', verbose_name='出油率')
    shlichshqi = models.CharField(max_length=30, blank=True, null=True, db_column='生理成熟期', verbose_name='生理成熟期')
    kahuqi = models.CharField(max_length=30, blank=True, null=True, db_column='开花期', verbose_name='开花期')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    chmiqi = models.CharField(max_length=30, blank=True, null=True, db_column='出苗期', verbose_name='出苗期')
    chmalv = models.CharField(max_length=30, blank=True, null=True, db_column='出麻率', verbose_name='出麻率')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    zhzifaya = models.CharField(max_length=30, blank=True, null=True, db_column='种子发芽', verbose_name='种子发芽')
    gajichli = models.CharField(max_length=30, blank=True, null=True, db_column='干茎产量', verbose_name='干茎产量')
    zhpise = models.CharField(max_length=30, blank=True, null=True, db_column='种皮色', verbose_name='种皮色')
    goyichdu = models.CharField(max_length=30, blank=True, null=True, db_column='工艺长度', verbose_name='工艺长度')
    dazhshgush = models.CharField(max_length=30, blank=True, null=True, db_column='单株朔果数', verbose_name='单株朔果数')
    dazhshchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株生产力', verbose_name='单株生产力')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    xiwechli = models.CharField(max_length=30, blank=True, null=True, db_column='纤维产量', verbose_name='纤维产量')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    pizhdaha = models.CharField(max_length=30, blank=True, null=True, db_column='品种代号', verbose_name='品种代号')
    xiweqidu = models.CharField(max_length=30, blank=True, null=True, db_column='纤维强度', verbose_name='纤维强度')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yujichli = models.CharField(max_length=30, blank=True, null=True, db_column='原茎产量', verbose_name='原茎产量')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    xiweha = models.CharField(max_length=30, blank=True, null=True, db_column='纤维号', verbose_name='纤维号')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    fejish = models.CharField(max_length=30, blank=True, null=True, db_column='分茎数', verbose_name='分茎数')
    yimi = models.CharField(max_length=40, blank=True, null=True, db_column='译名', verbose_name='译名')
    kadafuxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗倒伏性', verbose_name='抗倒伏性')
    kahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱性', verbose_name='抗旱性')
    goyichshqi = models.CharField(max_length=30, blank=True, null=True, db_column='工艺成熟期', verbose_name='工艺成熟期')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    zhzichli = models.CharField(max_length=30, blank=True, null=True, db_column='种子产量', verbose_name='种子产量')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_亚麻'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class qitagualei(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单瓜重', verbose_name='单瓜重')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    gumilafe = models.CharField(max_length=30, blank=True, null=True, db_column='瓜面腊粉', verbose_name='瓜面腊粉')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜皮色', verbose_name='商瓜皮色')
    lagucise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜次色', verbose_name='老瓜次色')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    lagubawe = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜斑纹', verbose_name='老瓜斑纹')
    lagupise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜皮色', verbose_name='老瓜皮色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='瓜形', verbose_name='瓜形')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    shgucise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜次色', verbose_name='商瓜次色')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shgubawe = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜斑纹', verbose_name='商瓜斑纹')
    gulexizh = models.CharField(max_length=30, blank=True, null=True, db_column='瓜棱形状', verbose_name='瓜棱形状')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_其它瓜类'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class qitalvyecai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    yeroma = models.CharField(max_length=30, blank=True, null=True, db_column='叶茸毛', verbose_name='叶茸毛')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    yebizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄长', verbose_name='叶柄长')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶长', verbose_name='叶长')
    yeku = models.CharField(max_length=30, blank=True, null=True, db_column='叶宽', verbose_name='叶宽')
    dazhzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株重', verbose_name='单株重')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    shyomich = models.CharField(max_length=30, blank=True, null=True, db_column='食用名称', verbose_name='食用名称')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yeji = models.CharField(max_length=30, blank=True, null=True, db_column='叶角', verbose_name='叶角')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_其它绿叶菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class qitadoulei(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    zhpicise = models.CharField(max_length=30, blank=True, null=True, db_column='种皮次色', verbose_name='种皮次色')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    zhzipise = models.CharField(max_length=30, blank=True, null=True, db_column='种子皮色', verbose_name='种子皮色')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    yibase = models.CharField(max_length=30, blank=True, null=True, db_column='翼瓣色', verbose_name='翼瓣色')
    zhzixizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子形状', verbose_name='种子形状')
    nejicise = models.CharField(max_length=30, blank=True, null=True, db_column='嫩荚次色', verbose_name='嫩荚次色')
    zhzidaxi = models.CharField(max_length=30, blank=True, null=True, db_column='种子大小', verbose_name='种子大小')
    nejise = models.CharField(max_length=30, blank=True, null=True, db_column='嫩荚色', verbose_name='嫩荚色')
    yibacise = models.CharField(max_length=30, blank=True, null=True, db_column='翼瓣次色', verbose_name='翼瓣次色')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    jiho = models.CharField(max_length=30, blank=True, null=True, db_column='荚厚', verbose_name='荚厚')
    jixi = models.CharField(max_length=30, blank=True, null=True, db_column='荚形', verbose_name='荚形')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    lajirish = models.CharField(max_length=30, blank=True, null=True, db_column='老荚日数', verbose_name='老荚日数')
    dajizh = models.CharField(max_length=30, blank=True, null=True, db_column='单荚重', verbose_name='单荚重')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    qijirish = models.CharField(max_length=30, blank=True, null=True, db_column='青荚日数', verbose_name='青荚日数')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    jiku = models.CharField(max_length=30, blank=True, null=True, db_column='荚宽', verbose_name='荚宽')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_其它豆类'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class donghancai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    roma = models.CharField(max_length=30, blank=True, null=True, db_column='茸毛', verbose_name='茸毛')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    dazhzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株重', verbose_name='单株重')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    yeji = models.CharField(max_length=30, blank=True, null=True, db_column='叶角', verbose_name='叶角')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_冬寒菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class donggua(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    yimi = models.CharField(max_length=40, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单瓜重', verbose_name='单瓜重')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    gumilafe = models.CharField(max_length=30, blank=True, null=True, db_column='瓜面腊粉', verbose_name='瓜面腊粉')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜皮色', verbose_name='商瓜皮色')
    lagucise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜次色', verbose_name='老瓜次色')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    lagubawe = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜斑纹', verbose_name='老瓜斑纹')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    lagupise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜皮色', verbose_name='老瓜皮色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='瓜形', verbose_name='瓜形')
    gucidush = models.CharField(max_length=30, blank=True, null=True, db_column='瓜刺多少', verbose_name='瓜刺多少')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    cishhujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='雌首花节位', verbose_name='雌首花节位')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    shgucise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜次色', verbose_name='商瓜次色')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shgubawe = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜斑纹', verbose_name='商瓜斑纹')
    gulexizh = models.CharField(max_length=30, blank=True, null=True, db_column='瓜棱形状', verbose_name='瓜棱形状')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_冬瓜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class daodou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    dajilish = models.CharField(max_length=30, blank=True, null=True, db_column='单荚粒数', verbose_name='单荚粒数')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_刀豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class fencong(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    jijise = models.CharField(max_length=30, blank=True, null=True, db_column='假茎色', verbose_name='假茎色')
    yelafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶蜡粉', verbose_name='叶蜡粉')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    xiqi = models.CharField(max_length=30, blank=True, null=True, db_column='香气', verbose_name='香气')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    lawe = models.CharField(max_length=30, blank=True, null=True, db_column='辣味', verbose_name='辣味')
    dazhzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株重', verbose_name='单株重')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    fenixi = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖性', verbose_name='分蘖性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_分葱'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class limadou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    sang = models.CharField(max_length=30, blank=True, null=True, db_column='谷氨酸', verbose_name='谷氨酸')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    jiansu = models.CharField(max_length=30, blank=True, null=True, db_column='精氨酸', verbose_name='精氨酸')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    zohe = models.CharField(max_length=30, blank=True, null=True, db_column='总和', verbose_name='总和')
    yiliansu = models.CharField(max_length=30, blank=True, null=True, db_column='异亮氨酸', verbose_name='异亮氨酸')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    seansu = models.CharField(max_length=30, blank=True, null=True, db_column='色氨酸', verbose_name='色氨酸')
    zuansu = models.CharField(max_length=30, blank=True, null=True, db_column='组氨酸', verbose_name='组氨酸')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bebiansu = models.CharField(max_length=30, blank=True, null=True, db_column='苯丙氨酸', verbose_name='苯丙氨酸')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    yueguang = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    las = models.CharField(max_length=30, blank=True, null=True, db_column='酪氨酸', verbose_name='酪氨酸')
    liansu = models.CharField(max_length=30, blank=True, null=True, db_column='亮氨酸', verbose_name='亮氨酸')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    gaansu = models.CharField(max_length=30, blank=True, null=True, db_column='甘氨酸', verbose_name='甘氨酸')
    dajilish = models.CharField(max_length=30, blank=True, null=True, db_column='单荚粒数', verbose_name='单荚粒数')
    xiansu = models.CharField(max_length=30, blank=True, null=True, db_column='缬氨酸', verbose_name='缬氨酸')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    fuansu = models.CharField(max_length=30, blank=True, null=True, db_column='脯氨酸', verbose_name='脯氨酸')
    suannai = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_利马豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class nangua(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    yimi = models.CharField(max_length=40, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单瓜重', verbose_name='单瓜重')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    gumilafe = models.CharField(max_length=30, blank=True, null=True, db_column='瓜面腊粉', verbose_name='瓜面腊粉')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜皮色', verbose_name='商瓜皮色')
    lagucise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜次色', verbose_name='老瓜次色')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    lagubawe = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜斑纹', verbose_name='老瓜斑纹')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    lagupise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜皮色', verbose_name='老瓜皮色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='瓜形', verbose_name='瓜形')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    cishhujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='雌首花节位', verbose_name='雌首花节位')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    shgucise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜次色', verbose_name='商瓜次色')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shgubawe = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜斑纹', verbose_name='商瓜斑纹')
    gulexizh = models.CharField(max_length=30, blank=True, null=True, db_column='瓜棱形状', verbose_name='瓜棱形状')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_南瓜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class yeyongwoju(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    jiqiyufo = models.CharField(max_length=30, blank=True, null=True, db_column='结球与否', verbose_name='结球与否')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    chtaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抽薹性', verbose_name='抽薹性')
    qixi = models.CharField(max_length=30, blank=True, null=True, db_column='球形', verbose_name='球形')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    dazhzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株重', verbose_name='单株重')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    yimi = models.CharField(max_length=40, blank=True, null=True, db_column='译名', verbose_name='译名')
    shfe = models.CharField(max_length=30, blank=True, null=True, db_column='水分', verbose_name='水分')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_叶用莴苣'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class yegaicai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    xilipidush = models.CharField(max_length=30, blank=True, null=True, db_column='小裂片对数', verbose_name='小裂片对数')
    yemilafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶面蜡粉', verbose_name='叶面蜡粉')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='收获期', verbose_name='收获期')
    kazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='开展度', verbose_name='开展度')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yelike = models.CharField(max_length=30, blank=True, null=True, db_column='叶裂刻', verbose_name='叶裂刻')
    dizhqi = models.CharField(max_length=30, blank=True, null=True, db_column='定植期', verbose_name='定植期')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    jilawe = models.CharField(max_length=30, blank=True, null=True, db_column='芥辣味', verbose_name='芥辣味')
    yebiku = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄宽', verbose_name='叶柄宽')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    yebiho = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄厚', verbose_name='叶柄厚')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    shzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='生长期', verbose_name='生长期')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    naihanxing = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    yemicima = models.CharField(max_length=30, blank=True, null=True, db_column='叶面刺毛', verbose_name='叶面刺毛')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    yebizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄长', verbose_name='叶柄长')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    yebitezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄特征', verbose_name='叶柄特征')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶长', verbose_name='叶长')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    jiqixi = models.CharField(max_length=30, blank=True, null=True, db_column='结球性', verbose_name='结球性')
    yeku = models.CharField(max_length=30, blank=True, null=True, db_column='叶宽', verbose_name='叶宽')
    dazhzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株重', verbose_name='单株重')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    yimi = models.CharField(max_length=40, blank=True, null=True, db_column='译名', verbose_name='译名')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    fenixi = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖性', verbose_name='分蘖性')
    yeyi = models.CharField(max_length=30, blank=True, null=True, db_column='叶翼', verbose_name='叶翼')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_叶芥菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class xiangrikui(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    pezhse = models.CharField(max_length=30, blank=True, null=True, db_column='胚轴色', verbose_name='胚轴色')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    zhtose = models.CharField(max_length=30, blank=True, null=True, db_column='柱头色', verbose_name='柱头色')
    hupazhji = models.CharField(max_length=30, blank=True, null=True, db_column='花盘直径', verbose_name='花盘直径')
    zishhayolv = models.CharField(max_length=30, blank=True, null=True, db_column='子实含油率', verbose_name='子实含油率')
    cudabahali = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白含量', verbose_name='粗蛋白含量')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='类型', verbose_name='类型')
    hupaqixidu = models.CharField(max_length=30, blank=True, null=True, db_column='花盘倾斜度', verbose_name='花盘倾斜度')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    shzhhuse = models.CharField(max_length=30, blank=True, null=True, db_column='舌状花色', verbose_name='舌状花色')
    pikelv = models.CharField(max_length=30, blank=True, null=True, db_column='皮壳率', verbose_name='皮壳率')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yojise = models.CharField(max_length=30, blank=True, null=True, db_column='幼茎色', verbose_name='幼茎色')
    shyuriqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育日期', verbose_name='生育日期')
    dazhzishzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株子实重', verbose_name='单株子实重')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    fezhzhlv = models.CharField(max_length=30, blank=True, null=True, db_column='分枝株率', verbose_name='分枝株率')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    hupaxizh = models.CharField(max_length=30, blank=True, null=True, db_column='花盘形状', verbose_name='花盘形状')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    yepish = models.CharField(max_length=30, blank=True, null=True, db_column='叶片数', verbose_name='叶片数')
    biha = models.CharField(max_length=30, blank=True, null=True, db_column='编号', verbose_name='编号')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_向日葵'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class kafei(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shgacudu = models.CharField(max_length=30, blank=True, null=True, db_column='树干粗度', verbose_name='树干粗度')
    neyeyase = models.CharField(max_length=30, blank=True, null=True, db_column='嫩叶颜色', verbose_name='嫩叶颜色')
    yifezhcudu = models.CharField(max_length=30, blank=True, null=True, db_column='一分枝粗度', verbose_name='一分枝粗度')
    disanichli = models.CharField(max_length=30, blank=True, null=True, db_column='第三年产量', verbose_name='第三年产量')
    sinijuch = models.CharField(max_length=30, blank=True, null=True, db_column='四年均产', verbose_name='四年均产')
    zhzhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='种质来源', verbose_name='种质来源')
    yepizhkubi = models.CharField(max_length=30, blank=True, null=True, db_column='叶片长宽比', verbose_name='叶片长宽比')
    yepishga = models.CharField(max_length=30, blank=True, null=True, db_column='叶片手感', verbose_name='叶片手感')
    shguyase = models.CharField(max_length=30, blank=True, null=True, db_column='熟果颜色', verbose_name='熟果颜色')
    yeduxizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶端形状', verbose_name='叶端形状')
    bacujidu = models.CharField(max_length=30, blank=True, null=True, db_column='保存经度', verbose_name='保存经度')
    pijie = models.CharField(db_column='评价E', max_length=30, blank=True, null=True, verbose_name='评价E')
    kahaneli = models.CharField(max_length=30, blank=True, null=True, db_column='抗寒能力', verbose_name='抗寒能力')
    yejixizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶基形状', verbose_name='叶基形状')
    yerohodu = models.CharField(max_length=30, blank=True, null=True, db_column='叶肉厚度', verbose_name='叶肉厚度')
    guzhshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果终熟期', verbose_name='果终熟期')
    shgaxizh = models.CharField(max_length=30, blank=True, null=True, db_column='树干形状', verbose_name='树干形状')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    yiyozhli = models.CharField(max_length=30, blank=True, null=True, db_column='饮用质量', verbose_name='饮用质量')
    dabazh = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    shyoqiku = models.CharField(max_length=30, blank=True, null=True, db_column='使用情况', verbose_name='使用情况')
    zota = models.CharField(max_length=30, blank=True, null=True, db_column='总糖', verbose_name='总糖')
    xirush = models.CharField(max_length=30, blank=True, null=True, db_column='雄蕊数', verbose_name='雄蕊数')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    yijifezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='一级分枝数', verbose_name='一级分枝数')
    bacudimi = models.CharField(max_length=30, blank=True, null=True, db_column='保存地名', verbose_name='保存地名')
    yijizhjiju = models.CharField(max_length=30, blank=True, null=True, db_column='一级枝节距', verbose_name='一级枝节距')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='盛花期', verbose_name='盛花期')
    pjd = models.CharField(db_column='评价D', max_length=30, blank=True, null=True, verbose_name='评价D')
    zhzhmich = models.CharField(max_length=30, blank=True, null=True, db_column='种质名称', verbose_name='种质名称')
    yepishzhzh = models.CharField(max_length=30, blank=True, null=True, db_column='叶片伸展状', verbose_name='叶片伸展状')
    gushqi = models.CharField(max_length=30, blank=True, null=True, db_column='果熟期', verbose_name='果熟期')
    bacuhaba = models.CharField(max_length=30, blank=True, null=True, db_column='保存海拔', verbose_name='保存海拔')
    zhjigujish = models.CharField(max_length=30, blank=True, null=True, db_column='株结果节数', verbose_name='株结果节数')
    yizhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='引种单位', verbose_name='引种单位')
    zhgajish = models.CharField(max_length=30, blank=True, null=True, db_column='主干节数', verbose_name='主干节数')
    hufe = models.CharField(max_length=30, blank=True, null=True, db_column='灰分', verbose_name='灰分')
    mushbuyase = models.CharField(max_length=30, blank=True, null=True, db_column='木栓部颜色', verbose_name='木栓部颜色')
    bacuwedu = models.CharField(max_length=30, blank=True, null=True, db_column='保存纬度', verbose_name='保存纬度')
    diyinichli = models.CharField(max_length=30, blank=True, null=True, db_column='第一年产量', verbose_name='第一年产量')
    gujixizh = models.CharField(max_length=30, blank=True, null=True, db_column='果基形状', verbose_name='果基形状')
    shihuaqi = models.CharField(max_length=30, blank=True, null=True, db_column='始花期', verbose_name='始花期')
    guduxizh = models.CharField(max_length=30, blank=True, null=True, db_column='果端形状', verbose_name='果端形状')
    gufu = models.CharField(max_length=30, blank=True, null=True, db_column='冠幅', verbose_name='冠幅')
    gushshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果盛熟期', verbose_name='果盛熟期')
    baligadozh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒干豆重', verbose_name='百粒干豆重')
    hubash = models.CharField(max_length=30, blank=True, null=True, db_column='花瓣数', verbose_name='花瓣数')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    zhhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='终花期', verbose_name='终花期')
    fazhfash = models.CharField(max_length=30, blank=True, null=True, db_column='繁殖方式', verbose_name='繁殖方式')
    pijia = models.CharField(db_column='评价A', max_length=30, blank=True, null=True, verbose_name='评价A')
    zashxi = models.CharField(max_length=30, blank=True, null=True, db_column='早熟性', verbose_name='早熟性')
    pijic = models.CharField(db_column='评价C', max_length=30, blank=True, null=True, verbose_name='评价C')
    zhzhrupush = models.CharField(max_length=30, blank=True, null=True, db_column='种质入圃数', verbose_name='种质入圃数')
    huzhtozhku = models.CharField(max_length=30, blank=True, null=True, db_column='花柱头状况', verbose_name='花柱头状况')
    shgayase = models.CharField(max_length=30, blank=True, null=True, db_column='树干颜色', verbose_name='树干颜色')
    zhfa = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪', verbose_name='脂肪')
    zhzixizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子形状', verbose_name='种子形状')
    disinichli = models.CharField(max_length=30, blank=True, null=True, db_column='第四年产量', verbose_name='第四年产量')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yepixizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶片形状', verbose_name='叶片形状')
    zhcemajiji = models.CharField(max_length=30, blank=True, null=True, db_column='主侧脉夹角', verbose_name='主侧脉夹角')
    balixiguzh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒鲜果重', verbose_name='百粒鲜果重')
    bacuzudiwe = models.CharField(max_length=30, blank=True, null=True, db_column='保存最低温', verbose_name='保存最低温')
    guxizh = models.CharField(max_length=30, blank=True, null=True, db_column='果形状', verbose_name='果形状')
    bacunijuwe = models.CharField(max_length=30, blank=True, null=True, db_column='保存年均温', verbose_name='保存年均温')
    yehexizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶痕形状', verbose_name='叶痕形状')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    guqidaxi = models.CharField(max_length=30, blank=True, null=True, db_column='果脐大小', verbose_name='果脐大小')
    yepiyase = models.CharField(max_length=30, blank=True, null=True, db_column='叶片颜色', verbose_name='叶片颜色')
    ziyedaxi = models.CharField(max_length=30, blank=True, null=True, db_column='子叶大小', verbose_name='子叶大小')
    jijichdu = models.CharField(max_length=30, blank=True, null=True, db_column='节间长度', verbose_name='节间长度')
    cijifezh = models.CharField(max_length=30, blank=True, null=True, db_column='次级分枝', verbose_name='次级分枝')
    shfe = models.CharField(max_length=30, blank=True, null=True, db_column='水分', verbose_name='水分')
    yeyuzhku = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘状况', verbose_name='叶缘状况')
    teyixizh = models.CharField(max_length=30, blank=True, null=True, db_column='特异性状', verbose_name='特异性状')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    qiguyase = models.CharField(max_length=30, blank=True, null=True, db_column='青果颜色', verbose_name='青果颜色')
    erjifezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='二级分枝数', verbose_name='二级分枝数')
    fezhjijizh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝节间长', verbose_name='分枝节间长')
    dadolv = models.CharField(max_length=30, blank=True, null=True, db_column='单豆率', verbose_name='单豆率')
    xigugadobi = models.CharField(max_length=30, blank=True, null=True, db_column='鲜果干豆比', verbose_name='鲜果干豆比')
    kafeji = models.CharField(max_length=30, blank=True, null=True, db_column='咖啡碱', verbose_name='咖啡碱')
    jizhjiji = models.CharField(max_length=30, blank=True, null=True, db_column='茎枝夹角', verbose_name='茎枝夹角')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='树型', verbose_name='树型')
    huyuta = models.CharField(max_length=30, blank=True, null=True, db_column='还原糖', verbose_name='还原糖')
    diernichli = models.CharField(max_length=30, blank=True, null=True, db_column='第二年产量', verbose_name='第二年产量')
    qishshgu = models.CharField(max_length=30, blank=True, null=True, db_column='果始熟期', verbose_name='果始熟期')
    lvyusu = models.CharField(max_length=30, blank=True, null=True, db_column='绿原酸', verbose_name='绿原酸')
    shfefash = models.CharField(max_length=30, blank=True, null=True, db_column='授粉方式', verbose_name='授粉方式')
    pijib = models.CharField(db_column='评价B', max_length=30, blank=True, null=True, verbose_name='评价B')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    bacuniyuli = models.CharField(max_length=30, blank=True, null=True, db_column='保存年雨量', verbose_name='保存年雨量')
    gupihodu = models.CharField(max_length=30, blank=True, null=True, db_column='果皮厚度', verbose_name='果皮厚度')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_咖啡'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class silengdou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    dabazh = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    dajilish = models.CharField(max_length=30, blank=True, null=True, db_column='单荚粒数', verbose_name='单荚粒数')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    xumi = models.CharField(max_length=50, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_四棱豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class difu(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    zhhuxuchdu = models.CharField(max_length=30, blank=True, null=True, db_column='主花序长度', verbose_name='主花序长度')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    huxuse = models.CharField(max_length=30, blank=True, null=True, db_column='花序色', verbose_name='花序色')
    layudi = models.CharField(max_length=30, blank=True, null=True, db_column='来源地', verbose_name='来源地')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    lebi = models.CharField(max_length=30, blank=True, null=True, db_column='类别', verbose_name='类别')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株形', verbose_name='株形')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    qita = models.CharField(max_length=30, blank=True, null=True, db_column='其它', verbose_name='其它')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_地肤'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class duohuacaidou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    sang = models.CharField(max_length=30, blank=True, null=True, db_column='谷氨酸', verbose_name='谷氨酸')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    jiansu = models.CharField(max_length=30, blank=True, null=True, db_column='精氨酸', verbose_name='精氨酸')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    zohe = models.CharField(max_length=30, blank=True, null=True, db_column='总和', verbose_name='总和')
    las = models.CharField(max_length=30, blank=True, null=True, db_column='酪氨酸', verbose_name='酪氨酸')
    yiliansu = models.CharField(max_length=30, blank=True, null=True, db_column='异亮氨酸', verbose_name='异亮氨酸')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    seansu = models.CharField(max_length=30, blank=True, null=True, db_column='色氨酸', verbose_name='色氨酸')
    zuansu = models.CharField(max_length=30, blank=True, null=True, db_column='组氨酸', verbose_name='组氨酸')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bebiansu = models.CharField(max_length=30, blank=True, null=True, db_column='苯丙氨酸', verbose_name='苯丙氨酸')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    yueguang = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    liansu = models.CharField(max_length=30, blank=True, null=True, db_column='亮氨酸', verbose_name='亮氨酸')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    gaansu = models.CharField(max_length=30, blank=True, null=True, db_column='甘氨酸', verbose_name='甘氨酸')
    dajilish = models.CharField(max_length=30, blank=True, null=True, db_column='单荚粒数', verbose_name='单荚粒数')
    xiansu = models.CharField(max_length=30, blank=True, null=True, db_column='缬氨酸', verbose_name='缬氨酸')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    fuansu = models.CharField(max_length=30, blank=True, null=True, db_column='脯氨酸', verbose_name='脯氨酸')
    naias = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_多花菜豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class dabaicai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yeqizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶球重', verbose_name='叶球重')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    kazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='开展度', verbose_name='开展度')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    yeqiheji = models.CharField(max_length=30, blank=True, null=True, db_column='叶球横径', verbose_name='叶球横径')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='收获期', verbose_name='收获期')
    yimi = models.CharField(max_length=40, blank=True, null=True, db_column='译名', verbose_name='译名')
    kogaxi = models.CharField(max_length=30, blank=True, null=True, db_column='口感性', verbose_name='口感性')
    keroxita = models.CharField(max_length=30, blank=True, null=True, db_column='可溶性糖', verbose_name='可溶性糖')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    shmefabilv = models.CharField(max_length=30, blank=True, null=True, db_column='霜霉发病率', verbose_name='霜霉发病率')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    xumi = models.CharField(max_length=50, blank=True, null=True, db_column='学名', verbose_name='学名')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    yeqibahexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶球抱合型', verbose_name='叶球抱合型')
    yeqixi = models.CharField(max_length=30, blank=True, null=True, db_column='叶球心', verbose_name='叶球心')
    tufabilv = models.CharField(db_column='TUMV发病率', max_length=30, blank=True, null=True, verbose_name='TUMV发病率')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    shfe = models.CharField(max_length=30, blank=True, null=True, db_column='水分', verbose_name='水分')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    cuxiwe = models.CharField(max_length=30, blank=True, null=True, db_column='粗纤维', verbose_name='粗纤维')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    yeqixizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶球形状', verbose_name='叶球形状')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    shzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='生长期', verbose_name='生长期')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    yeqidi = models.CharField(max_length=30, blank=True, null=True, db_column='叶球顶', verbose_name='叶球顶')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    xiwehali = models.CharField(max_length=30, blank=True, null=True, db_column='纤维含量', verbose_name='纤维含量')
    nahanxin = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    yeqizoji = models.CharField(max_length=30, blank=True, null=True, db_column='叶球纵径', verbose_name='叶球纵径')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_大白菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class dacong(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    jijise = models.CharField(max_length=30, blank=True, null=True, db_column='假茎色', verbose_name='假茎色')
    yelafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶蜡粉', verbose_name='叶蜡粉')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    wapiseze = models.CharField(max_length=30, blank=True, null=True, db_column='外皮色泽', verbose_name='外皮色泽')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    xiqi = models.CharField(max_length=30, blank=True, null=True, db_column='香气', verbose_name='香气')
    lijirose = models.CharField(max_length=30, blank=True, null=True, db_column='鳞茎肉色', verbose_name='鳞茎肉色')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    jijixizh = models.CharField(max_length=30, blank=True, null=True, db_column='假茎形状', verbose_name='假茎形状')
    jijizh = models.CharField(max_length=30, blank=True, null=True, db_column='假茎重', verbose_name='假茎重')
    yecu = models.CharField(max_length=30, blank=True, null=True, db_column='叶粗', verbose_name='叶粗')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    dazhzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株重', verbose_name='单株重')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    fenixi = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖性', verbose_name='分蘖性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_大葱'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class dadou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    banadeji3 = models.CharField(max_length=30, blank=True, null=True, db_column='孢囊等级3', verbose_name='孢囊等级3')
    pzname = models.CharField(max_length=40, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    biduzhsh = models.CharField(max_length=30, blank=True, null=True, db_column='病毒指数', verbose_name='病毒指数')
    qise = models.CharField(max_length=30, blank=True, null=True, db_column='脐色', verbose_name='脐色')
    xibideji = models.CharField(max_length=30, blank=True, null=True, db_column='锈病等级', verbose_name='锈病等级')
    shqikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟期抗旱性', verbose_name='熟期抗旱性')
    miqikale = models.CharField(max_length=30, blank=True, null=True, db_column='苗期抗冷', verbose_name='苗期抗冷')
    yosu = models.CharField(max_length=30, blank=True, null=True, db_column='油酸', verbose_name='油酸')
    shyuyufe = models.CharField(max_length=30, blank=True, null=True, db_column='生育月份', verbose_name='生育月份')
    chdilayu = models.CharField(max_length=30, blank=True, null=True, db_column='产地来源', verbose_name='产地来源')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='类型', verbose_name='类型')
    yizhsu = models.CharField(max_length=30, blank=True, null=True, db_column='硬脂酸', verbose_name='硬脂酸')
    shyurish = models.CharField(max_length=30, blank=True, null=True, db_column='生育日数', verbose_name='生育日数')
    yimeyizhji = models.CharField(max_length=30, blank=True, null=True, db_column='胰酶抑制剂', verbose_name='胰酶抑制剂')
    yimi = models.CharField(max_length=40, blank=True, null=True, db_column='译名', verbose_name='译名')
    banadeji1 = models.CharField(max_length=30, blank=True, null=True, db_column='孢囊等级1', verbose_name='孢囊等级1')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yayosu = models.CharField(max_length=30, blank=True, null=True, db_column='亚油酸', verbose_name='亚油酸')
    doji = models.CharField(max_length=30, blank=True, null=True, db_column='东经', verbose_name='东经')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    ruzhsu = models.CharField(max_length=30, blank=True, null=True, db_column='软脂酸', verbose_name='软脂酸')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    pijubana5 = models.CharField(max_length=30, blank=True, null=True, db_column='平均孢囊5', verbose_name='平均孢囊5')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    banadeji5 = models.CharField(max_length=30, blank=True, null=True, db_column='孢囊等级5', verbose_name='孢囊等级5')
    yueguang = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    pijubana1 = models.CharField(max_length=30, blank=True, null=True, db_column='平均孢囊1', verbose_name='平均孢囊1')
    banadeji2 = models.CharField(max_length=30, blank=True, null=True, db_column='孢囊等级2', verbose_name='孢囊等级2')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    xibikabixi = models.CharField(max_length=30, blank=True, null=True, db_column='锈病抗病性', verbose_name='锈病抗病性')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    bewe = models.CharField(max_length=30, blank=True, null=True, db_column='北纬', verbose_name='北纬')
    yaqikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='芽期抗旱性', verbose_name='芽期抗旱性')
    pijubana3 = models.CharField(max_length=30, blank=True, null=True, db_column='平均孢囊3', verbose_name='平均孢囊3')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    banazhsh3 = models.CharField(max_length=30, blank=True, null=True, db_column='孢囊指数3', verbose_name='孢囊指数3')
    qu = models.CharField(max_length=30, blank=True, null=True, db_column='区', verbose_name='区')
    xibifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='锈病反应型', verbose_name='锈病反应型')
    yaqikale = models.CharField(max_length=30, blank=True, null=True, db_column='芽期抗冷', verbose_name='芽期抗冷')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    bezh = models.TextField(blank=True, null=True, db_column='备注', verbose_name='备注')
    banadeji4 = models.CharField(max_length=30, blank=True, null=True, db_column='孢囊等级4', verbose_name='孢囊等级4')
    miqikayaxi = models.CharField(max_length=30, blank=True, null=True, db_column='苗期抗盐性', verbose_name='苗期抗盐性')
    ziyese = models.CharField(max_length=30, blank=True, null=True, db_column='子叶色', verbose_name='子叶色')
    bidudeji = models.CharField(max_length=30, blank=True, null=True, db_column='病毒等级', verbose_name='病毒等级')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    romase = models.CharField(max_length=30, blank=True, null=True, db_column='茸毛色', verbose_name='茸毛色')
    gach = models.CharField(max_length=30, blank=True, null=True, db_column='高程', verbose_name='高程')
    pijubana4 = models.CharField(max_length=30, blank=True, null=True, db_column='平均孢囊4', verbose_name='平均孢囊4')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    yaqikayaxi = models.CharField(max_length=30, blank=True, null=True, db_column='芽期抗盐性', verbose_name='芽期抗盐性')
    pijubana2 = models.CharField(max_length=30, blank=True, null=True, db_column='平均孢囊2', verbose_name='平均孢囊2')
    yamasu = models.CharField(max_length=30, blank=True, null=True, db_column='亚麻酸', verbose_name='亚麻酸')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_大豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class Zuodamai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    sulish = models.CharField(max_length=30, blank=True, null=True, db_column='穗粒数', verbose_name='穗粒数')
    pzname = models.CharField(max_length=60, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    xuyudawe = models.CharField(max_length=30, blank=True, null=True, db_column='选育单位', verbose_name='选育单位')
    dochxi = models.CharField(max_length=30, blank=True, null=True, db_column='冬春性', verbose_name='冬春性')
    nalajibi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝级别', verbose_name='耐涝级别')
    dadichshxi = models.CharField(max_length=30, blank=True, null=True, db_column='当地成熟型', verbose_name='当地成熟型')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    tiwebibilv = models.CharField(max_length=30, blank=True, null=True, db_column='条纹病病率', verbose_name='条纹病病率')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    maxi = models.CharField(max_length=30, blank=True, null=True, db_column='芒性', verbose_name='芒性')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    doji = models.CharField(max_length=30, blank=True, null=True, db_column='东经', verbose_name='东经')
    xumi = models.CharField(max_length=50, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    huhufabilv = models.CharField(max_length=30, blank=True, null=True, db_column='黄花发病率', verbose_name='黄花发病率')
    pilu = models.CharField(max_length=30, blank=True, null=True, db_column='皮裸', verbose_name='皮裸')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    bewe = models.CharField(max_length=30, blank=True, null=True, db_column='北纬', verbose_name='北纬')
    kese = models.CharField(max_length=30, blank=True, null=True, db_column='壳色', verbose_name='壳色')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    suhemase = models.CharField(max_length=30, blank=True, null=True, db_column='穗和芒色', verbose_name='穗和芒色')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    huaiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='黄矮严重度', verbose_name='黄矮严重度')
    chmebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病抗性', verbose_name='赤霉病抗性')
    huhuyekaxi = models.CharField(max_length=30, blank=True, null=True, db_column='黄花叶抗性', verbose_name='黄花叶抗性')
    mx = models.CharField(max_length=30, blank=True, null=True, db_column='芒形', verbose_name='芒形')
    huhuhuhudu = models.CharField(max_length=30, blank=True, null=True, db_column='黄花黄化度', verbose_name='黄花黄化度')
    tahuli = models.CharField(max_length=30, blank=True, null=True, db_column='糖化力', verbose_name='糖化力')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    tiwebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='条纹病抗性', verbose_name='条纹病抗性')
    chmebisulv = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病穗率', verbose_name='赤霉病穗率')
    sumidu = models.CharField(max_length=30, blank=True, null=True, db_column='穗密度', verbose_name='穗密度')
    chmebizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病指数', verbose_name='赤霉病指数')
    xipu = models.CharField(max_length=60, blank=True, null=True, db_column='系谱', verbose_name='系谱')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='棱型', verbose_name='棱型')
    shmibafech = models.CharField(max_length=30, blank=True, null=True, db_column='水敏百分差', verbose_name='水敏百分差')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    nayajibi = models.CharField(max_length=30, blank=True, null=True, db_column='耐盐级别', verbose_name='耐盐级别')
    yimi = models.CharField(max_length=60, blank=True, null=True, db_column='译名', verbose_name='译名')
    shmichdu = models.CharField(max_length=30, blank=True, null=True, db_column='水敏称度', verbose_name='水敏称度')
    gach = models.CharField(max_length=30, blank=True, null=True, db_column='高程', verbose_name='高程')
    kahajibi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱级别', verbose_name='抗旱级别')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    qufejichwu = models.CharField(max_length=30, blank=True, null=True, db_column='全粉浸出物', verbose_name='全粉浸出物')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    fenili = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖力', verbose_name='分蘖力')
    naias = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    juyudu = models.CharField(max_length=30, blank=True, null=True, db_column='均匀度', verbose_name='均匀度')
    yahabijibi = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病级别', verbose_name='蚜害病级别')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    yomise = models.CharField(max_length=30, blank=True, null=True, db_column='幼苗色', verbose_name='幼苗色')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='容重', verbose_name='容重')
    yapile = models.CharField(max_length=30, blank=True, null=True, db_column='样品类', verbose_name='样品类')
    chbabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='赤斑病评价', verbose_name='赤斑病评价')
    yahabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病评价', verbose_name='蚜害病评价')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    sx = models.CharField(max_length=30, blank=True, null=True, db_column='穗形', verbose_name='穗形')
    bafefayixi = models.CharField(max_length=30, blank=True, null=True, db_column='白粉反应型', verbose_name='白粉反应型')
    wekubi = models.CharField(max_length=30, blank=True, null=True, db_column='纹枯病', verbose_name='纹枯病')
    yahabizhsh = models.CharField(max_length=10, blank=True, null=True, db_column='蚜害病指数', verbose_name='蚜害病指数')
    balizh = models.CharField(max_length=10, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    shyurish = models.CharField(max_length=30, blank=True, null=True, db_column='生育日数', verbose_name='生育日数')
    zhfasu16 = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪酸160', verbose_name='脂肪酸160')
    yexiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='叶锈严重度', verbose_name='叶锈严重度')
    ebalv = models.CharField(max_length=10, blank=True, null=True, db_column='垩白率', verbose_name='垩白率')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    kahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱性', verbose_name='抗旱性')
    yexifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='叶锈反应型', verbose_name='叶锈反应型')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    yahazhsh = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害指数', verbose_name='蚜害指数')
    jinuxi = models.CharField(max_length=30, blank=True, null=True, db_column='粳糯性', verbose_name='粳糯性')
    subizh = models.CharField(max_length=30, blank=True, null=True, db_column='穗柄长', verbose_name='穗柄长')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    mixi = models.CharField(max_length=30, blank=True, null=True, db_column='米香', verbose_name='米香')
    hebabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='褐斑病指数', verbose_name='褐斑病指数')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    laanzhdaba = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨占蛋白', verbose_name='赖氨占蛋白')
    chmebibisu = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病病穗', verbose_name='赤霉病病穗')
    babefesh = models.CharField(max_length=30, blank=True, null=True, db_column='白背飞虱', verbose_name='白背飞虱')
    v = models.CharField(db_column='VE', max_length=30, blank=True, null=True, verbose_name='VE')
    chbabiji = models.CharField(max_length=30, blank=True, null=True, db_column='赤斑病级', verbose_name='赤斑病级')
    gefubizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='根腐病指数', verbose_name='根腐病指数')
    mise = models.CharField(max_length=30, blank=True, null=True, db_column='米色', verbose_name='米色')
    jizhlv = models.CharField(max_length=30, blank=True, null=True, db_column='角质率', verbose_name='角质率')
    gaxifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈反应型', verbose_name='秆锈反应型')
    yomiyese = models.CharField(max_length=30, blank=True, null=True, db_column='幼苗叶色', verbose_name='幼苗叶色')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    tixipubilv = models.CharField(max_length=30, blank=True, null=True, db_column='条锈普遍率', verbose_name='条锈普遍率')
    dazhlizh = models.CharField(max_length=30, blank=True, null=True, db_column='单株粒重', verbose_name='单株粒重')
    galiyakaji = models.CharField(db_column="'高粱蚜抗级", max_length=30, blank=True, null=True, verbose_name='')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    yimayowu = models.CharField(max_length=30, blank=True, null=True, db_column='颖毛有无', verbose_name='颖毛有无')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    yaqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='芽期抗旱', verbose_name='芽期抗旱')
    vb = models.CharField(db_column='VB2', max_length=30, blank=True, null=True, verbose_name='VB2')
    yubiha = models.CharField(max_length=30, blank=True, null=True, db_column='原编号', verbose_name='原编号')
    yexipubilv = models.CharField(max_length=30, blank=True, null=True, db_column='叶锈普遍率', verbose_name='叶锈普遍率')
    zazhwa = models.CharField(max_length=30, blank=True, null=True, db_column='早中晚', verbose_name='早中晚')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    xuyufafa = models.CharField(max_length=30, blank=True, null=True, db_column='选育方法', verbose_name='选育方法')
    dazhsuzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株穗重', verbose_name='单株穗重')
    chdu = models.CharField(max_length=30, blank=True, null=True, db_column='锤度', verbose_name='锤度')
    tixifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='条锈反应型', verbose_name='条锈反应型')
    xiji = models.CharField(max_length=30, blank=True, null=True, db_column='籼粳', verbose_name='籼粳')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    chsurish = models.CharField(max_length=30, blank=True, null=True, db_column='抽穗日数', verbose_name='抽穗日数')
    layudi = models.CharField(max_length=30, blank=True, null=True, db_column='来源地', verbose_name='来源地')
    gaxiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈严重度', verbose_name='秆锈严重度')
    miwe = models.CharField(max_length=30, blank=True, null=True, db_column='苗瘟', verbose_name='苗瘟')
    shqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='熟期抗旱', verbose_name='熟期抗旱')
    fenish = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖数', verbose_name='分蘖数')
    sihesubilv = models.CharField(max_length=30, blank=True, null=True, db_column='丝黑穗病率', verbose_name='丝黑穗病率')
    tijikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='田间抗寒性', verbose_name='田间抗寒性')
    miqinaha = models.CharField(max_length=30, blank=True, null=True, db_column='苗期耐旱', verbose_name='苗期耐旱')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    yizhjish = models.CharField(max_length=30, blank=True, null=True, db_column='一株茎数', verbose_name='一株茎数')
    gujikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='灌浆抗寒性', verbose_name='灌浆抗寒性')
    ma = models.CharField(max_length=30, blank=True, null=True, db_column='芒', verbose_name='芒')
    chsuqi = models.CharField(max_length=30, blank=True, null=True, db_column='出穗期', verbose_name='出穗期')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒型', verbose_name='粒型')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    zhjijish = models.CharField(max_length=30, blank=True, null=True, db_column='主茎节数', verbose_name='主茎节数')
    jicu = models.CharField(max_length=30, blank=True, null=True, db_column='茎粗', verbose_name='茎粗')
    bafeyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='白粉严重度', verbose_name='白粉严重度')
    yaqinaha = models.CharField(max_length=30, blank=True, null=True, db_column='芽期耐寒', verbose_name='芽期耐寒')
    yahabiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病级', verbose_name='蚜害病级')
    yebabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='叶斑病指数', verbose_name='叶斑病指数')
    zhjichdu = models.CharField(max_length=30, blank=True, null=True, db_column='主茎长度', verbose_name='主茎长度')
    fenixi = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖性', verbose_name='分蘖性')
    yidu = models.CharField(max_length=30, blank=True, null=True, db_column='硬度', verbose_name='硬度')
    gefusubiji = models.CharField(max_length=30, blank=True, null=True, db_column='根腐穗病级', verbose_name='根腐穗病级')
    yijise = models.CharField(max_length=30, blank=True, null=True, db_column='颖尖色', verbose_name='颖尖色')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    lx = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    zhfasu18 = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪酸183', verbose_name='脂肪酸183')
    shbiha = models.CharField(max_length=30, blank=True, null=True, db_column='省编号', verbose_name='省编号')
    yuchnixi = models.CharField(max_length=30, blank=True, null=True, db_column='育成年限', verbose_name='育成年限')
    yikese = models.CharField(max_length=30, blank=True, null=True, db_column='颖壳色', verbose_name='颖壳色')
    xibipiji = models.CharField(max_length=30, blank=True, null=True, db_column='锈病评价', verbose_name='锈病评价')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    dazhgazh = models.CharField(max_length=30, blank=True, null=True, db_column='单株秆重', verbose_name='单株秆重')
    shfe = models.CharField(max_length=30, blank=True, null=True, db_column='水份', verbose_name='水份')
    chdizh = models.CharField(max_length=30, blank=True, null=True, db_column='沉淀值', verbose_name='沉淀值')
    jimilv = models.CharField(max_length=30, blank=True, null=True, db_column='精米率', verbose_name='精米率')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    yebabiji = models.CharField(max_length=30, blank=True, null=True, db_column='叶斑病级', verbose_name='叶斑病级')
    zhjizhji = models.CharField(max_length=30, blank=True, null=True, db_column='主茎直径', verbose_name='主茎直径')
    zhkelv = models.CharField(max_length=30, blank=True, null=True, db_column='着壳率', verbose_name='着壳率')
    gefuyebiji = models.CharField(max_length=30, blank=True, null=True, db_column='根腐叶病级', verbose_name='根腐叶病级')
    zhkubi = models.CharField(max_length=30, blank=True, null=True, db_column='长宽比', verbose_name='长宽比')
    xibizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='锈病指数', verbose_name='锈病指数')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    xi = models.CharField(max_length=30, blank=True, null=True, db_column='硒', verbose_name='硒')
    yikebapidu = models.CharField(max_length=30, blank=True, null=True, db_column='颖壳包皮度', verbose_name='颖壳包皮度')
    yaqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='芽期耐盐', verbose_name='芽期耐盐')
    bacudawe_2 = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位_2', verbose_name='保存单位_2')
    yoxizh = models.CharField(max_length=30, blank=True, null=True, db_column='有效枝', verbose_name='有效枝')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    yibehazhlv = models.CharField(max_length=30, blank=True, null=True, db_column='蝇被害株率', verbose_name='蝇被害株率')
    yaqinayaxi = models.CharField(max_length=30, blank=True, null=True, db_column='芽期耐盐性', verbose_name='芽期耐盐性')
    yumimikaji = models.CharField(max_length=30, blank=True, null=True, db_column='玉米螟抗级', verbose_name='玉米螟抗级')
    gefusu = models.CharField(max_length=30, blank=True, null=True, db_column='根腐穗', verbose_name='根腐穗')
    huaibi = models.CharField(max_length=30, blank=True, null=True, db_column='黄矮病', verbose_name='黄矮病')
    jichdu = models.CharField(max_length=30, blank=True, null=True, db_column='胶稠度', verbose_name='胶稠度')
    gaansu = models.CharField(max_length=30, blank=True, null=True, db_column='甘氨酸', verbose_name='甘氨酸')
    yebabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='叶斑病评价', verbose_name='叶斑病评价')
    guwebijibi = models.CharField(max_length=30, blank=True, null=True, db_column='谷瘟病级别', verbose_name='谷瘟病级别')
    miqinayaxi = models.CharField(max_length=30, blank=True, null=True, db_column='苗期耐盐性', verbose_name='苗期耐盐性')
    layugu = models.CharField(max_length=30, blank=True, null=True, db_column='来源国', verbose_name='来源国')
    yijiwazh = models.CharField(max_length=30, blank=True, null=True, db_column='颖尖弯直', verbose_name='颖尖弯直')
    kalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗涝性', verbose_name='抗涝性')
    dabazh = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    cimachdu = models.CharField(max_length=30, blank=True, null=True, db_column='刺毛长度', verbose_name='刺毛长度')
    dafuxi = models.CharField(max_length=30, blank=True, null=True, db_column='倒伏性', verbose_name='倒伏性')
    yibehazhsh = models.CharField(max_length=30, blank=True, null=True, db_column='蝇被害指数', verbose_name='蝇被害指数')
    chmebibizh = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病病指', verbose_name='赤霉病病指')
    fafajizuhe = models.CharField(max_length=30, blank=True, null=True, db_column='方法及组合', verbose_name='方法及组合')
    hebabiji = models.CharField(max_length=30, blank=True, null=True, db_column='褐斑病级', verbose_name='褐斑病级')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    xings = models.CharField(max_length=30, blank=True, null=True, db_column='穗型', verbose_name='穗型')
    regokahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='人工抗寒性', verbose_name='人工抗寒性')
    mazh = models.CharField(max_length=30, blank=True, null=True, db_column='芒长', verbose_name='芒长')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    zhpiguze = models.CharField(max_length=30, blank=True, null=True, db_column='种皮光泽', verbose_name='种皮光泽')
    zhfasu20 = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪酸200', verbose_name='脂肪酸200')
    yirushji = models.CharField(max_length=30, blank=True, null=True, db_column='引入时间', verbose_name='引入时间')
    gaxipubilv = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈普遍率', verbose_name='秆锈普遍率')
    camilv = models.CharField(max_length=30, blank=True, null=True, db_column='糙米率', verbose_name='糙米率')
    yueguang = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    yahabizh = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害比值', verbose_name='蚜害比值')
    susoji = models.CharField(max_length=30, blank=True, null=True, db_column='穗松紧', verbose_name='穗松紧')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_大麦'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class dama(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    zhzihayolv = models.CharField(max_length=30, blank=True, null=True, db_column='种子含油率', verbose_name='种子含油率')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    zhzichshqi = models.CharField(max_length=30, blank=True, null=True, db_column='种子成熟期', verbose_name='种子成熟期')
    xiweqili = models.CharField(max_length=30, blank=True, null=True, db_column='纤维强力', verbose_name='纤维强力')
    zhzimuch = models.CharField(max_length=30, blank=True, null=True, db_column='种子亩产', verbose_name='种子亩产')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    xiwemuch = models.CharField(max_length=30, blank=True, null=True, db_column='纤维亩产', verbose_name='纤维亩产')
    xiwechdu = models.CharField(max_length=30, blank=True, null=True, db_column='纤维长度', verbose_name='纤维长度')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    gajichmalv = models.CharField(max_length=30, blank=True, null=True, db_column='干茎出麻率', verbose_name='干茎出麻率')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    xipezhse = models.CharField(max_length=30, blank=True, null=True, db_column='下胚轴色', verbose_name='下胚轴色')
    yedaxi = models.CharField(max_length=30, blank=True, null=True, db_column='叶大小', verbose_name='叶大小')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    kahuqi = models.CharField(max_length=30, blank=True, null=True, db_column='开花期', verbose_name='开花期')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yetiji = models.CharField(max_length=30, blank=True, null=True, db_column='叶跳甲', verbose_name='叶跳甲')
    camashyiqi = models.CharField(max_length=30, blank=True, null=True, db_column='采麻收刈期', verbose_name='采麻收刈期')
    yomixiyese = models.CharField(max_length=30, blank=True, null=True, db_column='幼苗心叶色', verbose_name='幼苗心叶色')
    zhqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种千粒重', verbose_name='种千粒重')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    zhpihuwe = models.CharField(max_length=30, blank=True, null=True, db_column='种皮花纹', verbose_name='种皮花纹')
    zhpise = models.CharField(max_length=30, blank=True, null=True, db_column='种皮色', verbose_name='种皮色')
    xiwehodu = models.CharField(max_length=30, blank=True, null=True, db_column='纤维厚度', verbose_name='纤维厚度')
    chmiqi = models.CharField(max_length=30, blank=True, null=True, db_column='出苗期', verbose_name='出苗期')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_大麻'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class nenjinghuayecai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    huqiheji = models.CharField(max_length=30, blank=True, null=True, db_column='花球横径', verbose_name='花球横径')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    huqipizh = models.CharField(max_length=30, blank=True, null=True, db_column='花球品质', verbose_name='花球品质')
    yemilafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶面蜡粉', verbose_name='叶面蜡粉')
    qijise = models.CharField(max_length=30, blank=True, null=True, db_column='球茎色', verbose_name='球茎色')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    huqixizh = models.CharField(max_length=30, blank=True, null=True, db_column='花球形状', verbose_name='花球形状')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    dizhqi = models.CharField(max_length=30, blank=True, null=True, db_column='定植期', verbose_name='定植期')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    hulese = models.CharField(max_length=30, blank=True, null=True, db_column='花蕾色', verbose_name='花蕾色')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='收获期', verbose_name='收获期')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    huqizoji = models.CharField(max_length=30, blank=True, null=True, db_column='花球纵径', verbose_name='花球纵径')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    xumi = models.CharField(max_length=50, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    huqijishdu = models.CharField(max_length=30, blank=True, null=True, db_column='花球紧实度', verbose_name='花球紧实度')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    huqizh = models.CharField(max_length=30, blank=True, null=True, db_column='花球重', verbose_name='花球重')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    naihanxing = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_嫩茎花椰菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class zigaicai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    geyotu = models.CharField(max_length=30, blank=True, null=True, db_column='根用途', verbose_name='根用途')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    xilipidush = models.CharField(max_length=30, blank=True, null=True, db_column='小裂片对数', verbose_name='小裂片对数')
    yemilafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶面蜡粉', verbose_name='叶面蜡粉')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    zhzixizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子形状', verbose_name='种子形状')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yelike = models.CharField(max_length=30, blank=True, null=True, db_column='叶裂刻', verbose_name='叶裂刻')
    dizhqi = models.CharField(max_length=30, blank=True, null=True, db_column='定植期', verbose_name='定植期')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    jilawe = models.CharField(max_length=30, blank=True, null=True, db_column='芥辣味', verbose_name='芥辣味')
    xumi = models.CharField(max_length=60, blank=True, null=True, db_column='学名', verbose_name='学名')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    shzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='生长期', verbose_name='生长期')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='收获期', verbose_name='收获期')
    yecu = models.CharField(max_length=30, blank=True, null=True, db_column='叶簇', verbose_name='叶簇')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    yemicima = models.CharField(max_length=30, blank=True, null=True, db_column='叶面刺毛', verbose_name='叶面刺毛')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    naihanxing = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    zhziyase = models.CharField(max_length=30, blank=True, null=True, db_column='种子颜色', verbose_name='种子颜色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    yeyi = models.CharField(max_length=30, blank=True, null=True, db_column='叶翼', verbose_name='叶翼')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_子芥菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class xiaobiandou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    sang = models.CharField(max_length=30, blank=True, null=True, db_column='谷氨酸', verbose_name='谷氨酸')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    jiansu = models.CharField(max_length=30, blank=True, null=True, db_column='精氨酸', verbose_name='精氨酸')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    zohe = models.CharField(max_length=30, blank=True, null=True, db_column='总和', verbose_name='总和')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    yiliansu = models.CharField(max_length=30, blank=True, null=True, db_column='异亮氨酸', verbose_name='异亮氨酸')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    seansu = models.CharField(max_length=30, blank=True, null=True, db_column='色氨酸', verbose_name='色氨酸')
    zhfa = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪', verbose_name='脂肪')
    zuansu = models.CharField(max_length=30, blank=True, null=True, db_column='组氨酸', verbose_name='组氨酸')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bebiansu = models.CharField(max_length=30, blank=True, null=True, db_column='苯丙氨酸', verbose_name='苯丙氨酸')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    yueguang = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    dabazh = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    liansu = models.CharField(max_length=30, blank=True, null=True, db_column='亮氨酸', verbose_name='亮氨酸')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    gaansu = models.CharField(max_length=30, blank=True, null=True, db_column='甘氨酸', verbose_name='甘氨酸')
    dajilish = models.CharField(max_length=30, blank=True, null=True, db_column='单荚粒数', verbose_name='单荚粒数')
    xiansu = models.CharField(max_length=30, blank=True, null=True, db_column='缬氨酸', verbose_name='缬氨酸')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    miansu = models.CharField(max_length=30, blank=True, null=True, db_column='酩氨酸', verbose_name='酩氨酸')
    fuansu = models.CharField(max_length=30, blank=True, null=True, db_column='脯氨酸', verbose_name='脯氨酸')
    naias = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_小扁豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class xiaodou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    sang = models.CharField(max_length=30, blank=True, null=True, db_column='谷氨酸', verbose_name='谷氨酸')
    xuyudawe = models.CharField(max_length=30, blank=True, null=True, db_column='选育单位', verbose_name='选育单位')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    xiansu = models.CharField(max_length=30, blank=True, null=True, db_column='缬氨酸', verbose_name='缬氨酸')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    jiansu = models.CharField(max_length=30, blank=True, null=True, db_column='精氨酸', verbose_name='精氨酸')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    zohe = models.CharField(max_length=30, blank=True, null=True, db_column='总和', verbose_name='总和')
    miqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='苗期耐盐', verbose_name='苗期耐盐')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    yiliansu = models.CharField(max_length=30, blank=True, null=True, db_column='异亮氨酸', verbose_name='异亮氨酸')
    xibipubilv = models.CharField(max_length=30, blank=True, null=True, db_column='锈病普遍率', verbose_name='锈病普遍率')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    zhfa = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪', verbose_name='脂肪')
    zuansu = models.CharField(max_length=30, blank=True, null=True, db_column='组氨酸', verbose_name='组氨酸')
    yaqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='芽期抗寒', verbose_name='芽期抗寒')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    qu = models.CharField(max_length=30, blank=True, null=True, db_column='区', verbose_name='区')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    yebabiji = models.CharField(max_length=30, blank=True, null=True, db_column='叶斑病级', verbose_name='叶斑病级')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    doji = models.CharField(max_length=30, blank=True, null=True, db_column='东经', verbose_name='东经')
    seansu = models.CharField(max_length=30, blank=True, null=True, db_column='色氨酸', verbose_name='色氨酸')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yqkh = models.CharField(max_length=30, blank=True, null=True, db_column='芽期抗旱', verbose_name='芽期抗旱')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    bebiansu = models.CharField(max_length=30, blank=True, null=True, db_column='苯丙氨酸', verbose_name='苯丙氨酸')
    shqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='熟期抗旱', verbose_name='熟期抗旱')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    dabazh = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    bewe = models.CharField(max_length=30, blank=True, null=True, db_column='北纬', verbose_name='北纬')
    liansu = models.CharField(max_length=30, blank=True, null=True, db_column='亮氨酸', verbose_name='亮氨酸')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    xibikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='锈病抗性', verbose_name='锈病抗性')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yahazhsh = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害指数', verbose_name='蚜害指数')
    gaansu = models.CharField(max_length=30, blank=True, null=True, db_column='甘氨酸', verbose_name='甘氨酸')
    dajilish = models.CharField(max_length=30, blank=True, null=True, db_column='单荚粒数', verbose_name='单荚粒数')
    yahabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病评价', verbose_name='蚜害病评价')
    yueguang = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    yaqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='芽期耐盐', verbose_name='芽期耐盐')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    xibiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='锈病严重度', verbose_name='锈病严重度')
    yuchnife = models.CharField(max_length=30, blank=True, null=True, db_column='育成年份', verbose_name='育成年份')
    miansu = models.CharField(max_length=30, blank=True, null=True, db_column='酩氨酸', verbose_name='酩氨酸')
    fuansu = models.CharField(max_length=30, blank=True, null=True, db_column='脯氨酸', verbose_name='脯氨酸')
    yebabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='叶斑病指数', verbose_name='叶斑病指数')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    naias = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    yahabijibi = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病级别', verbose_name='蚜害病级别')
    huqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='花期抗寒', verbose_name='花期抗寒')
    gach = models.CharField(max_length=30, blank=True, null=True, db_column='高程', verbose_name='高程')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    yahabizh = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害比值', verbose_name='蚜害比值')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    yebabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='叶斑病评价', verbose_name='叶斑病评价')
    xibizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='锈病指数', verbose_name='锈病指数')
    zhjijish = models.CharField(max_length=30, blank=True, null=True, db_column='主茎节数', verbose_name='主茎节数')
    las = models.CharField(max_length=30, blank=True, null=True, db_column='酪氨酸', verbose_name='酪氨酸')
    kahajibi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱级别', verbose_name='抗旱级别')
    balilv = models.CharField(max_length=30, blank=True, null=True, db_column='爆裂率', verbose_name='爆裂率')
    guxiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='谷锈严重度', verbose_name='谷锈严重度')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    dawebiha = models.CharField(max_length=20, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    bafabibilv = models.CharField(max_length=20, blank=True, null=True, db_column='白发病病率', verbose_name='白发病病率')
    v = models.CharField(db_column='VE', max_length=30, blank=True, null=True, verbose_name='VE')
    mise = models.CharField(max_length=30, blank=True, null=True, db_column='米色', verbose_name='米色')
    vb = models.CharField(db_column='VB2', max_length=30, blank=True, null=True, verbose_name='VB2')
    bafabikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='白发病抗性', verbose_name='白发病抗性')
    xichbizh = models.CharField(max_length=30, blank=True, null=True, db_column='线虫病指', verbose_name='线虫病指')
    zhfasu18 = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪酸183', verbose_name='脂肪酸183')
    chsurish = models.CharField(max_length=30, blank=True, null=True, db_column='抽穗日数', verbose_name='抽穗日数')
    yizhjish = models.CharField(max_length=30, blank=True, null=True, db_column='一株茎数', verbose_name='一株茎数')
    sumayipiji = models.CharField(max_length=30, blank=True, null=True, db_column='粟芒蝇评价', verbose_name='粟芒蝇评价')
    zhjichdu = models.CharField(max_length=30, blank=True, null=True, db_column='主茎长度', verbose_name='主茎长度')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    kahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱性', verbose_name='抗旱性')
    zhjizhji = models.CharField(max_length=30, blank=True, null=True, db_column='主茎直径', verbose_name='主茎直径')
    xi = models.CharField(max_length=30, blank=True, null=True, db_column='硒', verbose_name='硒')
    yibehazhlv = models.CharField(max_length=30, blank=True, null=True, db_column='蝇被害株率', verbose_name='蝇被害株率')
    yikaxijibi = models.CharField(max_length=30, blank=True, null=True, db_column='蝇抗性级别', verbose_name='蝇抗性级别')
    dazhlizh = models.CharField(max_length=30, blank=True, null=True, db_column='单株粒重', verbose_name='单株粒重')
    zhfasu16 = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪酸160', verbose_name='脂肪酸160')
    jinuxi = models.CharField(max_length=30, blank=True, null=True, db_column='粳糯性', verbose_name='粳糯性')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_小豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class xiaomai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    chmebibizh = models.CharField(max_length=50, blank=True, null=True, db_column='赤霉病病指', verbose_name='赤霉病病指')
    sulish = models.CharField(max_length=40, blank=True, null=True, db_column='穗粒数', verbose_name='穗粒数')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    dochxi = models.CharField(max_length=30, blank=True, null=True, db_column='冬春性', verbose_name='冬春性')
    chdizh = models.CharField(max_length=30, blank=True, null=True, db_column='沉淀值', verbose_name='沉淀值')
    layugu = models.CharField(max_length=30, blank=True, null=True, db_column='来源国', verbose_name='来源国')
    tijikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='田间抗寒性', verbose_name='田间抗寒性')
    miqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='苗期耐盐', verbose_name='苗期耐盐')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    sh = models.CharField(max_length=40, blank=True, null=True, db_column='省', verbose_name='省')
    yexifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='叶锈反应型', verbose_name='叶锈反应型')
    kese = models.CharField(max_length=50, blank=True, null=True, db_column='壳色', verbose_name='壳色')
    yexiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='叶锈严重度', verbose_name='叶锈严重度')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    gaxipubilv = models.CharField(max_length=40, blank=True, null=True, db_column='秆锈普遍率', verbose_name='秆锈普遍率')
    doji = models.CharField(max_length=40, blank=True, null=True, db_column='东经', verbose_name='东经')
    gaxifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈反应型', verbose_name='秆锈反应型')
    gaxiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈严重度', verbose_name='秆锈严重度')
    qita = models.CharField(max_length=30, blank=True, null=True, db_column='其它', verbose_name='其它')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    gefusubiji = models.CharField(max_length=30, blank=True, null=True, db_column='根腐穗病级', verbose_name='根腐穗病级')
    huaibi = models.CharField(max_length=30, blank=True, null=True, db_column='黄矮病', verbose_name='黄矮病')
    regokahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='人工抗寒性', verbose_name='人工抗寒性')
    tixifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='条锈反应型', verbose_name='条锈反应型')
    bafefayixi = models.CharField(max_length=30, blank=True, null=True, db_column='白粉反应型', verbose_name='白粉反应型')
    kahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱性', verbose_name='抗旱性')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    cudaba = models.CharField(max_length=40, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    bewe = models.CharField(max_length=40, blank=True, null=True, db_column='北纬', verbose_name='北纬')
    yuchnixi = models.CharField(max_length=30, blank=True, null=True, db_column='育成年限', verbose_name='育成年限')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='容重', verbose_name='容重')
    chmebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病抗性', verbose_name='赤霉病抗性')
    suzh = models.CharField(max_length=50, blank=True, null=True, db_column='穗长', verbose_name='穗长')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    yaqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='芽期耐盐', verbose_name='芽期耐盐')
    tixiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='条锈严重度', verbose_name='条锈严重度')
    ma = models.CharField(max_length=40, blank=True, null=True, db_column='芒', verbose_name='芒')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    yexipubilv = models.CharField(max_length=50, blank=True, null=True, db_column='叶锈普遍率', verbose_name='叶锈普遍率')
    xipu = models.CharField(max_length=70, blank=True, null=True, db_column='系谱', verbose_name='系谱')
    yidu = models.CharField(max_length=30, blank=True, null=True, db_column='硬度', verbose_name='硬度')
    chmebizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病指数', verbose_name='赤霉病指数')
    naias = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    qilizh = models.CharField(max_length=40, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    gefuyebiji = models.CharField(max_length=30, blank=True, null=True, db_column='根腐叶病级', verbose_name='根腐叶病级')
    gach = models.CharField(max_length=40, blank=True, null=True, db_column='高程', verbose_name='高程')
    yimi = models.CharField(max_length=40, blank=True, null=True, db_column='译名', verbose_name='译名')
    chmebibisu = models.CharField(max_length=50, blank=True, null=True, db_column='赤霉病病穗', verbose_name='赤霉病病穗')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    bafeyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='白粉严重度', verbose_name='白粉严重度')
    tixipubilv = models.CharField(max_length=30, blank=True, null=True, db_column='条锈普遍率', verbose_name='条锈普遍率')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    mazh = models.CharField(max_length=30, blank=True, null=True, db_column='芒长', verbose_name='芒长')
    chsurish = models.CharField(max_length=30, blank=True, null=True, db_column='抽穗日数', verbose_name='抽穗日数')
    yikebapidu = models.CharField(max_length=30, blank=True, null=True, db_column='颖壳包皮度', verbose_name='颖壳包皮度')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    guxiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='谷锈严重度', verbose_name='谷锈严重度')
    yahabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病指数', verbose_name='蚜害病指数')
    tahuli = models.CharField(max_length=30, blank=True, null=True, db_column='糖化力', verbose_name='糖化力')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    sx = models.CharField(max_length=30, blank=True, null=True, db_column='穗形', verbose_name='穗形')
    sumidu = models.CharField(max_length=30, blank=True, null=True, db_column='穗密度', verbose_name='穗密度')
    mixi = models.CharField(max_length=30, blank=True, null=True, db_column='米香', verbose_name='米香')
    jinuxi = models.CharField(max_length=30, blank=True, null=True, db_column='粳糯性', verbose_name='粳糯性')
    subizh = models.CharField(max_length=30, blank=True, null=True, db_column='穗柄长', verbose_name='穗柄长')
    shyurish = models.CharField(max_length=30, blank=True, null=True, db_column='生育日数', verbose_name='生育日数')
    kahajibi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱级别', verbose_name='抗旱级别')
    babefesh = models.CharField(max_length=30, blank=True, null=True, db_column='白背飞虱', verbose_name='白背飞虱')
    v = models.CharField(db_column='VE', max_length=30, blank=True, null=True, verbose_name='VE')
    laanzhdaba = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨占蛋白', verbose_name='赖氨占蛋白')
    ti = models.CharField(max_length=30, blank=True, null=True, db_column='田', verbose_name='田')
    huaiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='黄矮严重度', verbose_name='黄矮严重度')
    yimayowu = models.CharField(max_length=30, blank=True, null=True, db_column='颖毛有无', verbose_name='颖毛有无')
    zhfasu16 = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪酸160', verbose_name='脂肪酸160')
    jizhlv = models.CharField(max_length=30, blank=True, null=True, db_column='角质率', verbose_name='角质率')
    yizhsu = models.CharField(max_length=30, blank=True, null=True, db_column='硬脂酸', verbose_name='硬脂酸')
    chmebisulv = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病穗率', verbose_name='赤霉病穗率')
    zazhwa = models.CharField(max_length=30, blank=True, null=True, db_column='早中晚', verbose_name='早中晚')
    vb = models.CharField(db_column='VB2', max_length=30, blank=True, null=True, verbose_name='VB2')
    yubiha = models.CharField(max_length=30, blank=True, null=True, db_column='原编号', verbose_name='原编号')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    tiwebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='条纹病抗性', verbose_name='条纹病抗性')
    xiji = models.CharField(max_length=30, blank=True, null=True, db_column='籼粳', verbose_name='籼粳')
    mise = models.CharField(max_length=30, blank=True, null=True, db_column='米色', verbose_name='米色')
    chdu = models.CharField(max_length=30, blank=True, null=True, db_column='锤度', verbose_name='锤度')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    fenili = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖力', verbose_name='分蘖力')
    miwe = models.CharField(max_length=30, blank=True, null=True, db_column='苗瘟', verbose_name='苗瘟')
    yomiqise = models.CharField(max_length=30, blank=True, null=True, db_column='幼苗鞘色', verbose_name='幼苗鞘色')
    layudi = models.CharField(max_length=256, blank=True, null=True, db_column='来源地', verbose_name='来源地')
    balilv = models.CharField(max_length=30, blank=True, null=True, db_column='爆裂率', verbose_name='爆裂率')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    chsuqi = models.CharField(max_length=30, blank=True, null=True, db_column='出穗期', verbose_name='出穗期')
    yizhjish = models.CharField(max_length=30, blank=True, null=True, db_column='一株茎数', verbose_name='一株茎数')
    gujikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='灌浆抗寒性', verbose_name='灌浆抗寒性')
    sihesubilv = models.CharField(max_length=30, blank=True, null=True, db_column='丝黑穗病率', verbose_name='丝黑穗病率')
    chbabiji = models.CharField(max_length=30, blank=True, null=True, db_column='赤斑病级', verbose_name='赤斑病级')
    maxi = models.CharField(max_length=30, blank=True, null=True, db_column='芒形', verbose_name='芒形')
    ebalv = models.CharField(max_length=30, blank=True, null=True, db_column='垩白率', verbose_name='垩白率')
    zhjijish = models.CharField(max_length=30, blank=True, null=True, db_column='主茎节数', verbose_name='主茎节数')
    jicu = models.CharField(max_length=30, blank=True, null=True, db_column='茎粗', verbose_name='茎粗')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒型', verbose_name='粒型')
    pilu = models.CharField(max_length=30, blank=True, null=True, db_column='皮裸', verbose_name='皮裸')
    yijise = models.CharField(max_length=30, blank=True, null=True, db_column='颖尖色', verbose_name='颖尖色')
    zhjichdu = models.CharField(max_length=30, blank=True, null=True, db_column='主茎长度', verbose_name='主茎长度')
    fenixi = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖性', verbose_name='分蘖性')
    hushxisu = models.CharField(max_length=30, blank=True, null=True, db_column='花生稀酸', verbose_name='花生稀酸')
    yahabiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病级', verbose_name='蚜害病级')
    nalajibi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝级别', verbose_name='耐涝级别')
    jimilv = models.CharField(max_length=30, blank=True, null=True, db_column='精米率', verbose_name='精米率')
    dazhgazh = models.CharField(max_length=30, blank=True, null=True, db_column='单株秆重', verbose_name='单株秆重')
    shfe = models.CharField(max_length=30, blank=True, null=True, db_column='水份', verbose_name='水份')
    zhjiyepish = models.CharField(max_length=30, blank=True, null=True, db_column='主茎叶片数', verbose_name='主茎叶片数')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='棱型', verbose_name='棱型')
    zhkubi = models.CharField(max_length=30, blank=True, null=True, db_column='长宽比', verbose_name='长宽比')
    zhjizhji = models.CharField(max_length=30, blank=True, null=True, db_column='主茎直径', verbose_name='主茎直径')
    zhkelv = models.CharField(max_length=30, blank=True, null=True, db_column='着壳率', verbose_name='着壳率')
    zolvsu = models.CharField(max_length=30, blank=True, null=True, db_column='棕榈酸', verbose_name='棕榈酸')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    bacudawe_2 = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位_2', verbose_name='保存单位_2')
    xi = models.CharField(max_length=30, blank=True, null=True, db_column='硒', verbose_name='硒')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    xisufezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='雄穗分枝数', verbose_name='雄穗分枝数')
    yahabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病评价', verbose_name='蚜害病评价')
    huhuyekaxi = models.CharField(max_length=30, blank=True, null=True, db_column='黄花叶抗性', verbose_name='黄花叶抗性')
    wekubi = models.CharField(max_length=30, blank=True, null=True, db_column='纹枯病', verbose_name='纹枯病')
    yibehazhlv = models.CharField(max_length=30, blank=True, null=True, db_column='蝇被害株率', verbose_name='蝇被害株率')
    shbiha = models.CharField(max_length=30, blank=True, null=True, db_column='省编号', verbose_name='省编号')
    cuzodife = models.CharField(max_length=30, blank=True, null=True, db_column='粗总淀粉', verbose_name='粗总淀粉')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    huhufabilv = models.CharField(max_length=30, blank=True, null=True, db_column='黄花发病率', verbose_name='黄花发病率')
    yijiwazh = models.CharField(max_length=30, blank=True, null=True, db_column='颖尖弯直', verbose_name='颖尖弯直')
    yikaxijibi = models.CharField(max_length=30, blank=True, null=True, db_column='蝇抗性级别', verbose_name='蝇抗性级别')
    yomise = models.CharField(max_length=30, blank=True, null=True, db_column='幼苗色', verbose_name='幼苗色')
    feyush = models.CharField(max_length=30, blank=True, null=True, db_column='α生育酚', verbose_name='α生育酚')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    qufejichwu = models.CharField(max_length=30, blank=True, null=True, db_column='全粉浸出物', verbose_name='全粉浸出物')
    fafajizuhe = models.CharField(max_length=30, blank=True, null=True, db_column='方法及组合', verbose_name='方法及组合')
    yibehazhsh = models.CharField(max_length=30, blank=True, null=True, db_column='蝇被害指数', verbose_name='蝇被害指数')
    dafuxi = models.CharField(max_length=30, blank=True, null=True, db_column='倒伏性', verbose_name='倒伏性')
    aihuyepiji = models.CharField(max_length=30, blank=True, null=True, db_column='矮花叶评价', verbose_name='矮花叶评价')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    huhuhuhudu = models.CharField(max_length=30, blank=True, null=True, db_column='黄花黄化度', verbose_name='黄花黄化度')
    shlu = models.CharField(max_length=30, blank=True, null=True, db_column='水陆', verbose_name='水陆')
    dazhlizh = models.CharField(max_length=30, blank=True, null=True, db_column='单株粒重', verbose_name='单株粒重')
    xs = models.CharField(max_length=30, blank=True, null=True, db_column='穗型', verbose_name='穗型')
    xibapiji = models.CharField(max_length=30, blank=True, null=True, db_column='小斑评价', verbose_name='小斑评价')
    chbabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='赤斑病评价', verbose_name='赤斑病评价')
    dadichshxi = models.CharField(max_length=30, blank=True, null=True, db_column='当地成熟型', verbose_name='当地成熟型')
    camilv = models.CharField(max_length=30, blank=True, null=True, db_column='糙米率', verbose_name='糙米率')
    zhfasu20 = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪酸200', verbose_name='脂肪酸200')
    yirushji = models.CharField(max_length=30, blank=True, null=True, db_column='引入时间', verbose_name='引入时间')
    hefebi = models.CharField(max_length=30, blank=True, null=True, db_column='黑粉病', verbose_name='黑粉病')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    xuyudawe = models.CharField(max_length=30, blank=True, null=True, db_column='选育单位', verbose_name='选育单位')
    jichdu = models.CharField(max_length=30, blank=True, null=True, db_column='胶稠度', verbose_name='胶稠度')
    laanzhyapi = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨占样品', verbose_name='赖氨占样品')
    dani = models.CharField(max_length=30, blank=True, null=True, db_column='单宁', verbose_name='单宁')
    yosu = models.CharField(max_length=30, blank=True, null=True, db_column='油酸', verbose_name='油酸')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_小麦'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class xiaomaixiyouzhong(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    shmi = models.CharField(max_length=40, blank=True, null=True, db_column='属名', verbose_name='属名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    ke = models.CharField(max_length=30, blank=True, null=True, db_column='壳', verbose_name='壳')
    gefusubiji = models.CharField(max_length=30, blank=True, null=True, db_column='根腐穗病级', verbose_name='根腐穗病级')
    yirushji = models.CharField(max_length=30, blank=True, null=True, db_column='引入时间', verbose_name='引入时间')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    suzh = models.CharField(max_length=30, blank=True, null=True, db_column='穗长', verbose_name='穗长')
    chmebizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病指数', verbose_name='赤霉病指数')
    tixifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='条锈反应型', verbose_name='条锈反应型')
    chmebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病抗性', verbose_name='赤霉病抗性')
    chsuqi = models.CharField(max_length=30, blank=True, null=True, db_column='抽穗期', verbose_name='抽穗期')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    tijikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='田间抗寒性', verbose_name='田间抗寒性')
    xipu = models.CharField(max_length=40, blank=True, null=True, db_column='系谱', verbose_name='系谱')
    bafefayixi = models.CharField(max_length=30, blank=True, null=True, db_column='白粉反应型', verbose_name='白粉反应型')
    kahuqi = models.CharField(max_length=30, db_column='开花期', verbose_name='开花期')
    gaxipubilv = models.CharField(max_length=30, db_column='秆锈普遍率', verbose_name='秆锈普遍率')
    naias = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    chmebibizh = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病病指', verbose_name='赤霉病病指')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    yexipubilv = models.CharField(max_length=30, blank=True, null=True, db_column='叶锈普遍率', verbose_name='叶锈普遍率')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    sulish = models.CharField(max_length=30, blank=True, null=True, db_column='穗粒数', verbose_name='穗粒数')
    yubiha = models.CharField(max_length=30, blank=True, null=True, db_column='原编号', verbose_name='原编号')
    yexifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='叶锈反应型', verbose_name='叶锈反应型')
    bafeyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='白粉严重度', verbose_name='白粉严重度')
    tixipubilv = models.CharField(max_length=30, blank=True, null=True, db_column='条锈普遍率', verbose_name='条锈普遍率')
    huaibi = models.CharField(max_length=30, blank=True, null=True, db_column='黄矮病', verbose_name='黄矮病')
    pzname = models.CharField(max_length=70, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yexiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='叶锈严重度', verbose_name='叶锈严重度')
    ma = models.CharField(max_length=30, blank=True, null=True, db_column='芒', verbose_name='芒')
    chmebibisu = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病病穗', verbose_name='赤霉病病穗')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    gaxifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈反应型', verbose_name='秆锈反应型')
    kahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱性', verbose_name='抗旱性')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    xumi = models.CharField(max_length=60, blank=True, null=True, db_column='学名', verbose_name='学名')
    gaxiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈严重度', verbose_name='秆锈严重度')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    regokahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='人工抗寒性', verbose_name='人工抗寒性')
    shzhdi = models.CharField(max_length=30, blank=True, null=True, db_column='收种地', verbose_name='收种地')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    chdizh = models.CharField(max_length=30, blank=True, null=True, db_column='沉淀值', verbose_name='沉淀值')
    dochxi = models.CharField(max_length=30, blank=True, null=True, db_column='冬春性', verbose_name='冬春性')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    li = models.CharField(max_length=30, blank=True, null=True, db_column='粒', verbose_name='粒')
    yidu = models.CharField(max_length=30, blank=True, null=True, db_column='硬度', verbose_name='硬度')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    tixiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='条锈严重度', verbose_name='条锈严重度')
    gefuyebiji = models.CharField(max_length=30, blank=True, null=True, db_column='根腐叶病级', verbose_name='根腐叶病级')
    rasetizu = models.CharField(max_length=30, blank=True, null=True, db_column='染色体组', verbose_name='染色体组')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_小麦稀有种'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class shanzha(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    shyuqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='生育期评价', verbose_name='生育期评价')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shgunili = models.CharField(max_length=30, blank=True, null=True, db_column='始果年龄', verbose_name='始果年龄')
    shyuqi = models.CharField(db_column='生育期D', max_length=30, blank=True, null=True, verbose_name='生育期D')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    nezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='内质评价', verbose_name='内质评价')
    zaguxipiji = models.CharField(max_length=30, blank=True, null=True, db_column='早果性评价', verbose_name='早果性评价')
    zota = models.CharField(db_column='总糖％', max_length=30, blank=True, null=True, verbose_name='总糖％')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    daguzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='单果重评价', verbose_name='单果重评价')
    gushchshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果实成熟期', verbose_name='果实成熟期')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    chshqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期评价', verbose_name='成熟期评价')
    zosu = models.CharField(db_column='总酸％', max_length=30, blank=True, null=True, verbose_name='总酸％')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzhg = models.CharField(db_column='单果重G', max_length=30, blank=True, null=True, verbose_name='单果重G')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    danihali = models.CharField(db_column='单宁含量％', max_length=30, blank=True, null=True, verbose_name='单宁含量％')
    rasetibesh = models.CharField(max_length=30, blank=True, null=True, db_column='染色体倍数', verbose_name='染色体倍数')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    keshlv = models.CharField(db_column='可食率％', max_length=30, blank=True, null=True, verbose_name='可食率％')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_山楂'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class biandou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    dajilish = models.CharField(max_length=30, blank=True, null=True, db_column='单荚粒数', verbose_name='单荚粒数')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    xumi = models.CharField(max_length=60, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_扁豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class putongcaidou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    jibabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='角斑病指数', verbose_name='角斑病指数')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    sang = models.CharField(max_length=30, blank=True, null=True, db_column='谷氨酸', verbose_name='谷氨酸')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    xiansu = models.CharField(max_length=30, blank=True, null=True, db_column='缬氨酸', verbose_name='缬氨酸')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    jiansu = models.CharField(max_length=30, blank=True, null=True, db_column='精氨酸', verbose_name='精氨酸')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    zohe = models.CharField(max_length=30, blank=True, null=True, db_column='总和', verbose_name='总和')
    yahabiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病级', verbose_name='蚜害病级')
    yiliansu = models.CharField(max_length=30, blank=True, null=True, db_column='异亮氨酸', verbose_name='异亮氨酸')
    tajubiji = models.CharField(max_length=30, blank=True, null=True, db_column='炭疽病级', verbose_name='炭疽病级')
    tajubizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='炭疽病指数', verbose_name='炭疽病指数')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    seansu = models.CharField(max_length=30, blank=True, null=True, db_column='色氨酸', verbose_name='色氨酸')
    zuansu = models.CharField(max_length=30, blank=True, null=True, db_column='组氨酸', verbose_name='组氨酸')
    yaqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='芽期抗寒', verbose_name='芽期抗寒')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    jibabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='角斑病评价', verbose_name='角斑病评价')
    doji = models.CharField(max_length=30, blank=True, null=True, db_column='东经', verbose_name='东经')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yajiankanghan = models.CharField(max_length=30, blank=True, null=True, db_column='芽期抗旱', verbose_name='芽期抗旱')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    yahabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病指数', verbose_name='蚜害病指数')
    bebiansu = models.CharField(max_length=30, blank=True, null=True, db_column='苯丙氨酸', verbose_name='苯丙氨酸')
    shqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='熟期抗旱', verbose_name='熟期抗旱')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    bewe = models.CharField(max_length=30, blank=True, null=True, db_column='北纬', verbose_name='北纬')
    liansu = models.CharField(max_length=30, blank=True, null=True, db_column='亮氨酸', verbose_name='亮氨酸')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    bezh = models.CharField(max_length=40, blank=True, null=True, db_column='备注', verbose_name='备注')
    gaansu = models.CharField(max_length=30, blank=True, null=True, db_column='甘氨酸', verbose_name='甘氨酸')
    dajilish = models.CharField(max_length=30, blank=True, null=True, db_column='单荚粒数', verbose_name='单荚粒数')
    yahabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病评价', verbose_name='蚜害病评价')
    yueguang = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    miansu = models.CharField(max_length=30, blank=True, null=True, db_column='酩氨酸', verbose_name='酩氨酸')
    fuansu = models.CharField(max_length=30, blank=True, null=True, db_column='脯氨酸', verbose_name='脯氨酸')
    naias = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    jibabiji = models.CharField(max_length=30, blank=True, null=True, db_column='角斑病级', verbose_name='角斑病级')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    gach = models.CharField(max_length=30, blank=True, null=True, db_column='高程', verbose_name='高程')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    tajubipiji = models.CharField(max_length=30, blank=True, null=True, db_column='炭疽病评价', verbose_name='炭疽病评价')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_普通菜豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class mushu(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kahaxipiji = models.CharField(max_length=30, blank=True, null=True, db_column='抗寒性评价', verbose_name='抗寒性评价')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    wezhkayese = models.CharField(max_length=30, blank=True, null=True, db_column='未展开叶色', verbose_name='未展开叶色')
    yebiyase = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄颜色', verbose_name='叶柄颜色')
    gawulv = models.CharField(max_length=30, blank=True, null=True, db_column='干物率', verbose_name='干物率')
    piji = models.CharField(db_column='评价D', max_length=30, blank=True, null=True, verbose_name='评价D')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    pijia = models.CharField(db_column='评价A', max_length=30, blank=True, null=True, verbose_name='评价A')
    kafepiji = models.CharField(max_length=30, blank=True, null=True, db_column='抗风评价', verbose_name='抗风评价')
    pijih = models.CharField(db_column='评价H', max_length=30, blank=True, null=True, verbose_name='评价H')
    lajiwapise = models.CharField(max_length=30, blank=True, null=True, db_column='老茎外皮色', verbose_name='老茎外皮色')
    qihelipiji = models.CharField(max_length=30, blank=True, null=True, db_column='亲和力评价', verbose_name='亲和力评价')
    yemayase = models.CharField(max_length=30, blank=True, null=True, db_column='叶脉颜色', verbose_name='叶脉颜色')
    xiwesuhali = models.CharField(max_length=30, blank=True, null=True, db_column='纤维素含量', verbose_name='纤维素含量')
    pijic = models.CharField(db_column='评价C', max_length=30, blank=True, null=True, verbose_name='评价C')
    zhzhmich = models.CharField(max_length=30, blank=True, null=True, db_column='种质名称', verbose_name='种质名称')
    teyixiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异性用途', verbose_name='特异性用途')
    fubeqiheli = models.CharField(max_length=30, blank=True, null=True, db_column='父本亲和力', verbose_name='父本亲和力')
    difehali = models.CharField(max_length=30, blank=True, null=True, db_column='淀粉含量', verbose_name='淀粉含量')
    kafedeji = models.CharField(max_length=30, blank=True, null=True, db_column='抗风等级', verbose_name='抗风等级')
    weshchali = models.CharField(db_column='维生C含量', max_length=30, blank=True, null=True, verbose_name='维生C含量')
    epinjia = models.CharField(db_column='评价E', max_length=30, blank=True, null=True, verbose_name='评价E')
    zhzhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='种质来源', verbose_name='种质来源')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    lajinepise = models.CharField(max_length=30, blank=True, null=True, db_column='老茎内皮色', verbose_name='老茎内皮色')
    fpinjia = models.CharField(db_column='评价F', max_length=30, blank=True, null=True, verbose_name='评价F')
    muchli = models.CharField(max_length=30, blank=True, null=True, db_column='亩产量', verbose_name='亩产量')
    mubeqiheli = models.CharField(max_length=30, blank=True, null=True, db_column='母本亲和力', verbose_name='母本亲和力')
    kugewapise = models.CharField(max_length=30, blank=True, null=True, db_column='块根外皮色', verbose_name='块根外皮色')
    qisuhali = models.CharField(max_length=30, blank=True, null=True, db_column='氰酸含量', verbose_name='氰酸含量')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    kugenepise = models.CharField(max_length=30, blank=True, null=True, db_column='块根内皮色', verbose_name='块根内皮色')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    pijib = models.CharField(db_column='评价B', max_length=30, blank=True, null=True, verbose_name='评价B')
    pijig = models.CharField(db_column='评价G', max_length=30, blank=True, null=True, verbose_name='评价G')
    kahadeji = models.CharField(max_length=30, blank=True, null=True, db_column='抗寒等级', verbose_name='抗寒等级')
    zhjilipixi = models.CharField(max_length=30, blank=True, null=True, db_column='中间裂片形', verbose_name='中间裂片形')
    kugexizh = models.CharField(max_length=30, blank=True, null=True, db_column='块根形状', verbose_name='块根形状')
    zhzhxita = models.CharField(max_length=30, blank=True, null=True, db_column='植株形态', verbose_name='植株形态')
    dabazhhali = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质含量', verbose_name='蛋白质含量')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_木薯'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class mudou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    dajilish = models.CharField(max_length=30, blank=True, null=True, db_column='单荚粒数', verbose_name='单荚粒数')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_木豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class Xiaolizi(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    keroguxiwu = models.CharField(max_length=30, blank=True, null=True, db_column='可溶固形物', verbose_name='可溶固形物')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    zhye = models.CharField(max_length=30, blank=True, null=True, db_column='汁液', verbose_name='汁液')
    nezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='内质评价', verbose_name='内质评价')
    zota = models.CharField(db_column='总糖％', max_length=30, blank=True, null=True, verbose_name='总糖％')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    daguzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='单果重评价', verbose_name='单果重评价')
    rose = models.CharField(max_length=30, blank=True, null=True, db_column='肉色', verbose_name='肉色')
    gushchshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果实成熟期', verbose_name='果实成熟期')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    daguzhg = models.CharField(db_column='单果重G', max_length=30, blank=True, null=True, verbose_name='单果重G')
    chshqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期评价', verbose_name='成熟期评价')
    zosu = models.CharField(db_column='总酸％', max_length=30, blank=True, null=True, verbose_name='总酸％')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    hezhlixi = models.CharField(max_length=30, blank=True, null=True, db_column='核粘离性', verbose_name='核粘离性')
    fayuqi = models.CharField(db_column='发育期D', max_length=30, blank=True, null=True, verbose_name='发育期D')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_李子'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class xing(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    keroguxiwu = models.CharField(max_length=30, blank=True, null=True, db_column='可溶固形物', verbose_name='可溶固形物')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    guretiku = models.CharField(max_length=30, blank=True, null=True, db_column='果仁甜苦', verbose_name='果仁甜苦')
    nezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='内质评价', verbose_name='内质评价')
    zota = models.CharField(db_column='总糖％', max_length=30, blank=True, null=True, verbose_name='总糖％')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    daguzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='单果重评价', verbose_name='单果重评价')
    rose = models.CharField(max_length=30, blank=True, null=True, db_column='肉色', verbose_name='肉色')
    gushchshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果实成熟期', verbose_name='果实成熟期')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    daguzhg = models.CharField(db_column='单果重G', max_length=30, blank=True, null=True, verbose_name='单果重G')
    chshqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期评价', verbose_name='成熟期评价')
    zosu = models.CharField(db_column='总酸％', max_length=30, blank=True, null=True, verbose_name='总酸％')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    hezhlixi = models.CharField(max_length=30, blank=True, null=True, db_column='核粘离性', verbose_name='核粘离性')
    guredaxig = models.CharField(db_column='果仁大小G', max_length=30, blank=True, null=True, verbose_name='果仁大小G')
    fayuqi = models.CharField(db_column='发育期D', max_length=30, blank=True, null=True, verbose_name='发育期D')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_杏'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class pipa(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    xizh = models.CharField(max_length=30, blank=True, null=True, db_column='形状', verbose_name='形状')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    zhhuta = models.CharField(db_column='转化糖％', max_length=30, blank=True, null=True, verbose_name='转化糖％')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    zhye = models.CharField(max_length=30, blank=True, null=True, db_column='汁液', verbose_name='汁液')
    xiqi = models.CharField(max_length=30, blank=True, null=True, db_column='香气', verbose_name='香气')
    hasuli = models.CharField(db_column='含酸量％', max_length=30, blank=True, null=True, verbose_name='含酸量％')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    daguzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='单果重评价', verbose_name='单果重评价')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    chshqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期评价', verbose_name='成熟期评价')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzhg = models.CharField(db_column='单果重G', max_length=30, blank=True, null=True, verbose_name='单果重G')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    zhqidu = models.CharField(max_length=30, blank=True, null=True, db_column='整齐度', verbose_name='整齐度')
    nezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='内质评价', verbose_name='内质评价')
    keshlv = models.CharField(db_column='可食率％', max_length=30, blank=True, null=True, verbose_name='可食率％')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_枇杷'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class zao(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    shyuqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='生育期评价', verbose_name='生育期评价')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shgunili = models.CharField(max_length=30, blank=True, null=True, db_column='始果年龄', verbose_name='始果年龄')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    zhye = models.CharField(max_length=30, blank=True, null=True, db_column='汁液', verbose_name='汁液')
    xizakeshlv = models.CharField(max_length=30, blank=True, null=True, db_column='鲜枣可食率', verbose_name='鲜枣可食率')
    nezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='内质评价', verbose_name='内质评价')
    zaguxipiji = models.CharField(max_length=30, blank=True, null=True, db_column='早果性评价', verbose_name='早果性评价')
    hasuli = models.CharField(db_column='含酸量％', max_length=30, blank=True, null=True, verbose_name='含酸量％')
    zota = models.CharField(db_column='总糖％', max_length=30, blank=True, null=True, verbose_name='总糖％')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    gushchshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果实成熟期', verbose_name='果实成熟期')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    daguzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='单果重评价', verbose_name='单果重评价')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    chshqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期评价', verbose_name='成熟期评价')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzhg = models.CharField(db_column='单果重G', max_length=30, blank=True, null=True, verbose_name='单果重G')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    shyuqi = models.CharField(db_column='生育期D', max_length=30, blank=True, null=True, verbose_name='生育期D')
    zhqidu = models.CharField(max_length=30, blank=True, null=True, db_column='整齐度', verbose_name='整齐度')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_枣'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class gouqi(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shpizh = models.CharField(max_length=30, blank=True, null=True, db_column='商品重', verbose_name='商品重')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    xizhtezh = models.CharField(max_length=30, blank=True, null=True, db_column='形状特征', verbose_name='形状特征')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_枸杞'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class ganju(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    keroguxiwu = models.CharField(max_length=30, blank=True, null=True, db_column='可溶固形物', verbose_name='可溶固形物')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    keshlv = models.CharField(max_length=30, blank=True, null=True, db_column='可食率', verbose_name='可食率')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    nezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='内质评价', verbose_name='内质评价')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    zhzish = models.CharField(max_length=30, blank=True, null=True, db_column='种子数', verbose_name='种子数')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    nimesu = models.CharField(max_length=30, blank=True, null=True, db_column='柠檬酸', verbose_name='柠檬酸')
    daguzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='单果重评价', verbose_name='单果重评价')
    gushchshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果实成熟期', verbose_name='果实成熟期')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    chshqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期评价', verbose_name='成熟期评价')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=40, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzhg = models.CharField(db_column='单果重G', max_length=30, blank=True, null=True, verbose_name='单果重G')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    cuxi = models.CharField(max_length=30, blank=True, null=True, db_column='粗细', verbose_name='粗细')
    zota = models.CharField(max_length=30, blank=True, null=True, db_column='总糖', verbose_name='总糖')
    guzh = models.CharField(max_length=30, blank=True, null=True, db_column='果汁', verbose_name='果汁')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_柑桔'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class shi(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    cashqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='采收期评价', verbose_name='采收期评价')
    shyuqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='生育期评价', verbose_name='生育期评价')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    zhye = models.CharField(max_length=30, blank=True, null=True, db_column='汁液', verbose_name='汁液')
    dani = models.CharField(max_length=30, blank=True, null=True, db_column='单宁', verbose_name='单宁')
    nezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='内质评价', verbose_name='内质评价')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    tuseshjih = models.CharField(db_column='脱涩时间H', max_length=30, blank=True, null=True, verbose_name='脱涩时间H')
    cashqi = models.CharField(db_column='采收期D', max_length=30, blank=True, null=True, verbose_name='采收期D')
    gushchshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果实成熟期', verbose_name='果实成熟期')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    keroguxiwu = models.CharField(max_length=30, blank=True, null=True, db_column='可溶固形物', verbose_name='可溶固形物')
    daguzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='单果重评价', verbose_name='单果重评价')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    daguzhg = models.CharField(db_column='单果重G', max_length=30, blank=True, null=True, verbose_name='单果重G')
    chshqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期评价', verbose_name='成熟期评价')
    keroxita = models.CharField(max_length=30, blank=True, null=True, db_column='可溶性糖', verbose_name='可溶性糖')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    kedidisu = models.CharField(max_length=30, blank=True, null=True, db_column='可滴定酸', verbose_name='可滴定酸')
    shyuqi = models.CharField(db_column='生育期D', max_length=30, blank=True, null=True, verbose_name='生育期D')
    zhqidu = models.CharField(max_length=30, blank=True, null=True, db_column='整齐度', verbose_name='整齐度')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_柿'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class LiZi(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    jinu = models.CharField(max_length=30, blank=True, null=True, db_column='粳糯', verbose_name='粳糯')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    shfe = models.CharField(db_column='水分％', max_length=30, blank=True, null=True, verbose_name='水分％')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    dizu = models.CharField(max_length=30, blank=True, null=True, db_column='底坐', verbose_name='底坐')
    nezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='内质评价', verbose_name='内质评价')
    tidu = models.CharField(max_length=30, blank=True, null=True, db_column='甜度', verbose_name='甜度')
    xiwe = models.CharField(max_length=30, blank=True, null=True, db_column='香味', verbose_name='香味')
    gushchshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果实成熟期', verbose_name='果实成熟期')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    cihuqi = models.CharField(max_length=30, blank=True, null=True, db_column='雌花期', verbose_name='雌花期')
    daguzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='单果重评价', verbose_name='单果重评价')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    dife = models.CharField(db_column='淀粉％', max_length=30, blank=True, null=True, verbose_name='淀粉％')
    ta = models.CharField(db_column='糖％', max_length=30, blank=True, null=True, verbose_name='糖％')
    daguzhg = models.CharField(db_column='单果重G', max_length=30, blank=True, null=True, verbose_name='单果重G')
    chshqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期评价', verbose_name='成熟期评价')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    xihuqi = models.CharField(max_length=30, blank=True, null=True, db_column='雄花期', verbose_name='雄花期')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    gudi = models.CharField(max_length=30, blank=True, null=True, db_column='果顶', verbose_name='果顶')
    zhqidu = models.CharField(max_length=30, blank=True, null=True, db_column='整齐度', verbose_name='整齐度')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_栗'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class hetao(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    rezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='仁质评价', verbose_name='仁质评价')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    chrelv = models.CharField(db_column='出仁率％', max_length=30, blank=True, null=True, verbose_name='出仁率％')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    guhudu = models.CharField(max_length=30, blank=True, null=True, db_column='光滑度', verbose_name='光滑度')
    chrelvpiji = models.CharField(max_length=30, blank=True, null=True, db_column='出仁率评价', verbose_name='出仁率评价')
    gushchshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果实成熟期', verbose_name='果实成熟期')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    cihuqi = models.CharField(max_length=30, blank=True, null=True, db_column='雌花期', verbose_name='雌花期')
    daguzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='单果重评价', verbose_name='单果重评价')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    daguzhg = models.CharField(db_column='单果重G', max_length=30, blank=True, null=True, verbose_name='单果重G')
    chshqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期评价', verbose_name='成熟期评价')
    li = models.CharField(db_column='磷％', max_length=30, blank=True, null=True, verbose_name='磷％')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    xihuqi = models.CharField(max_length=30, blank=True, null=True, db_column='雄花期', verbose_name='雄花期')
    zhfa = models.CharField(db_column='脂肪％', max_length=30, blank=True, null=True, verbose_name='脂肪％')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    dabazh = models.CharField(db_column='蛋白质％', max_length=30, blank=True, null=True, verbose_name='蛋白质％')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_核桃'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class gentiancai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    rozhgexi = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根形', verbose_name='肉质根形')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    geroshfe = models.CharField(max_length=30, blank=True, null=True, db_column='根肉水分', verbose_name='根肉水分')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='收获期', verbose_name='收获期')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    rozhgezh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根长', verbose_name='肉质根长')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    gerokoga = models.CharField(max_length=30, blank=True, null=True, db_column='根肉口感', verbose_name='根肉口感')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    shzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='生长期', verbose_name='生长期')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    yecu = models.CharField(max_length=30, blank=True, null=True, db_column='叶簇', verbose_name='叶簇')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    rozhgecu = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根粗', verbose_name='肉质根粗')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    gerozh = models.CharField(max_length=30, blank=True, null=True, db_column='根肉质', verbose_name='根肉质')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    yepizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶片长', verbose_name='叶片长')
    naihanxing = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    yepiku = models.CharField(max_length=30, blank=True, null=True, db_column='叶片宽', verbose_name='叶片宽')
    gepise = models.CharField(max_length=30, blank=True, null=True, db_column='根皮色', verbose_name='根皮色')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    dagezh = models.CharField(max_length=30, blank=True, null=True, db_column='单根重', verbose_name='单根重')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')
    gerose = models.CharField(max_length=30, blank=True, null=True, db_column='根肉色', verbose_name='根肉色')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_根甜菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class gengaicai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    rozhgexi = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根形', verbose_name='肉质根形')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    xilipidush = models.CharField(max_length=30, blank=True, null=True, db_column='小裂片对数', verbose_name='小裂片对数')
    yemilafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶面蜡粉', verbose_name='叶面蜡粉')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yelike = models.CharField(max_length=30, blank=True, null=True, db_column='叶裂刻', verbose_name='叶裂刻')
    dizhqi = models.CharField(max_length=30, blank=True, null=True, db_column='定植期', verbose_name='定植期')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    rozhgezh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根长', verbose_name='肉质根长')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    jilawe = models.CharField(max_length=30, blank=True, null=True, db_column='芥辣味', verbose_name='芥辣味')
    geroshfe = models.CharField(max_length=30, blank=True, null=True, db_column='根肉水分', verbose_name='根肉水分')
    xumi = models.CharField(max_length=60, blank=True, null=True, db_column='学名', verbose_name='学名')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    shzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='生长期', verbose_name='生长期')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    rozhgecu = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根粗', verbose_name='肉质根粗')
    yemicima = models.CharField(max_length=30, blank=True, null=True, db_column='叶面刺毛', verbose_name='叶面刺毛')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    gerozh = models.CharField(max_length=30, blank=True, null=True, db_column='根肉质', verbose_name='根肉质')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='收获期', verbose_name='收获期')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    yeyi = models.CharField(max_length=30, blank=True, null=True, db_column='叶翼', verbose_name='叶翼')
    naihanxing = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    dagezh = models.CharField(max_length=30, blank=True, null=True, db_column='单根重', verbose_name='单根重')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_根芥菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class tao(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    case = models.CharField(max_length=30, blank=True, null=True, db_column='彩色', verbose_name='彩色')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    keroxisu = models.CharField(max_length=30, blank=True, null=True, db_column='可溶性酸', verbose_name='可溶性酸')
    keroguxiwu = models.CharField(max_length=30, blank=True, null=True, db_column='可溶固形物', verbose_name='可溶固形物')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    zhye = models.CharField(max_length=30, blank=True, null=True, db_column='汁液', verbose_name='汁液')
    nezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='内质评价', verbose_name='内质评价')
    hufeyowu = models.CharField(max_length=30, blank=True, null=True, db_column='花粉有无', verbose_name='花粉有无')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    daguzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='单果重评价', verbose_name='单果重评价')
    rose = models.CharField(max_length=30, blank=True, null=True, db_column='肉色', verbose_name='肉色')
    gushchshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果实成熟期', verbose_name='果实成熟期')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    daguzhg = models.CharField(db_column='单果重G', max_length=30, blank=True, null=True, verbose_name='单果重G')
    chshqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期评价', verbose_name='成熟期评价')
    keroxita = models.CharField(max_length=30, blank=True, null=True, db_column='可溶性糖', verbose_name='可溶性糖')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    hezhlixi = models.CharField(max_length=30, blank=True, null=True, db_column='核粘离性', verbose_name='核粘离性')
    dise = models.CharField(max_length=30, blank=True, null=True, db_column='底色', verbose_name='底色')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_桃'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class Sang(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    neyeyase = models.CharField(max_length=30, blank=True, null=True, db_column='嫩叶颜色', verbose_name='嫩叶颜色')
    yazhshzhta = models.CharField(max_length=30, blank=True, null=True, db_column='芽着生状态', verbose_name='芽着生状态')
    yema = models.CharField(max_length=30, blank=True, null=True, db_column='叶脉', verbose_name='叶脉')
    qikerota = models.CharField(max_length=30, blank=True, null=True, db_column='秋可溶糖', verbose_name='秋可溶糖')
    chdasajili = models.CharField(max_length=30, blank=True, null=True, db_column='春担桑茧量', verbose_name='春担桑茧量')
    wesuwesubi = models.CharField(max_length=30, blank=True, null=True, db_column='萎缩萎缩病', verbose_name='萎缩萎缩病')
    yemicuhu = models.CharField(max_length=30, blank=True, null=True, db_column='叶面粗滑', verbose_name='叶面粗滑')
    fayaqi = models.CharField(max_length=30, blank=True, null=True, db_column='发芽期', verbose_name='发芽期')
    qigojiyesh = models.CharField(max_length=30, blank=True, null=True, db_column='秋公斤叶数', verbose_name='秋公斤叶数')
    yeyihuqi = models.CharField(max_length=30, blank=True, null=True, db_column='叶硬化期', verbose_name='叶硬化期')
    zhtichdu = models.CharField(max_length=30, blank=True, null=True, db_column='枝条长短', verbose_name='枝条长短')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    qiwajiceli = models.CharField(max_length=30, blank=True, null=True, db_column='秋万茧层量', verbose_name='秋万茧层量')
    kayeqi = models.CharField(max_length=30, blank=True, null=True, db_column='开叶期', verbose_name='开叶期')
    zhta = models.CharField(max_length=30, blank=True, null=True, db_column='枝态', verbose_name='枝态')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    huyewesubi = models.CharField(max_length=30, blank=True, null=True, db_column='花叶萎缩病', verbose_name='花叶萎缩病')
    yehobo = models.CharField(max_length=30, blank=True, null=True, db_column='叶厚薄', verbose_name='叶厚薄')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    chkerota = models.CharField(max_length=30, blank=True, null=True, db_column='春可溶糖', verbose_name='春可溶糖')
    zhchyeli = models.CharField(max_length=30, blank=True, null=True, db_column='株产叶量', verbose_name='株产叶量')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    fayalv = models.CharField(max_length=30, blank=True, null=True, db_column='发芽率', verbose_name='发芽率')
    rasetish = models.CharField(max_length=30, blank=True, null=True, db_column='染色体数', verbose_name='染色体数')
    chwatojili = models.CharField(max_length=30, blank=True, null=True, db_column='春万头茧量', verbose_name='春万头茧量')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yeji = models.CharField(max_length=30, blank=True, null=True, db_column='叶尖', verbose_name='叶尖')
    muchyeli = models.CharField(max_length=30, blank=True, null=True, db_column='亩产叶量', verbose_name='亩产叶量')
    hekuxijubi = models.CharField(max_length=30, blank=True, null=True, db_column='黑枯细菌病', verbose_name='黑枯细菌病')
    yezhshzhta = models.CharField(max_length=30, blank=True, null=True, db_column='叶着生状态', verbose_name='叶着生状态')
    xisudush = models.CharField(max_length=30, blank=True, null=True, db_column='雄穗多少', verbose_name='雄穗多少')
    wuyebi = models.CharField(max_length=30, blank=True, null=True, db_column='污叶病', verbose_name='污叶病')
    yebema = models.CharField(max_length=30, blank=True, null=True, db_column='叶背毛', verbose_name='叶背毛')
    yemiguze = models.CharField(max_length=30, blank=True, null=True, db_column='叶面光泽', verbose_name='叶面光泽')
    zhtipise = models.CharField(max_length=30, blank=True, null=True, db_column='枝条皮色', verbose_name='枝条皮色')
    shyase = models.CharField(max_length=30, blank=True, null=True, db_column='椹颜色', verbose_name='椹颜色')
    huzhyowu = models.CharField(max_length=30, blank=True, null=True, db_column='花柱有无', verbose_name='花柱有无')
    yezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶长', verbose_name='叶长')
    yeyumaci = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘芒刺', verbose_name='叶缘芒刺')
    fatili = models.CharField(max_length=30, blank=True, null=True, db_column='发条力', verbose_name='发条力')
    pikoge = models.CharField(max_length=30, blank=True, null=True, db_column='皮孔个', verbose_name='皮孔个')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    shgeye = models.CharField(max_length=30, blank=True, null=True, db_column='椹梗叶', verbose_name='椹梗叶')
    yj = models.CharField(max_length=30, blank=True, null=True, db_column='叶基', verbose_name='叶基')
    bafebi = models.CharField(max_length=30, blank=True, null=True, db_column='白粉病', verbose_name='白粉病')
    qikubi = models.CharField(max_length=30, blank=True, null=True, db_column='青枯病', verbose_name='青枯病')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    zhzilayudi = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源地', verbose_name='种子来源地')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    fuyadush = models.CharField(max_length=30, blank=True, null=True, db_column='副芽多少', verbose_name='副芽多少')
    naiashxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐湿性', verbose_name='耐湿性')
    yemisu = models.CharField(max_length=30, blank=True, null=True, db_column='叶面缩', verbose_name='叶面缩')
    jijizh = models.CharField(max_length=30, blank=True, null=True, db_column='节间长', verbose_name='节间长')
    yexizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶形状', verbose_name='叶形状')
    doyayase = models.CharField(max_length=30, blank=True, null=True, db_column='冬芽颜色', verbose_name='冬芽颜色')
    zhtiquzh = models.CharField(max_length=30, blank=True, null=True, db_column='枝条曲直', verbose_name='枝条曲直')
    qicudaba = models.CharField(max_length=30, blank=True, null=True, db_column='秋粗蛋白', verbose_name='秋粗蛋白')
    qiwatojili = models.CharField(max_length=30, blank=True, null=True, db_column='秋万头茧量', verbose_name='秋万头茧量')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    yemima = models.CharField(max_length=30, blank=True, null=True, db_column='叶面毛', verbose_name='叶面毛')
    qidasajili = models.CharField(max_length=30, blank=True, null=True, db_column='秋担桑茧量', verbose_name='秋担桑茧量')
    yefu = models.CharField(max_length=30, blank=True, null=True, db_column='叶幅', verbose_name='叶幅')
    shjishxi = models.CharField(max_length=30, blank=True, null=True, db_column='椹结实性', verbose_name='椹结实性')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    xisuchdu = models.CharField(max_length=30, blank=True, null=True, db_column='雄穗长度', verbose_name='雄穗长度')
    hebabi = models.CharField(max_length=30, blank=True, null=True, db_column='褐斑病', verbose_name='褐斑病')
    doyaxizh = models.CharField(max_length=30, blank=True, null=True, db_column='冬芽形状', verbose_name='冬芽形状')
    qimitiye = models.CharField(max_length=30, blank=True, null=True, db_column='秋米条叶', verbose_name='秋米条叶')
    huxi = models.CharField(max_length=30, blank=True, null=True, db_column='花性', verbose_name='花性')
    huhuwesubi = models.CharField(max_length=30, blank=True, null=True, db_column='黄化萎缩病', verbose_name='黄化萎缩病')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    shdush = models.CharField(max_length=30, blank=True, null=True, db_column='椹多少', verbose_name='椹多少')
    chwajiceli = models.CharField(max_length=30, blank=True, null=True, db_column='春万茧层量', verbose_name='春万茧层量')
    zhticuxi = models.CharField(max_length=30, blank=True, null=True, db_column='枝条粗细', verbose_name='枝条粗细')
    shchdu = models.CharField(max_length=30, blank=True, null=True, db_column='椹长度', verbose_name='椹长度')
    yexu = models.CharField(max_length=30, blank=True, null=True, db_column='叶序', verbose_name='叶序')
    shzhyalv = models.CharField(max_length=30, blank=True, null=True, db_column='生长芽率', verbose_name='生长芽率')
    chmitiye = models.CharField(max_length=30, blank=True, null=True, db_column='春米条叶', verbose_name='春米条叶')
    yebizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄长', verbose_name='叶柄长')
    niahanxing = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    sgy = models.CharField(max_length=30, blank=True, null=True, db_column='梢梗叶', verbose_name='梢梗叶')
    tigeye = models.CharField(max_length=30, blank=True, null=True, db_column='条梗叶', verbose_name='条梗叶')
    chgojiyesh = models.CharField(max_length=30, blank=True, null=True, db_column='春公斤叶数', verbose_name='春公斤叶数')
    chcudaba = models.CharField(max_length=30, blank=True, null=True, db_column='春粗蛋白', verbose_name='春粗蛋白')
    huyekafaxu = models.CharField(max_length=30, blank=True, null=True, db_column='花叶开放序', verbose_name='花叶开放序')
    shyofele = models.CharField(max_length=30, blank=True, null=True, db_column='实用分类', verbose_name='实用分类')
    suyexijubi = models.CharField(max_length=30, blank=True, null=True, db_column='缩叶细菌病', verbose_name='缩叶细菌病')
    yegeye = models.CharField(max_length=30, blank=True, null=True, db_column='叶梗叶', verbose_name='叶梗叶')
    zhtomahutu = models.CharField(max_length=30, blank=True, null=True, db_column='柱头毛或突', verbose_name='柱头毛或突')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_桑'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class Dali(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    shyuqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='生育期评价', verbose_name='生育期评价')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shgunili = models.CharField(max_length=30, blank=True, null=True, db_column='始果年龄', verbose_name='始果年龄')
    shyuqi = models.CharField(db_column='生育期D', max_length=30, blank=True, null=True, verbose_name='生育期D')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    zhye = models.CharField(max_length=30, blank=True, null=True, db_column='汁液', verbose_name='汁液')
    nezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='内质评价', verbose_name='内质评价')
    zaguxipiji = models.CharField(max_length=30, blank=True, null=True, db_column='早果性评价', verbose_name='早果性评价')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    keroguxiwu = models.CharField(max_length=30, blank=True, null=True, db_column='可溶固形物', verbose_name='可溶固形物')
    daguzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='单果重评价', verbose_name='单果重评价')
    gushchshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果实成熟期', verbose_name='果实成熟期')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    kedidisu = models.CharField(db_column='可滴定酸％', max_length=30, blank=True, null=True, verbose_name='可滴定酸％')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    chshqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期评价', verbose_name='成熟期评价')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzhg = models.CharField(db_column='单果重G', max_length=30, blank=True, null=True, verbose_name='单果重G')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    keroxita = models.CharField(db_column='可溶性糖％', max_length=30, blank=True, null=True, verbose_name='可溶性糖％')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_梨'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class mianhua(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    milich = models.CharField(max_length=30, blank=True, null=True, db_column='棉铃虫', verbose_name='棉铃虫')
    mife = models.CharField(max_length=30, blank=True, null=True, db_column='棉酚', verbose_name='棉酚')
    shzhsh = models.CharField(max_length=30, blank=True, null=True, db_column='生长势', verbose_name='生长势')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    guzhjiwe = models.CharField(max_length=30, blank=True, null=True, db_column='果枝节位', verbose_name='果枝节位')
    durose = models.CharField(max_length=30, blank=True, null=True, db_column='短绒色', verbose_name='短绒色')
    dani = models.CharField(max_length=30, blank=True, null=True, db_column='单宁', verbose_name='单宁')
    mihozhzh = models.CharField(max_length=30, blank=True, null=True, db_column='棉红蜘蛛', verbose_name='棉红蜘蛛')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株形', verbose_name='株形')
    bawamixi = models.CharField(max_length=30, blank=True, null=True, db_column='苞外蜜腺', verbose_name='苞外蜜腺')
    badu = models.CharField(max_length=30, blank=True, null=True, db_column='白度', verbose_name='白度')
    yehodu = models.CharField(max_length=30, blank=True, null=True, db_column='叶厚度', verbose_name='叶厚度')
    huyase = models.CharField(max_length=30, blank=True, null=True, db_column='花药色', verbose_name='花药色')
    doji = models.CharField(max_length=30, blank=True, null=True, db_column='东经', verbose_name='东经')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yepidaxi = models.CharField(max_length=30, blank=True, null=True, db_column='叶片大小', verbose_name='叶片大小')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    yemixi = models.CharField(max_length=30, blank=True, null=True, db_column='叶蜜腺', verbose_name='叶蜜腺')
    huguse = models.CharField(max_length=30, blank=True, null=True, db_column='花冠色', verbose_name='花冠色')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='铃形', verbose_name='铃形')
    hudaxi = models.CharField(max_length=30, blank=True, null=True, db_column='花大小', verbose_name='花大小')
    kuzh = models.CharField(max_length=30, blank=True, null=True, db_column='跨长', verbose_name='跨长')
    makelozh = models.CharField(max_length=30, blank=True, null=True, db_column='麦克隆值', verbose_name='麦克隆值')
    bewe = models.CharField(max_length=30, blank=True, null=True, db_column='北纬', verbose_name='北纬')
    zhrezhfa = models.CharField(max_length=30, blank=True, null=True, db_column='种仁脂肪', verbose_name='种仁脂肪')
    huwebi = models.CharField(max_length=30, blank=True, null=True, db_column='黄萎病', verbose_name='黄萎病')
    midusu = models.CharField(max_length=30, blank=True, null=True, db_column='棉毒素', verbose_name='棉毒素')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    zhjiyidu = models.CharField(max_length=30, blank=True, null=True, db_column='主茎硬度', verbose_name='主茎硬度')
    guzhsh = models.CharField(max_length=30, blank=True, null=True, db_column='果枝数', verbose_name='果枝数')
    qilishzhsh = models.CharField(max_length=30, blank=True, null=True, db_column='气流纱支数', verbose_name='气流纱支数')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    hufashhash = models.CharField(max_length=30, blank=True, null=True, db_column='环纺纱号数', verbose_name='环纺纱号数')
    dazhlish = models.CharField(max_length=30, blank=True, null=True, db_column='单株铃数', verbose_name='单株铃数')
    huzhzh = models.CharField(max_length=30, blank=True, null=True, db_column='花柱长', verbose_name='花柱长')
    shchbafelv = models.CharField(max_length=30, blank=True, null=True, db_column='伸长百分率', verbose_name='伸长百分率')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    guzhshzhji = models.CharField(max_length=30, blank=True, null=True, db_column='果枝伸展角', verbose_name='果枝伸展角')
    dafuxi = models.CharField(max_length=30, blank=True, null=True, db_column='倒伏性', verbose_name='倒伏性')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    guzhlexi = models.CharField(max_length=30, blank=True, null=True, db_column='果枝类型', verbose_name='果枝类型')
    zazhdeji = models.CharField(max_length=30, blank=True, null=True, db_column='杂质等级', verbose_name='杂质等级')
    jima = models.CharField(max_length=30, blank=True, null=True, db_column='茎毛', verbose_name='茎毛')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    zhzilayudi = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源地', verbose_name='种子来源地')
    pzname = models.CharField(max_length=50, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    ni = models.CharField(max_length=30, blank=True, null=True, db_column='年', verbose_name='年')
    lebi = models.CharField(max_length=30, blank=True, null=True, db_column='类别', verbose_name='类别')
    qilifazhbi = models.CharField(max_length=30, blank=True, null=True, db_column='气流纺指标', verbose_name='气流纺指标')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    gufashlv = models.CharField(max_length=30, blank=True, null=True, db_column='光反射率', verbose_name='光反射率')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    zhziroma = models.CharField(max_length=30, blank=True, null=True, db_column='种子绒毛', verbose_name='种子绒毛')
    yeroma = models.CharField(max_length=30, blank=True, null=True, db_column='叶绒毛', verbose_name='叶绒毛')
    xumise = models.CharField(max_length=30, blank=True, null=True, db_column='絮棉色', verbose_name='絮棉色')
    xumi = models.CharField(max_length=50, blank=True, null=True, db_column='学名', verbose_name='学名')
    gach = models.CharField(max_length=30, blank=True, null=True, db_column='高程', verbose_name='高程')
    holich = models.CharField(max_length=30, blank=True, null=True, db_column='红铃虫', verbose_name='红铃虫')
    huxise = models.CharField(max_length=30, blank=True, null=True, db_column='花芯色', verbose_name='花芯色')
    kuwebi = models.CharField(max_length=30, blank=True, null=True, db_column='枯萎病', verbose_name='枯萎病')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='铃色', verbose_name='铃色')
    yezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='叶枝数', verbose_name='叶枝数')
    hufashqili = models.CharField(max_length=30, blank=True, null=True, db_column='环纺纱强力', verbose_name='环纺纱强力')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    chduzhqidu = models.CharField(max_length=30, blank=True, null=True, db_column='长度整齐度', verbose_name='长度整齐度')
    zizh = models.CharField(max_length=30, blank=True, null=True, db_column='子指', verbose_name='子指')
    lishsh = models.CharField(max_length=30, blank=True, null=True, db_column='铃室数', verbose_name='铃室数')
    yach = models.CharField(max_length=30, blank=True, null=True, db_column='蚜虫', verbose_name='蚜虫')
    likali = models.CharField(max_length=30, blank=True, null=True, db_column='铃开裂', verbose_name='铃开裂')
    nayaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐盐性', verbose_name='耐盐性')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    libizh = models.CharField(max_length=30, blank=True, null=True, db_column='铃柄长', verbose_name='铃柄长')
    bayexizh = models.CharField(max_length=30, blank=True, null=True, db_column='苞叶形状', verbose_name='苞叶形状')
    biqidu = models.CharField(max_length=30, blank=True, null=True, db_column='比强度', verbose_name='比强度')
    zhredaba = models.CharField(max_length=30, blank=True, null=True, db_column='种仁蛋白', verbose_name='种仁蛋白')
    yife = models.CharField(max_length=30, blank=True, null=True, db_column='衣分', verbose_name='衣分')
    lizh = models.CharField(max_length=30, blank=True, null=True, db_column='铃重', verbose_name='铃重')
    lizhshfash = models.CharField(max_length=30, blank=True, null=True, db_column='铃着生方式', verbose_name='铃着生方式')
    zhjicuxi = models.CharField(max_length=30, blank=True, null=True, db_column='主茎粗细', verbose_name='主茎粗细')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    tuxi = models.CharField(max_length=30, blank=True, null=True, db_column='图象', verbose_name='图象')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_棉花'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class yezi(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    yepiyase = models.CharField(max_length=30, blank=True, null=True, db_column='叶片颜色', verbose_name='叶片颜色')
    zhch = models.CharField(max_length=30, blank=True, null=True, db_column='中产', verbose_name='中产')
    bimi = models.CharField(max_length=30, blank=True, null=True, db_column='别名', verbose_name='别名')
    zhzhrupush = models.CharField(max_length=30, blank=True, null=True, db_column='种质入圃数', verbose_name='种质入圃数')
    shyimidu = models.CharField(max_length=30, blank=True, null=True, db_column='适应密度', verbose_name='适应密度')
    xihu = models.CharField(max_length=30, blank=True, null=True, db_column='雄花', verbose_name='雄花')
    kogu = models.CharField(max_length=30, blank=True, null=True, db_column='空果', verbose_name='空果')
    shyifeli = models.CharField(max_length=30, blank=True, null=True, db_column='适应肥力', verbose_name='适应肥力')
    jijishli = models.CharField(max_length=30, blank=True, null=True, db_column='经济树龄', verbose_name='经济树龄')
    huba = models.CharField(max_length=30, blank=True, null=True, db_column='花苞', verbose_name='花苞')
    yuanming = models.CharField(max_length=30, blank=True, null=True, db_column='原名', verbose_name='原名')
    chli = models.CharField(max_length=30, blank=True, null=True, db_column='产量', verbose_name='产量')
    yizhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='引种单位', verbose_name='引种单位')
    bacuhaba = models.CharField(max_length=30, blank=True, null=True, db_column='保存海拔', verbose_name='保存海拔')
    shyiwedu = models.CharField(max_length=30, blank=True, null=True, db_column='适应温度', verbose_name='适应温度')
    shjifeha = models.CharField(max_length=30, blank=True, null=True, db_column='十级风害', verbose_name='十级风害')
    shyipodu = models.CharField(max_length=30, blank=True, null=True, db_column='适应坡度', verbose_name='适应坡度')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    shfefash = models.CharField(max_length=30, blank=True, null=True, db_column='授粉方式', verbose_name='授粉方式')
    bacujidu = models.CharField(max_length=30, blank=True, null=True, db_column='保存经度', verbose_name='保存经度')
    shsh = models.CharField(max_length=30, blank=True, null=True, db_column='生势', verbose_name='生势')
    xiyedush = models.CharField(max_length=30, blank=True, null=True, db_column='小叶对数', verbose_name='小叶对数')
    huqi = models.CharField(max_length=30, blank=True, null=True, db_column='花期', verbose_name='花期')
    dich = models.CharField(max_length=30, blank=True, null=True, db_column='低产', verbose_name='低产')
    yepixita = models.CharField(max_length=30, blank=True, null=True, db_column='叶片形态', verbose_name='叶片形态')
    daxiniyowu = models.CharField(max_length=30, blank=True, null=True, db_column='大小年有无', verbose_name='大小年有无')
    zhfayashji = models.CharField(max_length=30, blank=True, null=True, db_column='种发芽时间', verbose_name='种发芽时间')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    gushyase = models.CharField(max_length=30, blank=True, null=True, db_column='果实颜色', verbose_name='果实颜色')
    shyishdu = models.CharField(max_length=30, blank=True, null=True, db_column='适应湿度', verbose_name='适应湿度')
    bacuwedu = models.CharField(max_length=30, blank=True, null=True, db_column='保存纬度', verbose_name='保存纬度')
    zhke = models.CharField(max_length=30, blank=True, null=True, db_column='种壳', verbose_name='种壳')
    zhzhcali = models.CharField(max_length=30, blank=True, null=True, db_column='种质材料', verbose_name='种质材料')
    shguxita = models.CharField(max_length=30, blank=True, null=True, db_column='树冠形态', verbose_name='树冠形态')
    zhzhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='种质来源', verbose_name='种质来源')
    hubi = models.CharField(max_length=30, blank=True, null=True, db_column='花柄', verbose_name='花柄')
    xiyekudu = models.CharField(max_length=30, blank=True, null=True, db_column='小叶宽度', verbose_name='小叶宽度')
    cihuhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='雌花花期', verbose_name='雌花花期')
    xihuhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='雄花花期', verbose_name='雄花花期')
    shgu = models.CharField(max_length=30, blank=True, null=True, db_column='树冠', verbose_name='树冠')
    sherjifeha = models.CharField(max_length=30, blank=True, null=True, db_column='十二级风害', verbose_name='十二级风害')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    shdixishwe = models.CharField(max_length=30, blank=True, null=True, db_column='适地下水位', verbose_name='适地下水位')
    shyihaba = models.CharField(max_length=30, blank=True, null=True, db_column='适应海拔', verbose_name='适应海拔')
    lugu = models.CharField(max_length=30, blank=True, null=True, db_column='落果', verbose_name='落果')
    huxuzugulv = models.CharField(max_length=30, blank=True, null=True, db_column='花序座果率', verbose_name='花序座果率')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    huqichdi = models.CharField(max_length=30, blank=True, null=True, db_column='花期重叠', verbose_name='花期重叠')
    zajiqiheli = models.CharField(max_length=30, blank=True, null=True, db_column='杂交亲和力', verbose_name='杂交亲和力')
    cixihuqi = models.CharField(max_length=30, blank=True, null=True, db_column='雌雄花期', verbose_name='雌雄花期')
    ligu = models.CharField(max_length=30, blank=True, null=True, db_column='裂果', verbose_name='裂果')
    bacuzudiwe = models.CharField(max_length=30, blank=True, null=True, db_column='保存最低温', verbose_name='保存最低温')
    yezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶长', verbose_name='叶长')
    jiyidawe = models.CharField(max_length=30, blank=True, null=True, db_column='检疫单位', verbose_name='检疫单位')
    jiyiqiku = models.CharField(max_length=30, blank=True, null=True, db_column='检疫情况', verbose_name='检疫情况')
    shzhsudu = models.CharField(max_length=30, blank=True, null=True, db_column='生长速度', verbose_name='生长速度')
    huzh = models.CharField(max_length=30, blank=True, null=True, db_column='花枝', verbose_name='花枝')
    jiguqi = models.CharField(max_length=30, blank=True, null=True, db_column='结果期', verbose_name='结果期')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    zhpumiji = models.CharField(max_length=30, blank=True, null=True, db_column='种圃面积', verbose_name='种圃面积')
    jigagadu = models.CharField(max_length=30, blank=True, null=True, db_column='茎干高度', verbose_name='茎干高度')
    fazhfafa = models.CharField(max_length=30, blank=True, null=True, db_column='繁殖方法', verbose_name='繁殖方法')
    zhzhleximi = models.CharField(max_length=30, blank=True, null=True, db_column='种质类型名', verbose_name='种质类型名')
    yirucali = models.CharField(max_length=30, blank=True, null=True, db_column='引入材料', verbose_name='引入材料')
    bajifeha = models.CharField(max_length=30, blank=True, null=True, db_column='八级风害', verbose_name='八级风害')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    kabichneli = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫能力', verbose_name='抗病虫能力')
    yirushli = models.CharField(max_length=30, blank=True, null=True, db_column='引入数量', verbose_name='引入数量')
    gushxizh = models.CharField(max_length=30, blank=True, null=True, db_column='果实形状', verbose_name='果实形状')
    jigayehe = models.CharField(max_length=30, blank=True, null=True, db_column='茎干叶痕', verbose_name='茎干叶痕')
    shgatezh = models.CharField(max_length=30, blank=True, null=True, db_column='树干特征', verbose_name='树干特征')
    bacunijuwe = models.CharField(max_length=30, blank=True, null=True, db_column='保存年均温', verbose_name='保存年均温')
    yeshtidu = models.CharField(max_length=30, blank=True, null=True, db_column='椰水甜度', verbose_name='椰水甜度')
    shyiyuli = models.CharField(max_length=30, blank=True, null=True, db_column='适应雨量', verbose_name='适应雨量')
    kahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗寒性', verbose_name='抗寒性')
    shgaguhudu = models.CharField(max_length=30, blank=True, null=True, db_column='树干光滑度', verbose_name='树干光滑度')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    jigacudu = models.CharField(max_length=30, blank=True, null=True, db_column='茎干粗度', verbose_name='茎干粗度')
    yizhha = models.CharField(max_length=30, blank=True, null=True, db_column='引种号', verbose_name='引种号')
    shli = models.CharField(max_length=30, blank=True, null=True, db_column='树龄', verbose_name='树龄')
    gupi = models.CharField(max_length=30, blank=True, null=True, db_column='果皮', verbose_name='果皮')
    huxuxita = models.CharField(max_length=30, blank=True, null=True, db_column='花序形态', verbose_name='花序形态')
    yizhde = models.CharField(max_length=30, blank=True, null=True, db_column='引种地', verbose_name='引种地')
    bacuniyuli = models.CharField(max_length=30, blank=True, null=True, db_column='保存年雨量', verbose_name='保存年雨量')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    cihu = models.CharField(max_length=30, blank=True, null=True, db_column='雌花', verbose_name='雌花')
    jishneli = models.CharField(max_length=30, blank=True, null=True, db_column='结实能力', verbose_name='结实能力')
    yirushji = models.CharField(max_length=30, blank=True, null=True, db_column='引入时间', verbose_name='引入时间')
    gach = models.CharField(max_length=30, blank=True, null=True, db_column='高产', verbose_name='高产')
    bacudimi = models.CharField(max_length=30, blank=True, null=True, db_column='保存地名', verbose_name='保存地名')
    hz = models.CharField(max_length=30, blank=True, null=True, db_column='花轴', verbose_name='花轴')
    zhzhmich = models.CharField(max_length=30, blank=True, null=True, db_column='种质名称', verbose_name='种质名称')
    gushdaxi = models.CharField(max_length=30, blank=True, null=True, db_column='果实大小', verbose_name='果实大小')
    digu = models.CharField(max_length=30, blank=True, null=True, db_column='吊果', verbose_name='吊果')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_椰子'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class xiangjiao(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    jiruyase = models.CharField(max_length=30, blank=True, null=True, db_column='胶乳颜色', verbose_name='胶乳颜色')
    saxiyejiju = models.CharField(max_length=30, blank=True, null=True, db_column='三小叶间距', verbose_name='三小叶间距')
    shzhkuma = models.CharField(max_length=30, blank=True, null=True, db_column='生长快慢', verbose_name='生长快慢')
    yepixizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶片形状', verbose_name='叶片形状')
    cemaji = models.CharField(max_length=30, blank=True, null=True, db_column='侧脉胶', verbose_name='侧脉胶')
    yeji = models.CharField(max_length=30, blank=True, null=True, db_column='叶基', verbose_name='叶基')
    xumi = models.CharField(max_length=50, blank=True, null=True, db_column='学名', verbose_name='学名')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    xiyebichdu = models.CharField(max_length=30, blank=True, null=True, db_column='小叶柄长度', verbose_name='小叶柄长度')
    wuholuye = models.CharField(max_length=30, blank=True, null=True, db_column='物候落叶', verbose_name='物候落叶')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yeyuxizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘形状', verbose_name='叶缘形状')
    chligadib = models.CharField(db_column='产量高低B', max_length=30, blank=True, null=True, verbose_name='产量高低B')
    chligadia = models.CharField(db_column='产量高低A', max_length=30, blank=True, null=True, verbose_name='产量高低A')
    rasetish = models.CharField(max_length=30, blank=True, null=True, db_column='染色体数', verbose_name='染色体数')
    luyezawa = models.CharField(max_length=30, blank=True, null=True, db_column='落叶早晚', verbose_name='落叶早晚')
    jizhbi = models.CharField(max_length=30, blank=True, null=True, db_column='胶值比', verbose_name='胶值比')
    wuhochya = models.CharField(max_length=30, blank=True, null=True, db_column='物候抽芽', verbose_name='物候抽芽')
    mixixita = models.CharField(max_length=30, blank=True, null=True, db_column='蜜腺形态', verbose_name='蜜腺形态')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    jiwebi = models.CharField(max_length=30, blank=True, null=True, db_column='茎围比', verbose_name='茎围比')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zhzhmich = models.CharField(max_length=30, blank=True, null=True, db_column='种质名称', verbose_name='种质名称')
    dayezh = models.CharField(max_length=30, blank=True, null=True, db_column='大叶枕', verbose_name='大叶枕')
    chyazawa = models.CharField(max_length=30, blank=True, null=True, db_column='抽芽早晚', verbose_name='抽芽早晚')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_橡胶'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class maodou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    zhpicise = models.CharField(max_length=30, blank=True, null=True, db_column='种皮次色', verbose_name='种皮次色')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    zhzipise = models.CharField(max_length=30, blank=True, null=True, db_column='种子皮色', verbose_name='种子皮色')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    yibase = models.CharField(max_length=30, blank=True, null=True, db_column='翼瓣色', verbose_name='翼瓣色')
    zhzixizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子形状', verbose_name='种子形状')
    nejicise = models.CharField(max_length=30, blank=True, null=True, db_column='嫩荚次色', verbose_name='嫩荚次色')
    zhzidaxi = models.CharField(max_length=30, blank=True, null=True, db_column='种子大小', verbose_name='种子大小')
    nejise = models.CharField(max_length=30, blank=True, null=True, db_column='嫩荚色', verbose_name='嫩荚色')
    yibacise = models.CharField(max_length=30, blank=True, null=True, db_column='翼瓣次色', verbose_name='翼瓣次色')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    jiho = models.CharField(max_length=30, blank=True, null=True, db_column='荚厚', verbose_name='荚厚')
    jixi = models.CharField(max_length=30, blank=True, null=True, db_column='荚形', verbose_name='荚形')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    xpvjirish = models.CharField(max_length=30, blank=True, null=True, db_column='老荚日数', verbose_name='老荚日数')
    dajizh = models.CharField(max_length=30, blank=True, null=True, db_column='单荚重', verbose_name='单荚重')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    qijirish = models.CharField(max_length=30, blank=True, null=True, db_column='青荚日数', verbose_name='青荚日数')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    jiku = models.CharField(max_length=30, blank=True, null=True, db_column='荚宽', verbose_name='荚宽')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_毛豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class shuidao(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    jimilv = models.CharField(max_length=30, blank=True, null=True, db_column='精米率', verbose_name='精米率')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    huyichdu = models.CharField(max_length=30, blank=True, null=True, db_column='护颖长短', verbose_name='护颖长短')
    huhuwedu = models.CharField(max_length=30, blank=True, null=True, db_column='糊化温度', verbose_name='糊化温度')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    xuyudawe = models.CharField(max_length=30, blank=True, null=True, db_column='选育单位', verbose_name='选育单位')
    mise = models.CharField(max_length=30, blank=True, null=True, db_column='米色', verbose_name='米色')
    babefesh = models.CharField(max_length=30, blank=True, null=True, db_column='白背飞虱', verbose_name='白背飞虱')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    fafajizuhe = models.TextField(blank=True, null=True, db_column='方法及组合', verbose_name='方法及组合')
    miqinaha = models.CharField(max_length=30, blank=True, null=True, db_column='苗期耐旱', verbose_name='苗期耐旱')
    mazh = models.CharField(max_length=30, blank=True, null=True, db_column='芒长', verbose_name='芒长')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    bayeku = models.CharField(max_length=30, blank=True, null=True, db_column='白叶枯', verbose_name='白叶枯')
    camilv = models.CharField(max_length=30, blank=True, null=True, db_column='糙米率', verbose_name='糙米率')
    miwe = models.CharField(max_length=30, blank=True, null=True, db_column='苗瘟', verbose_name='苗瘟')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    lixizh = models.CharField(max_length=30, blank=True, null=True, db_column='粒形状', verbose_name='粒形状')
    doji = models.CharField(max_length=30, blank=True, null=True, db_column='东经', verbose_name='东经')
    mixi = models.CharField(max_length=30, blank=True, null=True, db_column='米香', verbose_name='米香')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    yimayowu = models.CharField(max_length=30, blank=True, null=True, db_column='颖毛有无', verbose_name='颖毛有无')
    yikese = models.CharField(max_length=30, blank=True, null=True, db_column='颖壳色', verbose_name='颖壳色')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    shlu = models.CharField(max_length=30, blank=True, null=True, db_column='水陆', verbose_name='水陆')
    wekubi = models.CharField(max_length=30, blank=True, null=True, db_column='纹枯病', verbose_name='纹枯病')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    xiji = models.CharField(max_length=30, blank=True, null=True, db_column='籼粳', verbose_name='籼粳')
    zhkubi = models.CharField(max_length=30, blank=True, null=True, db_column='长宽比', verbose_name='长宽比')
    naya = models.CharField(max_length=30, blank=True, null=True, db_column='耐盐', verbose_name='耐盐')
    chsuqi = models.CharField(max_length=30, blank=True, null=True, db_column='出穗期', verbose_name='出穗期')
    dabazh = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    bewe = models.CharField(max_length=30, blank=True, null=True, db_column='北纬', verbose_name='北纬')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    yijiwazh = models.CharField(max_length=30, blank=True, null=True, db_column='颖尖弯直', verbose_name='颖尖弯直')
    hedash = models.CharField(max_length=30, blank=True, null=True, db_column='褐稻虱', verbose_name='褐稻虱')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    lichdu = models.CharField(max_length=30, blank=True, null=True, db_column='粒长度', verbose_name='粒长度')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    zhnu = models.CharField(max_length=30, blank=True, null=True, db_column='粘糯', verbose_name='粘糯')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yijise = models.CharField(max_length=30, blank=True, null=True, db_column='颖尖色', verbose_name='颖尖色')
    naias = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    bacudawe_2 = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位_2', verbose_name='保存单位_2')
    gach = models.CharField(max_length=30, blank=True, null=True, db_column='高程', verbose_name='高程')
    ebalv = models.CharField(max_length=30, blank=True, null=True, db_column='垩白率', verbose_name='垩白率')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    jichdu = models.CharField(max_length=30, blank=True, null=True, db_column='胶稠度', verbose_name='胶稠度')
    yaqinaha = models.CharField(max_length=30, blank=True, null=True, db_column='芽期耐寒', verbose_name='芽期耐寒')
    zazhwa = models.CharField(max_length=30, blank=True, null=True, db_column='早中晚', verbose_name='早中晚')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    xipu = models.CharField(max_length=30, blank=True, null=True, db_column='系谱', verbose_name='系谱')
    yexiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='叶锈严重度', verbose_name='叶锈严重度')
    sxsh = models.CharField(max_length=30, blank=True, null=True, db_column='穗行数', verbose_name='穗行数')
    sx = models.CharField(max_length=30, blank=True, null=True, db_column='穗形', verbose_name='穗形')
    tahuli = models.CharField(max_length=30, blank=True, null=True, db_column='糖化力', verbose_name='糖化力')
    yexifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='叶锈反应型', verbose_name='叶锈反应型')
    subizh = models.CharField(max_length=30, blank=True, null=True, db_column='穗柄长', verbose_name='穗柄长')
    sumidu = models.CharField(max_length=30, blank=True, null=True, db_column='穗密度', verbose_name='穗密度')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    shyurish = models.CharField(max_length=30, blank=True, null=True, db_column='生育日数', verbose_name='生育日数')
    laanzhdaba = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨占蛋白', verbose_name='赖氨占蛋白')
    kahajibi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱级别', verbose_name='抗旱级别')
    chmebibisu = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病病穗', verbose_name='赤霉病病穗')
    shsulv = models.CharField(max_length=30, blank=True, null=True, db_column='双穗率', verbose_name='双穗率')
    chdu = models.CharField(max_length=30, blank=True, null=True, db_column='锤度', verbose_name='锤度')
    tiwebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='条纹病抗性', verbose_name='条纹病抗性')
    cuzodife = models.CharField(max_length=30, blank=True, null=True, db_column='粗总淀粉', verbose_name='粗总淀粉')
    layudi = models.CharField(max_length=30, blank=True, null=True, db_column='来源地', verbose_name='来源地')
    fenili = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖力', verbose_name='分蘖力')
    gaxiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈严重度', verbose_name='秆锈严重度')
    balilv = models.CharField(max_length=30, blank=True, null=True, db_column='爆裂率', verbose_name='爆裂率')
    fenixi = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖性', verbose_name='分蘖性')
    tiwebibilv = models.CharField(max_length=30, blank=True, null=True, db_column='条纹病病率', verbose_name='条纹病病率')
    ma = models.CharField(max_length=30, blank=True, null=True, db_column='芒', verbose_name='芒')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    yirushji = models.CharField(max_length=30, blank=True, null=True, db_column='引入时间', verbose_name='引入时间')
    shmichdu = models.CharField(max_length=30, blank=True, null=True, db_column='水敏称度', verbose_name='水敏称度')
    gaxifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈反应型', verbose_name='秆锈反应型')
    hushxisu = models.CharField(max_length=30, blank=True, null=True, db_column='花生稀酸', verbose_name='花生稀酸')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    jicu = models.CharField(max_length=30, blank=True, null=True, db_column='茎粗', verbose_name='茎粗')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒型', verbose_name='粒型')
    shfe = models.CharField(max_length=30, blank=True, null=True, db_column='水份', verbose_name='水份')
    pilu = models.CharField(max_length=30, blank=True, null=True, db_column='皮裸', verbose_name='皮裸')
    sulish = models.CharField(max_length=30, blank=True, null=True, db_column='穗粒数', verbose_name='穗粒数')
    dabapiji = models.CharField(max_length=30, blank=True, null=True, db_column='大斑评价', verbose_name='大斑评价')
    sihesubilv = models.CharField(max_length=30, blank=True, null=True, db_column='丝黑穗病率', verbose_name='丝黑穗病率')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    maxi = models.CharField(max_length=30, blank=True, null=True, db_column='芒性', verbose_name='芒性')
    chdizh = models.CharField(max_length=30, blank=True, null=True, db_column='沉淀值', verbose_name='沉淀值')
    zhjiyepish = models.CharField(max_length=30, blank=True, null=True, db_column='主茎叶片数', verbose_name='主茎叶片数')
    yikebapidu = models.CharField(max_length=30, blank=True, null=True, db_column='颖壳包皮度', verbose_name='颖壳包皮度')
    chmebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病抗性', verbose_name='赤霉病抗性')
    kahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱性', verbose_name='抗旱性')
    xisufezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='雄穗分枝数', verbose_name='雄穗分枝数')
    gujikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='灌浆抗寒性', verbose_name='灌浆抗寒性')
    shbiha = models.CharField(max_length=30, blank=True, null=True, db_column='省编号', verbose_name='省编号')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='棱型', verbose_name='棱型')
    bafefayixi = models.CharField(max_length=30, blank=True, null=True, db_column='白粉反应型', verbose_name='白粉反应型')
    zolvsu = models.CharField(max_length=30, blank=True, null=True, db_column='棕榈酸', verbose_name='棕榈酸')
    yomise = models.CharField(max_length=30, blank=True, null=True, db_column='幼苗色', verbose_name='幼苗色')
    huhufabilv = models.CharField(max_length=30, blank=True, null=True, db_column='黄花发病率', verbose_name='黄花发病率')
    dochxi = models.CharField(max_length=30, blank=True, null=True, db_column='冬春性', verbose_name='冬春性')
    feyush = models.CharField(max_length=30, blank=True, null=True, db_column='α生育酚', verbose_name='α生育酚')
    dafuxi = models.CharField(max_length=30, blank=True, null=True, db_column='倒伏性', verbose_name='倒伏性')
    qufejichwu = models.CharField(max_length=30, blank=True, null=True, db_column='全粉浸出物', verbose_name='全粉浸出物')
    chmebibizh = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病病指', verbose_name='赤霉病病指')
    suwega = models.CharField(max_length=30, blank=True, null=True, db_column='穗位高', verbose_name='穗位高')
    kese = models.CharField(max_length=30, blank=True, null=True, db_column='壳色', verbose_name='壳色')
    xibapiji = models.CharField(max_length=30, blank=True, null=True, db_column='小斑评价', verbose_name='小斑评价')
    miqikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='苗期抗寒性', verbose_name='苗期抗寒性')
    chmebisulv = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病穗率', verbose_name='赤霉病穗率')
    layugu = models.CharField(max_length=30, blank=True, null=True, db_column='来源国', verbose_name='来源国')
    sihesupi = models.CharField(max_length=30, blank=True, null=True, db_column='丝黑穗评', verbose_name='丝黑穗评')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_水稻'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class youli(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    dabazh = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    yeshshsudu = models.CharField(max_length=30, blank=True, null=True, db_column='叶失水速度', verbose_name='叶失水速度')
    fezhgadi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝高低', verbose_name='分枝高低')
    xiyeyupebi = models.CharField(max_length=30, blank=True, null=True, db_column='小叶与蓬比', verbose_name='小叶与蓬比')
    jiwe = models.CharField(max_length=30, blank=True, null=True, db_column='茎围', verbose_name='茎围')
    daha = models.CharField(max_length=30, blank=True, null=True, db_column='代号', verbose_name='代号')
    gufudaxi = models.CharField(max_length=30, blank=True, null=True, db_column='冠幅大小', verbose_name='冠幅大小')
    shgalexi = models.CharField(max_length=30, blank=True, null=True, db_column='树高类型', verbose_name='树高类型')
    guzohebi = models.CharField(max_length=30, blank=True, null=True, db_column='果纵横比', verbose_name='果纵横比')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    shjifedalv = models.CharField(max_length=30, blank=True, null=True, db_column='十级风倒率', verbose_name='十级风倒率')
    shga = models.CharField(max_length=30, blank=True, null=True, db_column='树高', verbose_name='树高')
    yizhde = models.CharField(max_length=30, blank=True, null=True, db_column='引种地', verbose_name='引种地')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    hegubi = models.CharField(max_length=30, blank=True, null=True, db_column='核果比', verbose_name='核果比')
    guroyase = models.CharField(max_length=30, blank=True, null=True, db_column='果肉颜色', verbose_name='果肉颜色')
    anjisuzoli = models.CharField(max_length=30, blank=True, null=True, db_column='氨基酸总量', verbose_name='氨基酸总量')
    kahaxipiji = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱性评价', verbose_name='抗旱性评价')
    fezhgadu = models.CharField(max_length=30, blank=True, null=True, db_column='分枝高度', verbose_name='分枝高度')
    yepixizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶片形状', verbose_name='叶片形状')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单果重', verbose_name='单果重')
    wujifedalv = models.CharField(max_length=30, blank=True, null=True, db_column='五级风倒率', verbose_name='五级风倒率')
    guroxiwe = models.CharField(max_length=30, blank=True, null=True, db_column='果肉纤维', verbose_name='果肉纤维')
    yepizohebi = models.CharField(max_length=30, blank=True, null=True, db_column='叶片纵横比', verbose_name='叶片纵横比')
    huqi = models.CharField(max_length=30, blank=True, null=True, db_column='花期', verbose_name='花期')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='熟果皮色', verbose_name='熟果皮色')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    chyeqi = models.CharField(max_length=30, blank=True, null=True, db_column='抽叶期', verbose_name='抽叶期')
    zhfa = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪', verbose_name='脂肪')
    chlipiji = models.CharField(max_length=30, blank=True, null=True, db_column='产量评价', verbose_name='产量评价')
    shzhkuma = models.CharField(max_length=30, blank=True, null=True, db_column='生长快慢', verbose_name='生长快慢')
    xiyemidu = models.CharField(max_length=30, blank=True, null=True, db_column='小叶密度', verbose_name='小叶密度')
    jiwedaxi = models.CharField(max_length=30, blank=True, null=True, db_column='茎围大小', verbose_name='茎围大小')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    pirohalifo = models.CharField(max_length=30, blank=True, null=True, db_column='皮肉好离否', verbose_name='皮肉好离否')
    guhejimidu = models.CharField(max_length=30, blank=True, null=True, db_column='果核紧密度', verbose_name='果核紧密度')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    huxi = models.CharField(max_length=30, blank=True, null=True, db_column='花型', verbose_name='花型')
    chli = models.CharField(max_length=30, blank=True, null=True, db_column='产量', verbose_name='产量')
    zhzhmidu = models.CharField(max_length=30, blank=True, null=True, db_column='种植密度', verbose_name='种植密度')
    yepihobo = models.CharField(max_length=30, blank=True, null=True, db_column='叶片厚薄', verbose_name='叶片厚薄')
    mezhgush = models.CharField(max_length=30, blank=True, null=True, db_column='每株果数', verbose_name='每株果数')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='盛花期', verbose_name='盛花期')
    pixi = models.CharField(max_length=30, blank=True, null=True, db_column='品系', verbose_name='品系')
    zhzhmich = models.CharField(max_length=30, blank=True, null=True, db_column='种质名称', verbose_name='种质名称')
    muchgush = models.CharField(max_length=30, blank=True, null=True, db_column='亩产果数', verbose_name='亩产果数')
    huyeqi = models.CharField(max_length=30, blank=True, null=True, db_column='换叶期', verbose_name='换叶期')
    kafeneli = models.CharField(max_length=30, blank=True, null=True, db_column='抗风能力', verbose_name='抗风能力')
    chguqi = models.CharField(max_length=30, blank=True, null=True, db_column='成果期', verbose_name='成果期')
    hufe = models.CharField(max_length=30, blank=True, null=True, db_column='灰分', verbose_name='灰分')
    yepihodu = models.CharField(max_length=30, blank=True, null=True, db_column='叶片厚度', verbose_name='叶片厚度')
    gurofewe = models.CharField(max_length=30, blank=True, null=True, db_column='果肉风味', verbose_name='果肉风味')
    chhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='初花期', verbose_name='初花期')
    gazh = models.CharField(max_length=30, blank=True, null=True, db_column='干重', verbose_name='干重')
    fehajudalv = models.CharField(max_length=30, blank=True, null=True, db_column='风害均倒率', verbose_name='风害均倒率')
    yebipiji = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄评价', verbose_name='叶柄评价')
    shgapiji = models.CharField(max_length=30, blank=True, null=True, db_column='树高评价', verbose_name='树高评价')
    yebichdu = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄长度', verbose_name='叶柄长度')
    yubacupu = models.CharField(max_length=30, blank=True, null=True, db_column='院保存圃', verbose_name='院保存圃')
    gufu = models.CharField(max_length=30, blank=True, null=True, db_column='冠幅', verbose_name='冠幅')
    tashhuhewu = models.CharField(max_length=30, blank=True, null=True, db_column='碳水化合物', verbose_name='碳水化合物')
    gupihodu = models.CharField(max_length=30, blank=True, null=True, db_column='果皮厚度', verbose_name='果皮厚度')
    hezh = models.CharField(max_length=30, blank=True, null=True, db_column='核重', verbose_name='核重')
    fehachdu = models.CharField(max_length=30, blank=True, null=True, db_column='风害程度', verbose_name='风害程度')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_油梨'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class youcai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    wuxiji = models.CharField(max_length=30, blank=True, null=True, db_column='戊烯基', verbose_name='戊烯基')
    zolvsu = models.CharField(max_length=30, blank=True, null=True, db_column='棕榈酸', verbose_name='棕榈酸')
    jijiyidu = models.CharField(max_length=30, blank=True, null=True, db_column='甲基吲哚', verbose_name='甲基吲哚')
    bixiji = models.CharField(max_length=30, blank=True, null=True, db_column='丙烯基', verbose_name='丙烯基')
    megulish = models.CharField(max_length=30, blank=True, null=True, db_column='每果粒数', verbose_name='每果粒数')
    quzhjigush = models.CharField(max_length=30, blank=True, null=True, db_column='全株角果数', verbose_name='全株角果数')
    qiji = models.CharField(max_length=30, blank=True, null=True, db_column='羟基', verbose_name='羟基')
    yicifezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='一次分枝数', verbose_name='一次分枝数')
    yizhsu = models.CharField(max_length=30, blank=True, null=True, db_column='硬脂酸', verbose_name='硬脂酸')
    shyurish = models.CharField(max_length=30, blank=True, null=True, db_column='生育日数', verbose_name='生育日数')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='类型', verbose_name='类型')
    layu = models.CharField(max_length=30, blank=True, null=True, db_column='来源', verbose_name='来源')
    dixiji = models.CharField(max_length=30, blank=True, null=True, db_column='丁烯基', verbose_name='丁烯基')
    jisu = models.CharField(max_length=30, blank=True, null=True, db_column='芥酸', verbose_name='芥酸')
    doji = models.CharField(max_length=30, blank=True, null=True, db_column='东经', verbose_name='东经')
    zoli = models.CharField(max_length=30, blank=True, null=True, db_column='总量', verbose_name='总量')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    gach = models.CharField(max_length=30, blank=True, null=True, db_column='高程', verbose_name='高程')
    xiji = models.CharField(max_length=30, blank=True, null=True, db_column='烯基', verbose_name='烯基')
    xuyufafa = models.CharField(max_length=30, blank=True, null=True, db_column='选育方法', verbose_name='选育方法')
    zhpise = models.CharField(max_length=30, blank=True, null=True, db_column='种皮色', verbose_name='种皮色')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    bewe = models.CharField(max_length=30, blank=True, null=True, db_column='北纬', verbose_name='北纬')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yidu = models.CharField(max_length=30, blank=True, null=True, db_column='吲哚', verbose_name='吲哚')
    fezhgadu = models.CharField(max_length=30, blank=True, null=True, db_column='分枝高度', verbose_name='分枝高度')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶型', verbose_name='叶型')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    yayosu = models.CharField(max_length=30, blank=True, null=True, db_column='亚油酸', verbose_name='亚油酸')
    juhebi = models.CharField(max_length=30, blank=True, null=True, db_column='菌核病', verbose_name='菌核病')
    x1 = models.CharField(db_column='X1', max_length=30, blank=True, null=True, verbose_name='X1')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    shmebi = models.CharField(max_length=30, blank=True, null=True, db_column='霜霉病', verbose_name='霜霉病')
    hushxisu = models.CharField(max_length=30, blank=True, null=True, db_column='花生烯酸', verbose_name='花生烯酸')
    yosu = models.CharField(max_length=30, blank=True, null=True, db_column='油酸', verbose_name='油酸')
    bidubi = models.CharField(max_length=30, blank=True, null=True, db_column='病毒病', verbose_name='病毒病')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    hayolv = models.CharField(max_length=30, blank=True, null=True, db_column='含油率', verbose_name='含油率')
    yamasu = models.CharField(max_length=30, blank=True, null=True, db_column='亚麻酸', verbose_name='亚麻酸')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_油菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class yangcong(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    lijixizh = models.CharField(max_length=30, blank=True, null=True, db_column='鳞茎形状', verbose_name='鳞茎形状')
    yelafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶蜡粉', verbose_name='叶蜡粉')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    xiqi = models.CharField(max_length=30, blank=True, null=True, db_column='香气', verbose_name='香气')
    lijirose = models.CharField(max_length=30, blank=True, null=True, db_column='鳞茎肉色', verbose_name='鳞茎肉色')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    lijipise = models.CharField(max_length=30, blank=True, null=True, db_column='鳞茎皮色', verbose_name='鳞茎皮色')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    lijizh = models.CharField(max_length=30, blank=True, null=True, db_column='鳞茎重', verbose_name='鳞茎重')
    lawe = models.CharField(max_length=30, blank=True, null=True, db_column='辣味', verbose_name='辣味')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_洋葱'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class manjianghong(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    dofazhxish = models.CharField(max_length=30, blank=True, null=True, db_column='冬繁殖系数', verbose_name='冬繁殖系数')
    fubish = models.CharField(max_length=30, blank=True, null=True, db_column='浮膘数', verbose_name='浮膘数')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    goshqixizh = models.CharField(max_length=30, blank=True, null=True, db_column='共生腔形状', verbose_name='共生腔形状')
    pajikutuqi = models.CharField(max_length=30, blank=True, null=True, db_column='泡胶块突起', verbose_name='泡胶块突起')
    wuyahuerli = models.CharField(max_length=30, blank=True, null=True, db_column='五氧化二磷', verbose_name='五氧化二磷')
    gezh = models.CharField(max_length=30, blank=True, null=True, db_column='根长', verbose_name='根长')
    chgudahuxi = models.CharField(max_length=30, blank=True, null=True, db_column='春固氮活性', verbose_name='春固氮活性')
    xibaguxizh = models.CharField(max_length=30, blank=True, null=True, db_column='小孢果形状', verbose_name='小孢果形状')
    da = models.CharField(max_length=30, blank=True, null=True, db_column='氮', verbose_name='氮')
    bacudaweha = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位号', verbose_name='保存单位号')
    zayixiba = models.CharField(max_length=30, blank=True, null=True, db_column='藻异形胞', verbose_name='藻异形胞')
    dabaguyase = models.CharField(max_length=30, blank=True, null=True, db_column='大孢果颜色', verbose_name='大孢果颜色')
    cixibi = models.CharField(max_length=30, blank=True, null=True, db_column='雌雄比', verbose_name='雌雄比')
    wudajichye = models.CharField(max_length=30, blank=True, null=True, db_column='无氮浸出液', verbose_name='无氮浸出液')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    pitidaxi = models.CharField(max_length=30, blank=True, null=True, db_column='萍体大小', verbose_name='萍体大小')
    shdariqi = models.CharField(max_length=30, blank=True, null=True, db_column='收到日期', verbose_name='收到日期')
    zayiyaba = models.CharField(max_length=30, blank=True, null=True, db_column='藻营养胞', verbose_name='藻营养胞')
    nayixi = models.CharField(max_length=30, blank=True, null=True, db_column='耐阴性', verbose_name='耐阴性')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    beyemituqi = models.CharField(max_length=30, blank=True, null=True, db_column='背叶面突起', verbose_name='背叶面突起')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    dopitiyase = models.CharField(max_length=30, blank=True, null=True, db_column='冬萍体颜色', verbose_name='冬萍体颜色')
    xipitiyase = models.CharField(max_length=30, blank=True, null=True, db_column='夏萍体颜色', verbose_name='夏萍体颜色')
    tuqifebu = models.CharField(max_length=30, blank=True, null=True, db_column='突起分布', verbose_name='突起分布')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    xigudahuxi = models.CharField(max_length=30, blank=True, null=True, db_column='夏固氮活性', verbose_name='夏固氮活性')
    qigudahuxi = models.CharField(max_length=30, blank=True, null=True, db_column='秋固氮活性', verbose_name='秋固氮活性')
    xifazhxish = models.CharField(max_length=30, blank=True, null=True, db_column='夏繁殖系数', verbose_name='夏繁殖系数')
    qipitiyase = models.CharField(max_length=30, blank=True, null=True, db_column='秋萍体颜色', verbose_name='秋萍体颜色')
    yuchdi = models.CharField(max_length=60, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    dabaguxizh = models.CharField(max_length=30, blank=True, null=True, db_column='大孢果形状', verbose_name='大孢果形状')
    cuxiwe = models.CharField(max_length=30, blank=True, null=True, db_column='粗纤维', verbose_name='粗纤维')
    yahuji = models.CharField(max_length=30, blank=True, null=True, db_column='氧化钾', verbose_name='氧化钾')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    fuyeyase = models.CharField(max_length=30, blank=True, null=True, db_column='腹叶颜色', verbose_name='腹叶颜色')
    qifazhxish = models.CharField(max_length=30, blank=True, null=True, db_column='秋繁殖系数', verbose_name='秋繁殖系数')
    beyexizh = models.CharField(max_length=30, blank=True, null=True, db_column='背叶形状', verbose_name='背叶形状')
    nayaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐盐性', verbose_name='耐盐性')
    xibaguyase = models.CharField(max_length=30, blank=True, null=True, db_column='小孢果颜色', verbose_name='小孢果颜色')
    yizhdebiha = models.CharField(max_length=30, blank=True, null=True, db_column='引种地编号', verbose_name='引种地编号')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    hufe = models.CharField(max_length=30, blank=True, null=True, db_column='灰分', verbose_name='灰分')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    jibashqi = models.CharField(max_length=30, blank=True, null=True, db_column='结孢始期', verbose_name='结孢始期')
    pitixizh = models.CharField(max_length=30, blank=True, null=True, db_column='萍体形状', verbose_name='萍体形状')
    jifezhmosh = models.CharField(max_length=30, blank=True, null=True, db_column='茎分枝模式', verbose_name='茎分枝模式')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    chfazhxish = models.CharField(max_length=30, blank=True, null=True, db_column='春繁殖系数', verbose_name='春繁殖系数')
    pizhlayudi = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源地', verbose_name='品种来源地')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    jibalv = models.CharField(max_length=30, blank=True, null=True, db_column='结孢率', verbose_name='结孢率')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')
    chpitiyase = models.CharField(max_length=30, blank=True, null=True, db_column='春萍体颜色', verbose_name='春萍体颜色')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_满江红'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class yancao(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    qikubi = models.CharField(max_length=30, blank=True, null=True, db_column='青枯病', verbose_name='青枯病')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    shmukezh = models.CharField(max_length=30, blank=True, null=True, db_column='施木克值', verbose_name='施木克值')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    zaqi = models.CharField(max_length=30, blank=True, null=True, db_column='杂气', verbose_name='杂气')
    xuyudawe = models.CharField(max_length=30, blank=True, null=True, db_column='选育单位', verbose_name='选育单位')
    jiwe = models.CharField(max_length=30, blank=True, null=True, db_column='茎围', verbose_name='茎围')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    yepihobo = models.CharField(max_length=30, blank=True, null=True, db_column='叶片厚薄', verbose_name='叶片厚薄')
    chwe = models.CharField(max_length=30, blank=True, null=True, db_column='吃味', verbose_name='吃味')
    yizazhkahu = models.CharField(max_length=30, blank=True, null=True, db_column='移栽至开花', verbose_name='移栽至开花')
    zajizuhe = models.CharField(max_length=50, blank=True, null=True, db_column='杂交组合', verbose_name='杂交组合')
    gejixichbi = models.CharField(max_length=30, blank=True, null=True, db_column='根结线虫病', verbose_name='根结线虫病')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='类型', verbose_name='类型')
    hejibi = models.CharField(max_length=30, blank=True, null=True, db_column='黑胫病', verbose_name='黑胫病')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    zota = models.CharField(max_length=30, blank=True, null=True, db_column='总糖', verbose_name='总糖')
    jito = models.CharField(max_length=30, blank=True, null=True, db_column='劲头', verbose_name='劲头')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    ta_ji = models.CharField(db_column='糖／碱', max_length=30, blank=True, null=True, verbose_name='糖／碱')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='灰色', verbose_name='灰色')
    yeji = models.CharField(max_length=30, blank=True, null=True, db_column='叶尖', verbose_name='叶尖')
    hs = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    dabazh = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    cm = models.CharField(db_column='CMV', max_length=30, blank=True, null=True, verbose_name='CMV')
    yaji = models.CharField(max_length=30, blank=True, null=True, db_column='烟碱', verbose_name='烟碱')
    yesh = models.CharField(max_length=30, blank=True, null=True, db_column='叶数', verbose_name='叶数')
    yaya = models.CharField(max_length=30, blank=True, null=True, db_column='烟蚜', verbose_name='烟蚜')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    yebi = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄', verbose_name='叶柄')
    yaqiyaji = models.CharField(max_length=30, blank=True, null=True, db_column='烟气烟碱', verbose_name='烟气烟碱')
    jiju = models.CharField(max_length=30, blank=True, null=True, db_column='节距', verbose_name='节距')
    xiqi = models.CharField(max_length=30, blank=True, null=True, db_column='香气', verbose_name='香气')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶长', verbose_name='叶长')
    huyuta = models.CharField(max_length=30, blank=True, null=True, db_column='还原糖', verbose_name='还原糖')
    rashxi = models.CharField(max_length=30, blank=True, null=True, db_column='燃烧性', verbose_name='燃烧性')
    jiyo = models.CharField(max_length=30, blank=True, null=True, db_column='焦油', verbose_name='焦油')
    yeku = models.CharField(max_length=30, blank=True, null=True, db_column='叶宽', verbose_name='叶宽')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    yepijigo = models.CharField(max_length=30, blank=True, null=True, db_column='叶片结构', verbose_name='叶片结构')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    cijixi = models.CharField(max_length=30, blank=True, null=True, db_column='刺激性', verbose_name='刺激性')
    jiyo_yaji = models.CharField(db_column='焦油／烟碱', max_length=30, blank=True, null=True, verbose_name='焦油／烟碱')
    zoda = models.CharField(max_length=30, blank=True, null=True, db_column='总氮', verbose_name='总氮')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    tuxi = models.CharField(max_length=30, blank=True, null=True, db_column='图象', verbose_name='图象')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_烟草'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class yanmai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    xisx = models.CharField(max_length=30, blank=True, null=True, db_column='小穗形', verbose_name='小穗形')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    sang = models.CharField(max_length=30, blank=True, null=True, db_column='谷氨酸', verbose_name='谷氨酸')
    nefuse = models.CharField(max_length=30, blank=True, null=True, db_column='内稃色', verbose_name='内稃色')
    zolvsu = models.CharField(max_length=30, blank=True, null=True, db_column='棕榈酸', verbose_name='棕榈酸')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    jiansu = models.CharField(max_length=30, blank=True, null=True, db_column='精氨酸', verbose_name='精氨酸')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    zohe = models.CharField(max_length=30, blank=True, null=True, db_column='总和', verbose_name='总和')
    yosu = models.CharField(max_length=30, blank=True, null=True, db_column='油酸', verbose_name='油酸')
    yoxifeni = models.CharField(max_length=30, blank=True, null=True, db_column='有效分蘖', verbose_name='有效分蘖')
    yamasu = models.CharField(max_length=30, blank=True, null=True, db_column='亚麻酸', verbose_name='亚麻酸')
    wafuse = models.CharField(max_length=30, blank=True, null=True, db_column='外稃色', verbose_name='外稃色')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    shyurish = models.CharField(max_length=30, blank=True, null=True, db_column='生育日数', verbose_name='生育日数')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yayosu = models.CharField(max_length=30, blank=True, null=True, db_column='亚油酸', verbose_name='亚油酸')
    yomixixi = models.CharField(max_length=30, blank=True, null=True, db_column='幼苗习性', verbose_name='幼苗习性')
    luku = models.CharField(max_length=30, blank=True, null=True, db_column='卵块', verbose_name='卵块')
    qiyeyexi = models.CharField(max_length=30, blank=True, null=True, db_column='旗叶叶相', verbose_name='旗叶叶相')
    zhzhfasu = models.CharField(max_length=30, blank=True, null=True, db_column='占脂肪酸', verbose_name='占脂肪酸')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zhsuzh = models.CharField(max_length=30, blank=True, null=True, db_column='主穗长', verbose_name='主穗长')
    bebiansu = models.CharField(max_length=30, blank=True, null=True, db_column='苯丙氨酸', verbose_name='苯丙氨酸')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    zhfa = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪', verbose_name='脂肪')
    yueguang = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    zuansu = models.CharField(max_length=30, blank=True, null=True, db_column='组氨酸', verbose_name='组氨酸')
    dafuxi = models.CharField(max_length=30, blank=True, null=True, db_column='倒伏性', verbose_name='倒伏性')
    dabazh = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    mayase = models.CharField(max_length=30, blank=True, null=True, db_column='芒颜色', verbose_name='芒颜色')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    liansu = models.CharField(max_length=30, blank=True, null=True, db_column='亮氨酸', verbose_name='亮氨酸')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    zhsxsush = models.CharField(max_length=30, blank=True, null=True, db_column='主穗小穗数', verbose_name='主穗小穗数')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    hesubilv = models.CharField(max_length=30, blank=True, null=True, db_column='黑穗病率', verbose_name='黑穗病率')
    bubazhfasu = models.CharField(max_length=30, blank=True, null=True, db_column='不饱脂肪酸', verbose_name='不饱脂肪酸')
    gaansu = models.CharField(max_length=30, blank=True, null=True, db_column='甘氨酸', verbose_name='甘氨酸')
    maxizh = models.CharField(max_length=30, blank=True, null=True, db_column='芒形状', verbose_name='芒形状')
    yach = models.CharField(max_length=30, blank=True, null=True, db_column='蚜虫', verbose_name='蚜虫')
    an = models.CharField(max_length=30, blank=True, null=True, db_column='氨', verbose_name='氨')
    yoch = models.CharField(max_length=30, blank=True, null=True, db_column='幼虫', verbose_name='幼虫')
    zhsulizh = models.CharField(max_length=30, blank=True, null=True, db_column='主穗粒重', verbose_name='主穗粒重')
    xiansu = models.CharField(max_length=30, blank=True, null=True, db_column='缬氨酸', verbose_name='缬氨酸')
    hesubikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='黑穗病抗性', verbose_name='黑穗病抗性')
    seansu = models.CharField(max_length=30, blank=True, null=True, db_column='色氨酸', verbose_name='色氨酸')
    dazhlizh = models.CharField(max_length=30, blank=True, null=True, db_column='单株粒重', verbose_name='单株粒重')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    miansu = models.CharField(max_length=30, blank=True, null=True, db_column='酩氨酸', verbose_name='酩氨酸')
    fuansu = models.CharField(max_length=30, blank=True, null=True, db_column='脯氨酸', verbose_name='脯氨酸')
    naias = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    pilu = models.CharField(max_length=30, blank=True, null=True, db_column='皮裸', verbose_name='皮裸')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    yomiyase = models.CharField(max_length=30, blank=True, null=True, db_column='幼苗颜色', verbose_name='幼苗颜色')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒型', verbose_name='粒型')
    kahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱性', verbose_name='抗旱性')
    hoyebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='红叶病抗性', verbose_name='红叶病抗性')
    lucesh = models.CharField(max_length=30, blank=True, null=True, db_column='轮层数', verbose_name='轮层数')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    sx = models.CharField(max_length=30, blank=True, null=True, db_column='穗形', verbose_name='穗形')
    yiliansu = models.CharField(max_length=30, blank=True, null=True, db_column='异亮氨酸', verbose_name='异亮氨酸')
    hoyebibiji = models.CharField(max_length=30, blank=True, null=True, db_column='红叶病病级', verbose_name='红叶病病级')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_燕麦'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class niubang(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    rozhgexi = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根形', verbose_name='肉质根形')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    geroshfe = models.CharField(max_length=30, blank=True, null=True, db_column='根肉水分', verbose_name='根肉水分')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='收获期', verbose_name='收获期')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    rozhgezh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根长', verbose_name='肉质根长')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    gerokoga = models.CharField(max_length=30, blank=True, null=True, db_column='根肉口感', verbose_name='根肉口感')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    shzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='生长期', verbose_name='生长期')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    yecu = models.CharField(max_length=30, blank=True, null=True, db_column='叶簇', verbose_name='叶簇')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    rozhgecu = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根粗', verbose_name='肉质根粗')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    gerozh = models.CharField(max_length=30, blank=True, null=True, db_column='根肉质', verbose_name='根肉质')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    yepizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶片长', verbose_name='叶片长')
    naihanxing = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    yepiku = models.CharField(max_length=30, blank=True, null=True, db_column='叶片宽', verbose_name='叶片宽')
    gepise = models.CharField(max_length=30, blank=True, null=True, db_column='根皮色', verbose_name='根皮色')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    dagezh = models.CharField(max_length=30, blank=True, null=True, db_column='单根重', verbose_name='单根重')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')
    gerose = models.CharField(max_length=30, blank=True, null=True, db_column='根肉色', verbose_name='根肉色')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_牛蒡'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class mucao(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    chsuhuyule = models.CharField(max_length=30, blank=True, null=True, db_column='抽穗或孕蕾', verbose_name='抽穗或孕蕾')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    sozhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='送种单位', verbose_name='送种单位')
    kuhu = models.CharField(max_length=30, blank=True, null=True, db_column='枯黄', verbose_name='枯黄')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    fayalv = models.CharField(max_length=30, blank=True, null=True, db_column='发芽率', verbose_name='发芽率')
    faqiqi = models.CharField(max_length=30, blank=True, null=True, db_column='返青期', verbose_name='返青期')
    xumi = models.CharField(max_length=60, blank=True, null=True, db_column='学名', verbose_name='学名')
    yubiha = models.CharField(max_length=30, blank=True, null=True, db_column='原编号', verbose_name='原编号')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    shyutish = models.CharField(max_length=30, blank=True, null=True, db_column='生育天数', verbose_name='生育天数')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    calilayu = models.CharField(max_length=30, blank=True, null=True, db_column='材料来源', verbose_name='材料来源')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    kahuqi = models.CharField(max_length=30, blank=True, null=True, db_column='开花期', verbose_name='开花期')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    shzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='收种期', verbose_name='收种期')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    caliyuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='材料原产地', verbose_name='材料原产地')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    zhmi = models.CharField(max_length=30, blank=True, null=True, db_column='中名', verbose_name='中名')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_牧草'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class ZuoYuMi(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    tijixibabi = models.CharField(max_length=30, blank=True, null=True, db_column='田间小斑病', verbose_name='田间小斑病')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    xijiyepish = models.CharField(max_length=30, blank=True, null=True, db_column='雄茎叶片数', verbose_name='雄茎叶片数')
    sucu = models.CharField(max_length=30, blank=True, null=True, db_column='穗粗', verbose_name='穗粗')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    zhjiyepish = models.CharField(max_length=30, blank=True, null=True, db_column='主茎叶片数', verbose_name='主茎叶片数')
    yiliansu = models.CharField(max_length=30, blank=True, null=True, db_column='异亮氨酸', verbose_name='异亮氨酸')
    dababiji = models.CharField(max_length=30, blank=True, null=True, db_column='大斑病级', verbose_name='大斑病级')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='类型', verbose_name='类型')
    seansu = models.CharField(max_length=30, blank=True, null=True, db_column='色氨酸', verbose_name='色氨酸')
    shyurish = models.CharField(max_length=30, blank=True, null=True, db_column='生育日数', verbose_name='生育日数')
    dabafayixi = models.CharField(max_length=30, blank=True, null=True, db_column='大斑反应型', verbose_name='大斑反应型')
    yaqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='芽期抗寒', verbose_name='芽期抗寒')
    yayosu = models.CharField(max_length=30, blank=True, null=True, db_column='亚油酸', verbose_name='亚油酸')
    aihuyechbi = models.CharField(max_length=30, blank=True, null=True, db_column='矮花叶成病', verbose_name='矮花叶成病')
    shsulv = models.CharField(max_length=30, blank=True, null=True, db_column='双穗率', verbose_name='双穗率')
    doji = models.CharField(max_length=30, blank=True, null=True, db_column='东经', verbose_name='东经')
    sang = models.CharField(max_length=30, blank=True, null=True, db_column='谷氨酸', verbose_name='谷氨酸')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    sxsh = models.CharField(max_length=30, blank=True, null=True, db_column='穗行数', verbose_name='穗行数')
    bebiansu = models.CharField(max_length=30, blank=True, null=True, db_column='苯丙氨酸', verbose_name='苯丙氨酸')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    aihuyepiji = models.CharField(max_length=30, blank=True, null=True, db_column='矮花叶评价', verbose_name='矮花叶评价')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    dafudu = models.CharField(max_length=30, blank=True, null=True, db_column='倒伏度', verbose_name='倒伏度')
    xisufezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='雄穗分枝数', verbose_name='雄穗分枝数')
    las = models.CharField(max_length=30, blank=True, null=True, db_column='酪氨酸', verbose_name='酪氨酸')
    shqikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟期抗寒性', verbose_name='熟期抗寒性')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    pezhbesh = models.CharField(max_length=30, blank=True, null=True, db_column='膨胀倍数', verbose_name='膨胀倍数')
    balilv = models.CharField(max_length=30, blank=True, null=True, db_column='爆裂率', verbose_name='爆裂率')
    suzh = models.CharField(max_length=30, blank=True, null=True, db_column='穗长', verbose_name='穗长')
    miqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='苗期抗寒', verbose_name='苗期抗寒')
    gujiqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='灌浆期抗寒', verbose_name='灌浆期抗寒')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    sihesupiji = models.CharField(max_length=30, blank=True, null=True, db_column='丝黑穗评价', verbose_name='丝黑穗评价')
    fuansu = models.CharField(max_length=30, blank=True, null=True, db_column='脯氨酸', verbose_name='脯氨酸')
    cuzodife = models.CharField(max_length=30, blank=True, null=True, db_column='粗总淀粉', verbose_name='粗总淀粉')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    xibapiji = models.CharField(max_length=30, blank=True, null=True, db_column='小斑评价', verbose_name='小斑评价')
    tijisihesu = models.CharField(max_length=30, blank=True, null=True, db_column='田间丝黑穗', verbose_name='田间丝黑穗')
    xibabiji = models.CharField(max_length=30, blank=True, null=True, db_column='小斑病级', verbose_name='小斑病级')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    pzname = models.CharField(max_length=50, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    zolvsu = models.CharField(max_length=30, blank=True, null=True, db_column='棕榈酸', verbose_name='棕榈酸')
    hushxisu = models.CharField(max_length=30, blank=True, null=True, db_column='花生稀酸', verbose_name='花生稀酸')
    jiansu = models.CharField(max_length=30, blank=True, null=True, db_column='精氨酸', verbose_name='精氨酸')
    bewe = models.CharField(max_length=30, blank=True, null=True, db_column='北纬', verbose_name='北纬')
    yamasu = models.CharField(max_length=30, blank=True, null=True, db_column='亚麻酸', verbose_name='亚麻酸')
    hefebi = models.CharField(max_length=30, blank=True, null=True, db_column='黑粉病', verbose_name='黑粉病')
    yizhsu = models.CharField(max_length=30, blank=True, null=True, db_column='硬脂酸', verbose_name='硬脂酸')
    dabapiji = models.CharField(max_length=30, blank=True, null=True, db_column='大斑评价', verbose_name='大斑评价')
    liansu = models.CharField(max_length=30, blank=True, null=True, db_column='亮氨酸', verbose_name='亮氨酸')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    guchdidi = models.CharField(max_length=30, blank=True, null=True, db_column='观察地点', verbose_name='观察地点')
    tijihefebi = models.CharField(max_length=30, blank=True, null=True, db_column='田间黑粉病', verbose_name='田间黑粉病')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    diqu = models.CharField(max_length=30, blank=True, null=True, db_column='地区', verbose_name='地区')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    gach = models.CharField(max_length=30, blank=True, null=True, db_column='高程', verbose_name='高程')
    chsirish = models.CharField(max_length=30, blank=True, null=True, db_column='抽丝日数', verbose_name='抽丝日数')
    cystine = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    zuansu = models.CharField(max_length=30, blank=True, null=True, db_column='组氨酸', verbose_name='组氨酸')
    sihesubilv = models.CharField(max_length=30, blank=True, null=True, db_column='丝黑穗病率', verbose_name='丝黑穗病率')
    medoansu = models.CharField(max_length=30, blank=True, null=True, db_column='门冬氨酸', verbose_name='门冬氨酸')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    yosu = models.CharField(max_length=30, blank=True, null=True, db_column='油酸', verbose_name='油酸')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    suwega = models.CharField(max_length=30, blank=True, null=True, db_column='穗位高', verbose_name='穗位高')
    shyufe = models.CharField(max_length=30, blank=True, null=True, db_column='α生育酚', verbose_name='α生育酚')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    xiansu = models.CharField(max_length=30, blank=True, null=True, db_column='缬氨酸', verbose_name='缬氨酸')
    zhse = models.CharField(max_length=30, blank=True, null=True, db_column='轴色', verbose_name='轴色')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    tijidababi = models.CharField(max_length=30, blank=True, null=True, db_column='田间大斑病', verbose_name='田间大斑病')
    gaansu = models.CharField(max_length=30, blank=True, null=True, db_column='甘氨酸', verbose_name='甘氨酸')
    aihuyemibi = models.CharField(max_length=30, blank=True, null=True, db_column='矮花叶苗病', verbose_name='矮花叶苗病')
    qibelayu = models.CharField(max_length=30, blank=True, null=True, db_column='亲本来源', verbose_name='亲本来源')
    naiasan = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    zhle = models.CharField(max_length=30, blank=True, null=True, db_column='种类', verbose_name='种类')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒型', verbose_name='粒型')
    an = models.CharField(max_length=30, blank=True, null=True, db_column='氨', verbose_name='氨')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    sx = models.CharField(max_length=30, blank=True, null=True, db_column='穗形', verbose_name='穗形')
    xipu = models.CharField(max_length=40, blank=True, null=True, db_column='系谱', verbose_name='系谱')
    tahuli = models.CharField(max_length=30, blank=True, null=True, db_column='糖化力', verbose_name='糖化力')
    yexifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='叶锈反应型', verbose_name='叶锈反应型')
    miansu = models.CharField(max_length=30, blank=True, null=True, db_column='酩氨酸', verbose_name='酩氨酸')
    sumidu = models.CharField(max_length=30, blank=True, null=True, db_column='穗密度', verbose_name='穗密度')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    yahazhsh = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害指数', verbose_name='蚜害指数')
    zohe = models.CharField(max_length=30, blank=True, null=True, db_column='总和', verbose_name='总和')
    kahajibi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱级别', verbose_name='抗旱级别')
    chmebibisu = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病病穗', verbose_name='赤霉病病穗')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    xibipiji = models.CharField(max_length=30, blank=True, null=True, db_column='锈病评价', verbose_name='锈病评价')
    tiwebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='条纹病抗性', verbose_name='条纹病抗性')
    tixifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='条锈反应型', verbose_name='条锈反应型')
    xuyufafa = models.CharField(max_length=30, blank=True, null=True, db_column='选育方法', verbose_name='选育方法')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    fenili = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖力', verbose_name='分蘖力')
    gaxiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈严重度', verbose_name='秆锈严重度')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    tiwebibilv = models.CharField(max_length=30, blank=True, null=True, db_column='条纹病病率', verbose_name='条纹病病率')
    ma = models.CharField(max_length=30, blank=True, null=True, db_column='芒', verbose_name='芒')
    yebabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='叶斑病指数', verbose_name='叶斑病指数')
    yaqikanghan = models.CharField(max_length=30, blank=True, null=True, db_column='芽期抗旱', verbose_name='芽期抗旱')
    maxi = models.CharField(max_length=30, blank=True, null=True, db_column='芒性', verbose_name='芒性')
    tijikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='田间抗寒性', verbose_name='田间抗寒性')
    gefubipiji = models.CharField(max_length=30, blank=True, null=True, db_column='根腐病评价', verbose_name='根腐病评价')
    yahabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病评价', verbose_name='蚜害病评价')
    shmichdu = models.CharField(max_length=30, blank=True, null=True, db_column='水敏称度', verbose_name='水敏称度')
    gaxifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈反应型', verbose_name='秆锈反应型')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    sulish = models.CharField(max_length=30, blank=True, null=True, db_column='穗粒数', verbose_name='穗粒数')
    lixing = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    pilu = models.CharField(max_length=30, blank=True, null=True, db_column='皮裸', verbose_name='皮裸')
    kese = models.CharField(max_length=30, blank=True, null=True, db_column='壳色', verbose_name='壳色')
    yahabijibi = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病级别', verbose_name='蚜害病级别')
    yahabiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病级', verbose_name='蚜害病级')
    nalajibi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝级别', verbose_name='耐涝级别')
    chdizh = models.CharField(max_length=30, blank=True, null=True, db_column='沉淀值', verbose_name='沉淀值')
    shqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='熟期抗旱', verbose_name='熟期抗旱')
    chmebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病抗性', verbose_name='赤霉病抗性')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    lengxing = models.CharField(max_length=30, blank=True, null=True, db_column='棱型', verbose_name='棱型')
    bafefayixi = models.CharField(max_length=30, blank=True, null=True, db_column='白粉反应型', verbose_name='白粉反应型')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    huhufabilv = models.CharField(max_length=30, blank=True, null=True, db_column='黄花发病率', verbose_name='黄花发病率')
    dochxi = models.CharField(max_length=30, blank=True, null=True, db_column='冬春性', verbose_name='冬春性')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    qufejichwu = models.CharField(max_length=30, blank=True, null=True, db_column='全粉浸出物', verbose_name='全粉浸出物')
    chmebibizh = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病病指', verbose_name='赤霉病病指')
    dabazh = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    bafebipiji = models.CharField(max_length=30, blank=True, null=True, db_column='白粉病评价', verbose_name='白粉病评价')
    huhuhuhudu = models.CharField(max_length=30, blank=True, null=True, db_column='黄花黄化度', verbose_name='黄花黄化度')
    yuchnixi = models.CharField(max_length=30, blank=True, null=True, db_column='育成年限', verbose_name='育成年限')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    chmebisulv = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病穗率', verbose_name='赤霉病穗率')
    gefusubiji = models.CharField(max_length=30, blank=True, null=True, db_column='根腐穗病级', verbose_name='根腐穗病级')
    zhpiguze = models.CharField(max_length=30, blank=True, null=True, db_column='种皮光泽', verbose_name='种皮光泽')
    xibibiji = models.CharField(max_length=30, blank=True, null=True, db_column='锈病病级', verbose_name='锈病病级')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_玉米'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class qiujingganlan(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    dizhzhshsh = models.CharField(max_length=30, blank=True, null=True, db_column='定植至始收', verbose_name='定植至始收')
    yemilafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶面蜡粉', verbose_name='叶面蜡粉')
    qijixizh = models.CharField(max_length=30, blank=True, null=True, db_column='球茎形状', verbose_name='球茎形状')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    qijizoji = models.CharField(max_length=30, blank=True, null=True, db_column='球茎纵径', verbose_name='球茎纵径')
    dizhqi = models.CharField(max_length=30, blank=True, null=True, db_column='定植期', verbose_name='定植期')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    xumi = models.CharField(max_length=60, blank=True, null=True, db_column='学名', verbose_name='学名')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    yepish = models.CharField(max_length=30, blank=True, null=True, db_column='叶片数', verbose_name='叶片数')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    yecu = models.CharField(max_length=30, blank=True, null=True, db_column='叶簇', verbose_name='叶簇')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    qijipise = models.CharField(max_length=30, blank=True, null=True, db_column='球茎皮色', verbose_name='球茎皮色')
    qijiheji = models.CharField(max_length=30, blank=True, null=True, db_column='球茎横径', verbose_name='球茎横径')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    qijishfe = models.CharField(max_length=30, blank=True, null=True, db_column='球茎水分', verbose_name='球茎水分')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    hannaixing = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='收获期', verbose_name='收获期')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    naihanxing = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    qijizh = models.CharField(max_length=30, blank=True, null=True, db_column='球茎重', verbose_name='球茎重')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_球茎甘蓝'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class hugua(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单瓜重', verbose_name='单瓜重')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    gumilafe = models.CharField(max_length=30, blank=True, null=True, db_column='瓜面腊粉', verbose_name='瓜面腊粉')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜皮色', verbose_name='商瓜皮色')
    lagucise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜次色', verbose_name='老瓜次色')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    lagubawe = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜斑纹', verbose_name='老瓜斑纹')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    lagupise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜皮色', verbose_name='老瓜皮色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='瓜形', verbose_name='瓜形')
    gucidush = models.CharField(max_length=30, blank=True, null=True, db_column='瓜刺多少', verbose_name='瓜刺多少')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    cishhujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='雌首花节位', verbose_name='雌首花节位')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    shgucise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜次色', verbose_name='商瓜次色')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shgubawe = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜斑纹', verbose_name='商瓜斑纹')
    gulexizh = models.CharField(max_length=30, blank=True, null=True, db_column='瓜棱形状', verbose_name='瓜棱形状')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_瓠瓜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class ganzhe(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    qixi = models.CharField(max_length=30, blank=True, null=True, db_column='亲系', verbose_name='亲系')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    kaha = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱', verbose_name='抗旱')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    jiji = models.CharField(max_length=30, blank=True, null=True, db_column='茎径', verbose_name='茎径')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yirushji = models.CharField(max_length=30, blank=True, null=True, db_column='引入时间', verbose_name='引入时间')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    hesubi = models.CharField(max_length=30, blank=True, null=True, db_column='黑穗病', verbose_name='黑穗病')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    chdu = models.CharField(max_length=30, blank=True, null=True, db_column='锤度', verbose_name='锤度')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    miqixixi = models.CharField(max_length=30, blank=True, null=True, db_column='苗期习性', verbose_name='苗期习性')
    yirudawe = models.CharField(max_length=30, blank=True, null=True, db_column='引入单位', verbose_name='引入单位')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yuchdawe = models.CharField(max_length=30, blank=True, null=True, db_column='育成单位', verbose_name='育成单位')
    shqi = models.CharField(max_length=30, blank=True, null=True, db_column='熟期', verbose_name='熟期')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_甘蔗'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class ganshu(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    xicudife = models.CharField(max_length=30, blank=True, null=True, db_column='鲜粗淀粉', verbose_name='鲜粗淀粉')
    sushqubi = models.CharField(max_length=30, blank=True, null=True, db_column='所属群别', verbose_name='所属群别')
    majise = models.CharField(max_length=30, blank=True, null=True, db_column='脉基色', verbose_name='脉基色')
    yemase = models.CharField(max_length=30, blank=True, null=True, db_column='叶脉色', verbose_name='叶脉色')
    nayaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐盐性', verbose_name='耐盐性')
    nazhxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐贮性', verbose_name='耐贮性')
    fezhdush = models.CharField(max_length=30, blank=True, null=True, db_column='分枝多少', verbose_name='分枝多少')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='类型', verbose_name='类型')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    layu = models.CharField(max_length=30, blank=True, null=True, db_column='来源', verbose_name='来源')
    yomishzhsh = models.CharField(max_length=30, blank=True, null=True, db_column='幼苗生长势', verbose_name='幼苗生长势')
    xicudaba = models.CharField(max_length=30, blank=True, null=True, db_column='鲜粗蛋白', verbose_name='鲜粗蛋白')
    yumi = models.CharField(max_length=30, blank=True, null=True, db_column='原名', verbose_name='原名')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yepidaxi = models.CharField(max_length=30, blank=True, null=True, db_column='叶片大小', verbose_name='叶片大小')
    gacudaba = models.CharField(max_length=30, blank=True, null=True, db_column='干粗蛋白', verbose_name='干粗蛋白')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    zuzhmachdu = models.CharField(max_length=30, blank=True, null=True, db_column='最长蔓长短', verbose_name='最长蔓长短')
    jicu = models.CharField(max_length=30, blank=True, null=True, db_column='茎粗', verbose_name='茎粗')
    gakeroxita = models.CharField(max_length=30, blank=True, null=True, db_column='干可溶性糖', verbose_name='干可溶性糖')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    shpise = models.CharField(max_length=30, blank=True, null=True, db_column='薯皮色', verbose_name='薯皮色')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='薯形', verbose_name='薯形')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    chli = models.CharField(max_length=30, blank=True, null=True, db_column='产量', verbose_name='产量')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    zuzhmazh = models.CharField(max_length=30, blank=True, null=True, db_column='最长蔓长', verbose_name='最长蔓长')
    bijise = models.CharField(max_length=30, blank=True, null=True, db_column='柄基色', verbose_name='柄基色')
    diyexi = models.CharField(max_length=30, blank=True, null=True, db_column='顶叶形', verbose_name='顶叶形')
    diyese = models.CharField(max_length=30, blank=True, null=True, db_column='顶叶色', verbose_name='顶叶色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    shwekaxi1 = models.CharField(max_length=30, blank=True, null=True, db_column='薯瘟抗性1', verbose_name='薯瘟抗性1')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    gefubizh = models.CharField(max_length=30, blank=True, null=True, db_column='根腐病指', verbose_name='根腐病指')
    jixichbi = models.CharField(max_length=30, blank=True, null=True, db_column='茎线虫病', verbose_name='茎线虫病')
    shrose = models.CharField(max_length=30, blank=True, null=True, db_column='薯肉色', verbose_name='薯肉色')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    jicudaxi = models.CharField(max_length=30, blank=True, null=True, db_column='茎粗大小', verbose_name='茎粗大小')
    gacudife = models.CharField(max_length=30, blank=True, null=True, db_column='干粗淀粉', verbose_name='干粗淀粉')
    xikeroxita = models.CharField(max_length=30, blank=True, null=True, db_column='鲜可溶性糖', verbose_name='鲜可溶性糖')
    gefubikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='根腐病抗性', verbose_name='根腐病抗性')
    meyaxi = models.CharField(max_length=30, blank=True, null=True, db_column='萌芽性', verbose_name='萌芽性')
    jiduroma = models.CharField(max_length=30, blank=True, null=True, db_column='茎端茸毛', verbose_name='茎端茸毛')
    yepizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶片长', verbose_name='叶片长')
    hogalv = models.CharField(max_length=30, blank=True, null=True, db_column='烘干率', verbose_name='烘干率')
    yepiku = models.CharField(max_length=30, blank=True, null=True, db_column='叶片宽', verbose_name='叶片宽')
    jibufezh = models.CharField(max_length=30, blank=True, null=True, db_column='基部分枝', verbose_name='基部分枝')
    shwekaxi2 = models.CharField(max_length=30, blank=True, null=True, db_column='薯瘟抗性2', verbose_name='薯瘟抗性2')
    yuxiha = models.CharField(max_length=30, blank=True, null=True, db_column='原系号', verbose_name='原系号')
    hebabi = models.CharField(max_length=30, blank=True, null=True, db_column='黑斑病', verbose_name='黑斑病')
    yiliansu = models.CharField(max_length=30, blank=True, null=True, db_column='异亮氨酸', verbose_name='异亮氨酸')
    sush = models.CharField(max_length=30, blank=True, null=True, db_column='所属', verbose_name='所属')
    tahuli = models.CharField(max_length=30, blank=True, null=True, db_column='糖化力', verbose_name='糖化力')
    yexifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='叶锈反应型', verbose_name='叶锈反应型')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    sumidu = models.CharField(max_length=30, blank=True, null=True, db_column='穗密度', verbose_name='穗密度')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    dawebiha = models.CharField(max_length=20, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    dabazh = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    bewe = models.CharField(max_length=30, blank=True, null=True, db_column='北纬', verbose_name='北纬')
    babefesh = models.CharField(max_length=30, blank=True, null=True, db_column='白背飞虱', verbose_name='白背飞虱')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    tiwebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='条纹病抗性', verbose_name='条纹病抗性')
    xiji = models.CharField(max_length=30, blank=True, null=True, db_column='籼粳', verbose_name='籼粳')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    fenili = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖力', verbose_name='分蘖力')
    chmebibisu = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病病穗', verbose_name='赤霉病病穗')
    miwe = models.CharField(max_length=30, blank=True, null=True, db_column='苗瘟', verbose_name='苗瘟')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    tiwebibilv = models.CharField(max_length=30, blank=True, null=True, db_column='条纹病病率', verbose_name='条纹病病率')
    ma = models.CharField(max_length=30, blank=True, null=True, db_column='芒', verbose_name='芒')
    miqinaha = models.CharField(max_length=30, blank=True, null=True, db_column='苗期耐旱', verbose_name='苗期耐旱')
    fuansu = models.CharField(max_length=30, blank=True, null=True, db_column='脯氨酸', verbose_name='脯氨酸')
    kahajibi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱级别', verbose_name='抗旱级别')
    tijikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='田间抗寒性', verbose_name='田间抗寒性')
    jimilv = models.CharField(max_length=30, blank=True, null=True, db_column='精米率', verbose_name='精米率')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    shmichdu = models.CharField(max_length=30, blank=True, null=True, db_column='水敏称度', verbose_name='水敏称度')
    gaxifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈反应型', verbose_name='秆锈反应型')
    zhkubi = models.CharField(max_length=30, blank=True, null=True, db_column='长宽比', verbose_name='长宽比')
    xiansu = models.CharField(max_length=30, blank=True, null=True, db_column='缬氨酸', verbose_name='缬氨酸')
    gach = models.CharField(max_length=30, blank=True, null=True, db_column='高程', verbose_name='高程')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    nalajibi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝级别', verbose_name='耐涝级别')
    chdizh = models.CharField(max_length=30, blank=True, null=True, db_column='沉淀值', verbose_name='沉淀值')
    zazhwa = models.CharField(max_length=30, blank=True, null=True, db_column='早中晚', verbose_name='早中晚')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    chmebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病抗性', verbose_name='赤霉病抗性')
    bacudawe_2 = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位_2', verbose_name='保存单位_2')
    jiase = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    lengxing = models.CharField(max_length=30, blank=True, null=True, db_column='棱型', verbose_name='棱型')
    doji = models.CharField(max_length=30, blank=True, null=True, db_column='东经', verbose_name='东经')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    huhufabilv = models.CharField(max_length=30, blank=True, null=True, db_column='黄花发病率', verbose_name='黄花发病率')
    dochxi = models.CharField(max_length=30, blank=True, null=True, db_column='冬春性', verbose_name='冬春性')
    yijiwazh = models.CharField(db_column="颖尖弯直'", max_length=30, blank=True, null=True, verbose_name='颖尖弯直')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    qufejichwu = models.CharField(max_length=30, blank=True, null=True, db_column='全粉浸出物', verbose_name='全粉浸出物')
    yingjianwazh = models.CharField(max_length=30, blank=True, null=True, db_column='颖尖弯直', verbose_name='颖尖弯直')
    las = models.CharField(max_length=30, blank=True, null=True, db_column='酪氨酸', verbose_name='酪氨酸')
    kese = models.CharField(max_length=30, blank=True, null=True, db_column='壳色', verbose_name='壳色')
    mazh = models.CharField(max_length=30, blank=True, null=True, db_column='芒长', verbose_name='芒长')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    gefusubiji = models.CharField(max_length=30, blank=True, null=True, db_column='根腐穗病级', verbose_name='根腐穗病级')
    camilv = models.CharField(max_length=30, blank=True, null=True, db_column='糙米率', verbose_name='糙米率')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_甘薯'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class tiangua(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    gucidush = models.CharField(max_length=30, blank=True, null=True, db_column='瓜刺多少', verbose_name='瓜刺多少')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单瓜重', verbose_name='单瓜重')
    shgucise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜次色', verbose_name='商瓜次色')
    lagupise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜皮色', verbose_name='老瓜皮色')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    jiguxixi = models.CharField(max_length=30, blank=True, null=True, db_column='结瓜习性', verbose_name='结瓜习性')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='瓜形', verbose_name='瓜形')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    gumilafe = models.CharField(max_length=30, blank=True, null=True, db_column='瓜面腊粉', verbose_name='瓜面腊粉')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    gulexizh = models.CharField(max_length=30, blank=True, null=True, db_column='瓜棱形状', verbose_name='瓜棱形状')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    lagubawe = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜斑纹', verbose_name='老瓜斑纹')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜皮色', verbose_name='商瓜皮色')
    lagucise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜次色', verbose_name='老瓜次色')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    shgubawe = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜斑纹', verbose_name='商瓜斑纹')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_甜瓜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class tiancai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    lazhhobo = models.CharField(max_length=30, blank=True, null=True, db_column='蜡质厚薄', verbose_name='蜡质厚薄')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    ziyemiji = models.CharField(max_length=30, blank=True, null=True, db_column='子叶面积', verbose_name='子叶面积')
    nahali = models.CharField(max_length=30, blank=True, null=True, db_column='钠含量', verbose_name='钠含量')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yegamizhji = models.CharField(max_length=30, blank=True, null=True, db_column='叶盖面直径', verbose_name='叶盖面直径')
    zhzichli = models.CharField(max_length=30, blank=True, null=True, db_column='种子产量', verbose_name='种子产量')
    rasetibexi = models.CharField(max_length=30, blank=True, null=True, db_column='染色体倍性', verbose_name='染色体倍性')
    zhzichshqi = models.CharField(max_length=30, blank=True, null=True, db_column='种子成熟期', verbose_name='种子成熟期')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒性', verbose_name='粒性')
    kahushqi = models.CharField(max_length=30, blank=True, null=True, db_column='开花盛期', verbose_name='开花盛期')
    bafebi = models.CharField(max_length=30, blank=True, null=True, db_column='白粉病', verbose_name='白粉病')
    getodaxi = models.CharField(max_length=30, blank=True, null=True, db_column='根头大小', verbose_name='根头大小')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    chtashqi = models.CharField(max_length=30, blank=True, null=True, db_column='抽苔盛期', verbose_name='抽苔盛期')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    gegoshqi = models.CharField(max_length=30, blank=True, null=True, db_column='根沟深浅', verbose_name='根沟深浅')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='类型', verbose_name='类型')
    danichtalv = models.CharField(max_length=30, blank=True, null=True, db_column='当年抽苔率', verbose_name='当年抽苔率')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    rozhcuxi = models.CharField(max_length=30, blank=True, null=True, db_column='肉质粗细', verbose_name='肉质粗细')
    yuxi = models.CharField(max_length=30, blank=True, null=True, db_column='育性', verbose_name='育性')
    zhtachli = models.CharField(max_length=30, blank=True, null=True, db_column='蔗糖产量', verbose_name='蔗糖产量')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    huhudubi = models.CharField(max_length=30, blank=True, null=True, db_column='黄花毒病', verbose_name='黄花毒病')
    yebiku = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄宽', verbose_name='叶柄宽')
    kugeshdu = models.CharField(max_length=30, blank=True, null=True, db_column='块根深度', verbose_name='块根深度')
    gugatululv = models.CharField(max_length=30, blank=True, null=True, db_column='果盖脱落率', verbose_name='果盖脱落率')
    chshlvye = models.CharField(max_length=30, blank=True, null=True, db_column='处署绿叶', verbose_name='处署绿叶')
    zhzichshdu = models.CharField(max_length=30, blank=True, null=True, db_column='种子成熟度', verbose_name='种子成熟度')
    yemixizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶面形状', verbose_name='叶面形状')
    kugexizh = models.CharField(max_length=30, blank=True, null=True, db_column='块根形状', verbose_name='块根形状')
    yomibazhzh = models.CharField(max_length=30, blank=True, null=True, db_column='幼苗百株重', verbose_name='幼苗百株重')
    jihali = models.CharField(max_length=30, blank=True, null=True, db_column='钾含量', verbose_name='钾含量')
    zhzifayalv = models.CharField(max_length=30, blank=True, null=True, db_column='种子发芽率', verbose_name='种子发芽率')
    hufeli = models.CharField(max_length=30, blank=True, null=True, db_column='花粉量', verbose_name='花粉量')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    ziyedaxi = models.CharField(max_length=30, blank=True, null=True, db_column='子叶大小', verbose_name='子叶大小')
    chshkuye = models.CharField(max_length=30, blank=True, null=True, db_column='处署枯叶', verbose_name='处署枯叶')
    hebabi = models.CharField(max_length=30, blank=True, null=True, db_column='褐斑病', verbose_name='褐斑病')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    dalilv = models.CharField(max_length=30, blank=True, null=True, db_column='单粒率', verbose_name='单粒率')
    jishmidu = models.CharField(max_length=30, blank=True, null=True, db_column='结实密度', verbose_name='结实密度')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    miqishzhsh = models.CharField(max_length=30, blank=True, null=True, db_column='苗期生长势', verbose_name='苗期生长势')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    zhzhzhxi = models.CharField(max_length=30, blank=True, null=True, db_column='种株株型', verbose_name='种株株型')
    dahali = models.CharField(max_length=30, blank=True, null=True, db_column='氮含量', verbose_name='氮含量')
    yecoxi = models.CharField(max_length=30, blank=True, null=True, db_column='叶丛型', verbose_name='叶丛型')
    gefubi = models.CharField(max_length=30, blank=True, null=True, db_column='根腐病', verbose_name='根腐病')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yerohobo = models.CharField(max_length=30, blank=True, null=True, db_column='叶肉厚薄', verbose_name='叶肉厚薄')
    zhtahali = models.CharField(max_length=30, blank=True, null=True, db_column='蔗糖含量', verbose_name='蔗糖含量')
    yeyuxi = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘形', verbose_name='叶缘形')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    wegushhush = models.CharField(max_length=30, blank=True, null=True, db_column='维管束环数', verbose_name='维管束环数')
    geyebizh = models.CharField(max_length=30, blank=True, null=True, db_column='根叶比值', verbose_name='根叶比值')
    yebizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄长', verbose_name='叶柄长')
    xipezhse = models.CharField(max_length=30, blank=True, null=True, db_column='下胚轴色', verbose_name='下胚轴色')
    yemidumaxi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面多毛性', verbose_name='叶面多毛性')
    jiyechli = models.CharField(max_length=30, blank=True, null=True, db_column='茎叶产量', verbose_name='茎叶产量')
    jijilexi = models.CharField(max_length=30, blank=True, null=True, db_column='经济类型', verbose_name='经济类型')
    zhzidalilv = models.CharField(max_length=30, blank=True, null=True, db_column='种子单粒率', verbose_name='种子单粒率')
    kugechlidu = models.CharField(max_length=30, blank=True, null=True, db_column='块根产量吨', verbose_name='块根产量吨')
    kugechli = models.CharField(max_length=30, blank=True, null=True, db_column='块根产量', verbose_name='块根产量')
    buyulv = models.CharField(max_length=30, blank=True, null=True, db_column='不育率', verbose_name='不育率')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    chtalv = models.CharField(max_length=30, blank=True, null=True, db_column='抽苔率', verbose_name='抽苔率')
    yesh = models.CharField(max_length=30, blank=True, null=True, db_column='叶数', verbose_name='叶数')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    gepiguhu = models.CharField(max_length=30, blank=True, null=True, db_column='根皮光滑', verbose_name='根皮光滑')
    chmishqi = models.CharField(max_length=30, blank=True, null=True, db_column='出苗盛期', verbose_name='出苗盛期')
    zhtachlidu = models.CharField(max_length=30, blank=True, null=True, db_column='蔗糖产量吨', verbose_name='蔗糖产量吨')
    gerose = models.CharField(max_length=30, blank=True, null=True, db_column='根肉色', verbose_name='根肉色')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_甜菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class fanqie(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    gumitezh = models.CharField(max_length=30, blank=True, null=True, db_column='果面特征', verbose_name='果面特征')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    shhujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='始花节位', verbose_name='始花节位')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    chshgupise = models.CharField(max_length=30, blank=True, null=True, db_column='成熟果皮色', verbose_name='成熟果皮色')
    guqidaxi = models.CharField(max_length=30, blank=True, null=True, db_column='果脐大小', verbose_name='果脐大小')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单果重', verbose_name='单果重')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶型', verbose_name='叶型')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    gurose = models.CharField(max_length=30, blank=True, null=True, db_column='果肉色', verbose_name='果肉色')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_番茄'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class baicai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    xumi = models.CharField(max_length=60, blank=True, null=True, db_column='学名', verbose_name='学名')
    hannaixing = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    yebiku = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄宽', verbose_name='叶柄宽')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    yebizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄长', verbose_name='叶柄长')
    yeku = models.CharField(max_length=30, blank=True, null=True, db_column='叶宽', verbose_name='叶宽')
    yelike = models.CharField(max_length=30, blank=True, null=True, db_column='叶裂刻', verbose_name='叶裂刻')
    naihanxing = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    dazhzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株重', verbose_name='单株重')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    xiwehali = models.CharField(max_length=30, blank=True, null=True, db_column='纤维含量', verbose_name='纤维含量')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    yezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶长', verbose_name='叶长')
    yemicima = models.CharField(max_length=30, blank=True, null=True, db_column='叶面刺毛', verbose_name='叶面刺毛')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='收获期', verbose_name='收获期')
    yebiho = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄厚', verbose_name='叶柄厚')
    dizhqi = models.CharField(max_length=30, blank=True, null=True, db_column='定植期', verbose_name='定植期')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    shzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='生长期', verbose_name='生长期')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_白菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class shidiaobai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yaxi = models.CharField(max_length=30, blank=True, null=True, db_column='芽形', verbose_name='芽形')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_石刁柏'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class sungua(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单瓜重', verbose_name='单瓜重')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    gumilafe = models.CharField(max_length=30, blank=True, null=True, db_column='瓜面腊粉', verbose_name='瓜面腊粉')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜皮色', verbose_name='商瓜皮色')
    lagucise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜次色', verbose_name='老瓜次色')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    lagubawe = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜斑纹', verbose_name='老瓜斑纹')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    lagupise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜皮色', verbose_name='老瓜皮色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='瓜形', verbose_name='瓜形')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    cishhujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='雌首花节位', verbose_name='雌首花节位')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    shgucise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜次色', verbose_name='商瓜次色')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shgubawe = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜斑纹', verbose_name='商瓜斑纹')
    gulexizh = models.CharField(max_length=30, blank=True, null=True, db_column='瓜棱形状', verbose_name='瓜棱形状')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_笋瓜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class zilixian(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    zhhuxuchdu = models.CharField(max_length=30, blank=True, null=True, db_column='主花序长度', verbose_name='主花序长度')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    huxuse = models.CharField(max_length=30, blank=True, null=True, db_column='花序色', verbose_name='花序色')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    lebi = models.CharField(max_length=30, blank=True, null=True, db_column='类别', verbose_name='类别')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    layudi = models.CharField(max_length=30, blank=True, null=True, db_column='来源地', verbose_name='来源地')
    huxuxi = models.CharField(max_length=30, blank=True, null=True, db_column='花序性', verbose_name='花序性')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    xipu = models.CharField(max_length=30, blank=True, null=True, db_column='系谱', verbose_name='系谱')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    qita = models.CharField(max_length=30, blank=True, null=True, db_column='其它', verbose_name='其它')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_籽粒苋'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class zisu(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    yeji = models.CharField(max_length=30, blank=True, null=True, db_column='叶角', verbose_name='叶角')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_紫苏'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class honghua(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    zhzihayolv = models.CharField(max_length=30, blank=True, null=True, db_column='种子含油率', verbose_name='种子含油率')
    chdihulayu = models.CharField(max_length=30, blank=True, null=True, db_column='产地或来源', verbose_name='产地或来源')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    dazhguqish = models.CharField(max_length=30, blank=True, null=True, db_column='单株果球数', verbose_name='单株果球数')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    kexi = models.CharField(max_length=30, blank=True, null=True, db_column='壳型', verbose_name='壳型')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    chmiqi = models.CharField(max_length=30, blank=True, null=True, db_column='出苗期', verbose_name='出苗期')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yayosu = models.CharField(max_length=30, blank=True, null=True, db_column='亚油酸', verbose_name='亚油酸')
    pikelv = models.CharField(max_length=30, blank=True, null=True, db_column='皮壳率', verbose_name='皮壳率')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    bapiyowuci = models.CharField(max_length=30, blank=True, null=True, db_column='苞片有无刺', verbose_name='苞片有无刺')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    yepiyowuci = models.CharField(max_length=30, blank=True, null=True, db_column='叶片有无刺', verbose_name='叶片有无刺')
    xuyufafa = models.CharField(max_length=30, blank=True, null=True, db_column='选育方法', verbose_name='选育方法')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_红花'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class hongma(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    zhjimazh = models.CharField(max_length=30, blank=True, null=True, db_column='株精麻重', verbose_name='株精麻重')
    tajubi = models.CharField(max_length=30, blank=True, null=True, db_column='炭疽病', verbose_name='炭疽病')
    gejixichbi = models.CharField(max_length=30, blank=True, null=True, db_column='根结线虫病', verbose_name='根结线虫病')
    zhjise = models.CharField(max_length=30, blank=True, null=True, db_column='中茎色', verbose_name='中茎色')
    xiwemuch = models.CharField(max_length=30, blank=True, null=True, db_column='纤维亩产', verbose_name='纤维亩产')
    zhxijizh = models.CharField(max_length=30, blank=True, null=True, db_column='株鲜茎重', verbose_name='株鲜茎重')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    kahuqi = models.CharField(max_length=30, blank=True, null=True, db_column='开花期', verbose_name='开花期')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    shzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='收种期', verbose_name='收种期')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    chmiqi = models.CharField(max_length=30, blank=True, null=True, db_column='出苗期', verbose_name='出苗期')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    huese = models.CharField(max_length=30, blank=True, null=True, db_column='花萼色', verbose_name='花萼色')
    zhqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种千粒重', verbose_name='种千粒重')
    yumamuch = models.CharField(max_length=30, blank=True, null=True, db_column='原麻亩产', verbose_name='原麻亩产')
    huguse = models.CharField(max_length=30, blank=True, null=True, db_column='花冠色', verbose_name='花冠色')
    lali = models.CharField(max_length=30, blank=True, null=True, db_column='拉力', verbose_name='拉力')
    jicu = models.CharField(max_length=30, blank=True, null=True, db_column='茎粗', verbose_name='茎粗')
    xileqi = models.CharField(max_length=30, blank=True, null=True, db_column='现蕾期', verbose_name='现蕾期')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    zhyumazh = models.CharField(max_length=30, blank=True, null=True, db_column='株原麻重', verbose_name='株原麻重')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    zhgapizh = models.CharField(max_length=30, blank=True, null=True, db_column='株干皮重', verbose_name='株干皮重')
    mijise = models.CharField(max_length=30, blank=True, null=True, db_column='苗茎色', verbose_name='苗茎色')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    zhsh = models.CharField(max_length=30, blank=True, null=True, db_column='支数', verbose_name='支数')
    huhose = models.CharField(max_length=30, blank=True, null=True, db_column='花喉色', verbose_name='花喉色')
    xipiho = models.CharField(max_length=30, blank=True, null=True, db_column='鲜皮厚', verbose_name='鲜皮厚')
    qushyutish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育天数', verbose_name='全生育天数')
    hojise = models.CharField(max_length=30, blank=True, null=True, db_column='后茎色', verbose_name='后茎色')
    gapijimalv = models.CharField(max_length=30, blank=True, null=True, db_column='干皮精麻率', verbose_name='干皮精麻率')
    zhxipizh = models.CharField(max_length=30, blank=True, null=True, db_column='株鲜皮重', verbose_name='株鲜皮重')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    xiweshhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='纤维收获期', verbose_name='纤维收获期')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    shzhtish = models.CharField(max_length=30, blank=True, null=True, db_column='生长天数', verbose_name='生长天数')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    jimamuch = models.CharField(max_length=30, blank=True, null=True, db_column='精麻亩产', verbose_name='精麻亩产')
    hugudaxi = models.CharField(max_length=30, blank=True, null=True, db_column='花冠大小', verbose_name='花冠大小')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    xijigapilv = models.CharField(max_length=30, blank=True, null=True, db_column='鲜茎干皮率', verbose_name='鲜茎干皮率')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶型', verbose_name='叶型')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_红麻'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class jieqiuganlan(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    dizhzhshsh = models.CharField(max_length=30, blank=True, null=True, db_column='定植至始收', verbose_name='定植至始收')
    yemilafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶面蜡粉', verbose_name='叶面蜡粉')
    yeqizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶球重', verbose_name='叶球重')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    wayese = models.CharField(max_length=30, blank=True, null=True, db_column='外叶色', verbose_name='外叶色')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    yeqiheji = models.CharField(max_length=30, blank=True, null=True, db_column='叶球横径', verbose_name='叶球横径')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='收获期', verbose_name='收获期')
    hanhaixing = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    yeqijishdu = models.CharField(max_length=30, blank=True, null=True, db_column='叶球紧实度', verbose_name='叶球紧实度')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    xumi = models.CharField(max_length=60, blank=True, null=True, db_column='学名', verbose_name='学名')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    xiwehali = models.CharField(max_length=30, blank=True, null=True, db_column='纤维含量', verbose_name='纤维含量')
    wayexi = models.CharField(max_length=30, blank=True, null=True, db_column='外叶形', verbose_name='外叶形')
    naihanxing = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    dizhqi = models.CharField(max_length=30, blank=True, null=True, db_column='定植期', verbose_name='定植期')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    yeqixizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶球形状', verbose_name='叶球形状')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    yeqidaxi = models.CharField(max_length=30, blank=True, null=True, db_column='叶球大小', verbose_name='叶球大小')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yeqise = models.CharField(max_length=30, blank=True, null=True, db_column='叶球色', verbose_name='叶球色')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    qizhxizhga = models.CharField(max_length=30, blank=True, null=True, db_column='球中心柱高', verbose_name='球中心柱高')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    yeqizoji = models.CharField(max_length=30, blank=True, null=True, db_column='叶球纵径', verbose_name='叶球纵径')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_结球甘蓝'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class lvfei(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    lijixi = models.CharField(max_length=30, blank=True, null=True, db_column='裂荚性', verbose_name='裂荚性')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    zhzilayudi = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源地', verbose_name='种子来源地')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    xicachli = models.CharField(max_length=30, blank=True, null=True, db_column='鲜草产量', verbose_name='鲜草产量')
    qise = models.CharField(max_length=30, blank=True, null=True, db_column='脐色', verbose_name='脐色')
    wuyahuerli = models.CharField(max_length=30, blank=True, null=True, db_column='五氧化二磷', verbose_name='五氧化二磷')
    naiashxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐湿性', verbose_name='耐湿性')
    ziyechtu = models.CharField(max_length=30, blank=True, null=True, db_column='子叶出土', verbose_name='子叶出土')
    bozhdidi = models.CharField(max_length=30, blank=True, null=True, db_column='播种地点', verbose_name='播种地点')
    chhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='初花期', verbose_name='初花期')
    jixi = models.CharField(max_length=30, blank=True, null=True, db_column='茎形', verbose_name='茎形')
    jishzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='茎生长习性', verbose_name='茎生长习性')
    hogalv = models.CharField(max_length=30, blank=True, null=True, db_column='烘干率', verbose_name='烘干率')
    dazhfezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='单株分枝数', verbose_name='单株分枝数')
    huxulexi = models.CharField(max_length=30, blank=True, null=True, db_column='花序类型', verbose_name='花序类型')
    chshjise = models.CharField(max_length=30, blank=True, null=True, db_column='成熟荚色', verbose_name='成熟荚色')
    nayixi = models.CharField(max_length=30, blank=True, null=True, db_column='耐荫性', verbose_name='耐荫性')
    jidexizh = models.CharField(max_length=30, blank=True, null=True, db_column='茎的性质', verbose_name='茎的性质')
    zapelebi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培类别', verbose_name='栽培类别')
    chshyexi = models.CharField(max_length=30, blank=True, null=True, db_column='初生叶形', verbose_name='初生叶形')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    yojise = models.CharField(max_length=30, blank=True, null=True, db_column='幼茎色', verbose_name='幼茎色')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    lujixi = models.CharField(max_length=30, blank=True, null=True, db_column='落荚性', verbose_name='落荚性')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    najixi = models.CharField(max_length=30, blank=True, null=True, db_column='耐瘠性', verbose_name='耐瘠性')
    chmiqi = models.CharField(max_length=30, blank=True, null=True, db_column='出苗期', verbose_name='出苗期')
    xumi = models.CharField(max_length=50, blank=True, null=True, db_column='学名', verbose_name='学名')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    nayaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐盐性', verbose_name='耐盐性')
    naiasx = models.CharField(max_length=30, blank=True, null=True, db_column='耐酸性', verbose_name='耐酸性')
    luyexi = models.CharField(max_length=30, blank=True, null=True, db_column='落叶性', verbose_name='落叶性')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    zhpise = models.CharField(max_length=30, blank=True, null=True, db_column='种皮色', verbose_name='种皮色')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    zashxi = models.CharField(max_length=30, blank=True, null=True, db_column='再生性', verbose_name='再生性')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    njx = models.CharField(max_length=30, blank=True, null=True, db_column='耐碱性', verbose_name='耐碱性')
    jijigadu = models.CharField(max_length=30, blank=True, null=True, db_column='结荚高度', verbose_name='结荚高度')
    yeji = models.CharField(max_length=30, blank=True, null=True, db_column='叶尖', verbose_name='叶尖')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yahuji = models.CharField(max_length=30, blank=True, null=True, db_column='氧化钾', verbose_name='氧化钾')
    jia_xing = models.CharField(max_length=30, blank=True, null=True, db_column='荚形', verbose_name='荚形')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='盛花期', verbose_name='盛花期')
    fuyelexi = models.CharField(max_length=30, blank=True, null=True, db_column='复叶类形', verbose_name='复叶类形')
    yexu = models.CharField(max_length=30, blank=True, null=True, db_column='叶序', verbose_name='叶序')
    dazhlish = models.CharField(max_length=30, blank=True, null=True, db_column='单株粒数', verbose_name='单株粒数')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    da = models.CharField(max_length=30, blank=True, null=True, db_column='氮', verbose_name='氮')
    shyutish = models.CharField(max_length=30, blank=True, null=True, db_column='生育天数', verbose_name='生育天数')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗寒性', verbose_name='抗寒性')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    fazhxish = models.CharField(max_length=30, blank=True, null=True, db_column='繁殖系数', verbose_name='繁殖系数')
    khx= models.CharField(max_length=30, blank=True, null=True, db_column='抗旱性', verbose_name='抗旱性')
    shhuzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='生活周期', verbose_name='生活周期')
    yj = models.CharField(max_length=30, blank=True, null=True, db_column='叶基', verbose_name='叶基')
    ziyeyase = models.CharField(max_length=30, blank=True, null=True, db_column='子叶颜色', verbose_name='子叶颜色')
    zhzichli = models.CharField(max_length=30, blank=True, null=True, db_column='种子产量', verbose_name='种子产量')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_绿肥'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class lvdou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    yebabiji = models.CharField(max_length=30, blank=True, null=True, db_column='叶斑病级', verbose_name='叶斑病级')
    sang = models.CharField(max_length=30, blank=True, null=True, db_column='谷氨酸', verbose_name='谷氨酸')
    xuyudawe = models.CharField(max_length=30, blank=True, null=True, db_column='选育单位', verbose_name='选育单位')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    xiansu = models.CharField(max_length=30, blank=True, null=True, db_column='缬氨酸', verbose_name='缬氨酸')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    jiansu = models.CharField(max_length=30, blank=True, null=True, db_column='精氨酸', verbose_name='精氨酸')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    zohe = models.CharField(max_length=30, blank=True, null=True, db_column='总和', verbose_name='总和')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    yiliansu = models.CharField(max_length=30, blank=True, null=True, db_column='异亮氨酸', verbose_name='异亮氨酸')
    gefubiji = models.CharField(max_length=30, blank=True, null=True, db_column='根腐病级', verbose_name='根腐病级')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    zhfa = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪', verbose_name='脂肪')
    zuansu = models.CharField(max_length=30, blank=True, null=True, db_column='组氨酸', verbose_name='组氨酸')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    gefubizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='根腐病指数', verbose_name='根腐病指数')
    seansu = models.CharField(max_length=30, blank=True, null=True, db_column='色氨酸', verbose_name='色氨酸')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yaqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='芽期抗旱', verbose_name='芽期抗旱')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    xuyufafa = models.CharField(max_length=30, blank=True, null=True, db_column='选育方法', verbose_name='选育方法')
    bebiansu = models.CharField(max_length=30, blank=True, null=True, db_column='苯丙氨酸', verbose_name='苯丙氨酸')
    shqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='熟期抗旱', verbose_name='熟期抗旱')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    dabazh = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    miqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='苗期耐盐', verbose_name='苗期耐盐')
    zhpiguze = models.CharField(max_length=30, blank=True, null=True, db_column='种皮光泽', verbose_name='种皮光泽')
    liansu = models.CharField(max_length=30, blank=True, null=True, db_column='亮氨酸', verbose_name='亮氨酸')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yahazhsh = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害指数', verbose_name='蚜害指数')
    gaansu = models.CharField(max_length=30, blank=True, null=True, db_column='甘氨酸', verbose_name='甘氨酸')
    dajilish = models.CharField(max_length=30, blank=True, null=True, db_column='单荚粒数', verbose_name='单荚粒数')
    yahabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病评价', verbose_name='蚜害病评价')
    gas = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    yaqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='芽期耐盐', verbose_name='芽期耐盐')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    yuchnife = models.CharField(max_length=30, blank=True, null=True, db_column='育成年份', verbose_name='育成年份')
    miansu = models.CharField(max_length=30, blank=True, null=True, db_column='酩氨酸', verbose_name='酩氨酸')
    gefubipiji = models.CharField(max_length=30, blank=True, null=True, db_column='根腐病评价', verbose_name='根腐病评价')
    fuansu = models.CharField(max_length=30, blank=True, null=True, db_column='脯氨酸', verbose_name='脯氨酸')
    yebabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='叶斑病指数', verbose_name='叶斑病指数')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    naias = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    yahabijibi = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病级别', verbose_name='蚜害病级别')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    yahabizh = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害比值', verbose_name='蚜害比值')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    yebabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='叶斑病评价', verbose_name='叶斑病评价')
    lixing = models.CharField(max_length=30, blank=True, null=True, db_column='粒型', verbose_name='粒型')
    hebabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='褐斑病指数', verbose_name='褐斑病指数')
    xibipiji = models.CharField(max_length=30, blank=True, null=True, db_column='锈病评价', verbose_name='锈病评价')
    yahabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病指数', verbose_name='蚜害病指数')
    juyudu = models.CharField(max_length=30, blank=True, null=True, db_column='均匀度', verbose_name='均匀度')
    chbabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='赤斑病指数', verbose_name='赤斑病指数')
    yahabiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病级', verbose_name='蚜害病级')
    kalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗涝性', verbose_name='抗涝性')
    chbabiji = models.CharField(max_length=30, blank=True, null=True, db_column='赤斑病级', verbose_name='赤斑病级')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    yoxizh = models.CharField(max_length=30, blank=True, null=True, db_column='有效枝', verbose_name='有效枝')
    xibizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='锈病指数', verbose_name='锈病指数')
    jiku = models.CharField(max_length=30, blank=True, null=True, db_column='荚宽', verbose_name='荚宽')
    hebabiji = models.CharField(max_length=30, blank=True, null=True, db_column='褐斑病级', verbose_name='褐斑病级')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    chbabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='赤斑病评价', verbose_name='赤斑病评价')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_绿豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class luole(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶长', verbose_name='叶长')
    yeku = models.CharField(max_length=30, blank=True, null=True, db_column='叶宽', verbose_name='叶宽')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_罗勒'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class hujiao(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    hufayohali = models.CharField(max_length=30, blank=True, null=True, db_column='挥发油含量', verbose_name='挥发油含量')
    daweguzhsh = models.CharField(max_length=30, blank=True, null=True, db_column='单位果枝数', verbose_name='单位果枝数')
    husuchdu = models.CharField(max_length=30, blank=True, null=True, db_column='花穗长度', verbose_name='花穗长度')
    pijig = models.CharField(db_column='评价G', max_length=30, blank=True, null=True, verbose_name='评价G')
    cuzhfahali = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪含量', verbose_name='粗脂肪含量')
    piji = models.CharField(db_column='评价E', max_length=30, blank=True, null=True, verbose_name='评价E')
    zhxushli = models.CharField(max_length=30, blank=True, null=True, db_column='枝序数量', verbose_name='枝序数量')
    yimitiquwu = models.CharField(max_length=30, blank=True, null=True, db_column='乙醚提取物', verbose_name='乙醚提取物')
    hufehali = models.CharField(max_length=30, blank=True, null=True, db_column='灰份含量', verbose_name='灰份含量')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    gaxibi = models.CharField(max_length=30, blank=True, null=True, db_column='干鲜比', verbose_name='干鲜比')
    shfehali = models.CharField(max_length=30, blank=True, null=True, db_column='水分含量', verbose_name='水分含量')
    pijia = models.CharField(db_column='评价A', max_length=30, blank=True, null=True, verbose_name='评价A')
    pijic = models.CharField(db_column='评价C', max_length=30, blank=True, null=True, verbose_name='评价C')
    gufudaxi = models.CharField(max_length=30, blank=True, null=True, db_column='冠幅大小', verbose_name='冠幅大小')
    ziliqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='籽粒千粒重', verbose_name='籽粒千粒重')
    zugazhch = models.CharField(max_length=30, blank=True, null=True, db_column='最高株产', verbose_name='最高株产')
    pijib = models.CharField(db_column='评价B', max_length=30, blank=True, null=True, verbose_name='评价B')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    zhzhmich = models.CharField(max_length=30, blank=True, null=True, db_column='种质名称', verbose_name='种质名称')
    chgulv = models.CharField(max_length=30, blank=True, null=True, db_column='成果率', verbose_name='成果率')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    biqizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='病情指数', verbose_name='病情指数')
    xigujicu = models.CharField(max_length=30, blank=True, null=True, db_column='鲜果径粗', verbose_name='鲜果径粗')
    zhch = models.CharField(max_length=30, blank=True, null=True, db_column='株产', verbose_name='株产')
    fpijia = models.CharField(db_column='评价F', max_length=30, blank=True, null=True, verbose_name='评价F')
    zhzhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='种质来源', verbose_name='种质来源')
    kawebineli = models.CharField(max_length=30, blank=True, null=True, db_column='抗瘟病能力', verbose_name='抗瘟病能力')
    zhzijicu = models.CharField(max_length=30, blank=True, null=True, db_column='种子径粗', verbose_name='种子径粗')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    difehali = models.CharField(max_length=30, blank=True, null=True, db_column='淀粉含量', verbose_name='淀粉含量')
    cudabahali = models.CharField(max_length=30, blank=True, null=True, db_column='粗旦白含量', verbose_name='粗旦白含量')
    dpingjia = models.CharField(db_column='评价D', max_length=30, blank=True, null=True, verbose_name='评价D')
    hujijihali = models.CharField(max_length=30, blank=True, null=True, db_column='胡椒碱含量', verbose_name='胡椒碱含量')
    gushtish = models.CharField(max_length=30, blank=True, null=True, db_column='果熟天数', verbose_name='果熟天数')
    webifabilv = models.CharField(max_length=30, blank=True, null=True, db_column='瘟病发病率', verbose_name='瘟病发病率')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_胡椒'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class huluobo(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    rozhgexi = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根形', verbose_name='肉质根形')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    geroshfe = models.CharField(max_length=30, blank=True, null=True, db_column='根肉水分', verbose_name='根肉水分')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='收获期', verbose_name='收获期')
    gesudaxi = models.CharField(max_length=30, blank=True, null=True, db_column='根髓大小', verbose_name='根髓大小')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    rozhgezh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根长', verbose_name='肉质根长')
    gesuse = models.CharField(max_length=30, blank=True, null=True, db_column='根髓色', verbose_name='根髓色')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    gerokoga = models.CharField(max_length=30, blank=True, null=True, db_column='根肉口感', verbose_name='根肉口感')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    shzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='生长期', verbose_name='生长期')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    yemiroma = models.CharField(max_length=30, blank=True, null=True, db_column='叶面茸毛', verbose_name='叶面茸毛')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    yecu = models.CharField(max_length=30, blank=True, null=True, db_column='叶簇', verbose_name='叶簇')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    rozhgecu = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根粗', verbose_name='肉质根粗')
    yebiroma = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄茸毛', verbose_name='叶柄茸毛')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    gerozh = models.CharField(max_length=30, blank=True, null=True, db_column='根肉质', verbose_name='根肉质')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    naihanxing = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    gepise = models.CharField(max_length=30, blank=True, null=True, db_column='根皮色', verbose_name='根皮色')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    gejibudaxi = models.CharField(max_length=30, blank=True, null=True, db_column='根肩部大小', verbose_name='根肩部大小')
    dagezh = models.CharField(max_length=30, blank=True, null=True, db_column='单根重', verbose_name='单根重')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')
    gerose = models.CharField(max_length=30, blank=True, null=True, db_column='根肉色', verbose_name='根肉色')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_胡萝卜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class yaoguo(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kahaxipiji = models.CharField(max_length=30, blank=True, null=True, db_column='抗寒性评价', verbose_name='抗寒性评价')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    guqi = models.CharField(max_length=30, blank=True, null=True, db_column='果期', verbose_name='果期')
    pijia = models.CharField(db_column='评价A', max_length=30, blank=True, null=True, verbose_name='评价A')
    piji = models.CharField(db_column='评价I', max_length=30, blank=True, null=True, verbose_name='评价I')
    lihali = models.CharField(max_length=30, blank=True, null=True, db_column='磷含量', verbose_name='磷含量')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    pijic = models.CharField(db_column='评价C', max_length=30, blank=True, null=True, verbose_name='评价C')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    rekebi = models.CharField(max_length=30, blank=True, null=True, db_column='仁壳比', verbose_name='仁壳比')
    zhfahali = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪含量', verbose_name='脂肪含量')
    fpijia = models.CharField(db_column='评价F', max_length=30, blank=True, null=True, verbose_name='评价F')
    zhyayotu = models.CharField(max_length=30, blank=True, null=True, db_column='主要用途', verbose_name='主要用途')
    huqi = models.CharField(max_length=30, blank=True, null=True, db_column='花期', verbose_name='花期')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    mehali = models.CharField(max_length=30, blank=True, null=True, db_column='镁含量', verbose_name='镁含量')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    gulizhli = models.CharField(max_length=30, blank=True, null=True, db_column='果梨重量', verbose_name='果梨重量')
    pijiad = models.CharField(db_column='评价D', max_length=30, blank=True, null=True, verbose_name='评价D')
    ba_zhgaku = models.CharField(db_column='八℃枝干枯', max_length=30, blank=True, null=True, verbose_name='八℃枝干枯')
    jihali = models.CharField(max_length=30, blank=True, null=True, db_column='钾含量', verbose_name='钾含量')
    pijik = models.CharField(db_column='评价K', max_length=30, blank=True, null=True, verbose_name='评价K')
    dabazhhali = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质含量', verbose_name='蛋白质含量')
    pijil = models.CharField(db_column='评价L', max_length=30, blank=True, null=True, verbose_name='评价L')
    wu_siwalv = models.CharField(db_column='五℃死亡率', max_length=30, blank=True, null=True, verbose_name='五℃死亡率')
    chli = models.CharField(max_length=30, blank=True, null=True, db_column='产量', verbose_name='产量')
    wu_zhjiku = models.CharField(db_column='五℃主茎枯', max_length=30, blank=True, null=True, verbose_name='五℃主茎枯')
    pijih = models.CharField(db_column='评价H', max_length=30, blank=True, null=True, verbose_name='评价H')
    bacudimi = models.CharField(max_length=30, blank=True, null=True, db_column='保存地名', verbose_name='保存地名')
    pijib = models.CharField(db_column='评价B', max_length=30, blank=True, null=True, verbose_name='评价B')
    ba_layelu = models.CharField(db_column='八℃老叶落', max_length=30, blank=True, null=True, verbose_name='八℃老叶落')
    zhzhmich = models.CharField(max_length=30, blank=True, null=True, db_column='种质名称', verbose_name='种质名称')
    jiguzh = models.CharField(max_length=30, blank=True, null=True, db_column='坚果重', verbose_name='坚果重')
    gahali = models.CharField(max_length=30, blank=True, null=True, db_column='钙含量', verbose_name='钙含量')
    zhzhxita = models.CharField(max_length=30, blank=True, null=True, db_column='植株形态', verbose_name='植株形态')
    ba_neshku = models.CharField(db_column='八℃嫩梢枯', max_length=30, blank=True, null=True, verbose_name='八℃嫩梢枯')
    wu_zhgaku = models.CharField(db_column='五℃枝杆枯', max_length=30, blank=True, null=True, verbose_name='五℃枝杆枯')
    pijig = models.CharField(db_column='评价G', max_length=30, blank=True, null=True, verbose_name='评价G')
    chrelv = models.CharField(max_length=30, blank=True, null=True, db_column='出仁率', verbose_name='出仁率')
    zhyakuwuzh = models.CharField(max_length=30, blank=True, null=True, db_column='主要矿物质', verbose_name='主要矿物质')
    guliyase = models.CharField(max_length=30, blank=True, null=True, db_column='果梨颜色', verbose_name='果梨颜色')
    difehali = models.CharField(max_length=30, blank=True, null=True, db_column='淀粉含量', verbose_name='淀粉含量')
    ba_huxuku = models.CharField(db_column='八℃花序枯', max_length=30, blank=True, null=True, verbose_name='八℃花序枯')
    ba_neyeku = models.CharField(db_column='八℃嫩叶枯', max_length=30, blank=True, null=True, verbose_name='八℃嫩叶枯')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_腰果'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class jiegua(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单瓜重', verbose_name='单瓜重')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    gumilafe = models.CharField(max_length=30, blank=True, null=True, db_column='瓜面腊粉', verbose_name='瓜面腊粉')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜皮色', verbose_name='商瓜皮色')
    lagucise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜次色', verbose_name='老瓜次色')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    lagubawe = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜斑纹', verbose_name='老瓜斑纹')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    gucise = models.CharField(max_length=30, blank=True, null=True, db_column='瓜刺色', verbose_name='瓜刺色')
    lagupise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜皮色', verbose_name='老瓜皮色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='瓜形', verbose_name='瓜形')
    gucidush = models.CharField(max_length=30, blank=True, null=True, db_column='瓜刺多少', verbose_name='瓜刺多少')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    cishhujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='雌首花节位', verbose_name='雌首花节位')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    shgucise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜次色', verbose_name='商瓜次色')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shgubawe = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜斑纹', verbose_name='商瓜斑纹')
    gulexizh = models.CharField(max_length=30, blank=True, null=True, db_column='瓜棱形状', verbose_name='瓜棱形状')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_节瓜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class mangguo(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    layeyase = models.CharField(max_length=30, blank=True, null=True, db_column='老叶颜色', verbose_name='老叶颜色')
    yizhbiha = models.CharField(max_length=30, blank=True, null=True, db_column='引种编号', verbose_name='引种编号')
    neyeyase = models.CharField(max_length=30, blank=True, null=True, db_column='嫩叶颜色', verbose_name='嫩叶颜色')
    chlishzhga = models.CharField(max_length=30, blank=True, null=True, db_column='成龄树主干', verbose_name='成龄树主干')
    chlijiqita = models.CharField(max_length=30, blank=True, null=True, db_column='产量及其它', verbose_name='产量及其它')
    pesh = models.CharField(max_length=30, blank=True, null=True, db_column='胚数', verbose_name='胚数')
    hechyiru = models.CharField(max_length=30, blank=True, null=True, db_column='何处引入', verbose_name='何处引入')
    zhzhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='种质来源', verbose_name='种质来源')
    gupipife = models.CharField(max_length=30, blank=True, null=True, db_column='果皮披粉', verbose_name='果皮披粉')
    zhzixizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子形状', verbose_name='种子形状')
    yezhxizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶枕形状', verbose_name='叶枕形状')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    shguyase = models.CharField(max_length=30, blank=True, null=True, db_column='熟果颜色', verbose_name='熟果颜色')
    cema = models.CharField(max_length=30, blank=True, null=True, db_column='侧脉', verbose_name='侧脉')
    chzhlv = models.CharField(max_length=30, blank=True, null=True, db_column='出汁率', verbose_name='出汁率')
    guxizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='果形指数', verbose_name='果形指数')
    yejixizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶基形状', verbose_name='叶基形状')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    daguzhli = models.CharField(max_length=30, blank=True, null=True, db_column='单果重量', verbose_name='单果重量')
    shguxizh = models.CharField(max_length=30, blank=True, null=True, db_column='树冠形状', verbose_name='树冠形状')
    gupihudu = models.CharField(max_length=30, blank=True, null=True, db_column='果皮滑度', verbose_name='果皮滑度')
    zhgaguhudu = models.CharField(max_length=30, blank=True, null=True, db_column='主干光滑度', verbose_name='主干光滑度')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yepidaxi = models.CharField(max_length=30, blank=True, null=True, db_column='叶片大小', verbose_name='叶片大小')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    zhgafezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='主干分枝数', verbose_name='主干分枝数')
    guroxiqi = models.CharField(max_length=30, blank=True, null=True, db_column='果肉香气', verbose_name='果肉香气')
    gupihuwe = models.CharField(max_length=30, blank=True, null=True, db_column='果皮花纹', verbose_name='果皮花纹')
    yepechdu = models.CharField(max_length=30, blank=True, null=True, db_column='叶蓬长短', verbose_name='叶蓬长短')
    guwa = models.CharField(max_length=30, blank=True, null=True, db_column='果洼', verbose_name='果洼')
    shyoqiku = models.CharField(max_length=30, blank=True, null=True, db_column='使用情况', verbose_name='使用情况')
    yehexizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶痕形状', verbose_name='叶痕形状')
    shzhdiroma = models.CharField(max_length=30, blank=True, null=True, db_column='生长点茸毛', verbose_name='生长点茸毛')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    yirushji = models.CharField(max_length=30, blank=True, null=True, db_column='引入时间', verbose_name='引入时间')
    zhke = models.CharField(max_length=30, blank=True, null=True, db_column='种壳', verbose_name='种壳')
    pijib = models.CharField(db_column='评价B', max_length=30, blank=True, null=True, verbose_name='评价B')
    zhzhmich = models.CharField(max_length=30, blank=True, null=True, db_column='种质名称', verbose_name='种质名称')
    mushhuyase = models.CharField(max_length=30, blank=True, null=True, db_column='木栓化颜色', verbose_name='木栓化颜色')
    gushchshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果实成熟期', verbose_name='果实成熟期')
    guji = models.CharField(max_length=30, blank=True, null=True, db_column='果肩', verbose_name='果肩')
    gurofewe = models.CharField(max_length=30, blank=True, null=True, db_column='果肉风味', verbose_name='果肉风味')
    yemash = models.CharField(max_length=30, blank=True, null=True, db_column='叶脉数', verbose_name='叶脉数')
    zhgayase = models.CharField(max_length=30, blank=True, null=True, db_column='主干颜色', verbose_name='主干颜色')
    gurojigo = models.CharField(max_length=30, blank=True, null=True, db_column='果肉结构', verbose_name='果肉结构')
    zhrexizh = models.CharField(max_length=30, blank=True, null=True, db_column='种仁形状', verbose_name='种仁形状')
    gupi = models.CharField(max_length=30, blank=True, null=True, db_column='果皮', verbose_name='果皮')
    yejianxinzhuang = models.CharField(max_length=30, blank=True, null=True, db_column='叶尖形状', verbose_name='叶尖形状')
    qiguyase = models.CharField(max_length=30, blank=True, null=True, db_column='青果颜色', verbose_name='青果颜色')
    gubi = models.CharField(max_length=30, blank=True, null=True, db_column='果柄', verbose_name='果柄')
    quta = models.CharField(max_length=30, blank=True, null=True, db_column='全糖', verbose_name='全糖')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    pijia = models.CharField(db_column='评价A', max_length=30, blank=True, null=True, verbose_name='评价A')
    gupibadi = models.CharField(max_length=30, blank=True, null=True, db_column='果皮白点', verbose_name='果皮白点')
    fugo = models.CharField(max_length=30, blank=True, null=True, db_column='腹沟', verbose_name='腹沟')
    shfe = models.CharField(max_length=30, blank=True, null=True, db_column='水份', verbose_name='水份')
    guzh = models.CharField(max_length=30, blank=True, null=True, db_column='果枕', verbose_name='果枕')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    guroyase = models.CharField(max_length=30, blank=True, null=True, db_column='果肉颜色', verbose_name='果肉颜色')
    wama = models.CharField(max_length=30, blank=True, null=True, db_column='网脉', verbose_name='网脉')
    yepixizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶片形状', verbose_name='叶片形状')
    wazhyowu = models.CharField(max_length=30, blank=True, null=True, db_column='网状有无', verbose_name='网状有无')
    keshbufe = models.CharField(max_length=30, blank=True, null=True, db_column='可食部分', verbose_name='可食部分')
    guxipiji = models.CharField(max_length=30, blank=True, null=True, db_column='果形评价', verbose_name='果形评价')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    gurozhdi = models.CharField(max_length=30, blank=True, null=True, db_column='果肉质地', verbose_name='果肉质地')
    gudi = models.CharField(max_length=30, blank=True, null=True, db_column='果顶', verbose_name='果顶')
    zhzizhli = models.CharField(max_length=30, blank=True, null=True, db_column='种子重量', verbose_name='种子重量')
    yebixita = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄形态', verbose_name='叶柄形态')
    pizhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='品质评价', verbose_name='品质评价')
    roxiguxiwu = models.CharField(max_length=30, blank=True, null=True, db_column='溶性固形物', verbose_name='溶性固形物')
    pejuchdu = models.CharField(max_length=30, blank=True, null=True, db_column='蓬距长短', verbose_name='蓬距长短')
    yepexizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶蓬形状', verbose_name='叶蓬形状')
    lipihexizh = models.CharField(max_length=30, blank=True, null=True, db_column='鳞片痕形状', verbose_name='鳞片痕形状')
    yexizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='叶形指数', verbose_name='叶形指数')
    guhu = models.CharField(max_length=30, blank=True, null=True, db_column='果喙', verbose_name='果喙')
    shgushmi = models.CharField(max_length=30, blank=True, null=True, db_column='树冠疏密', verbose_name='树冠疏密')
    zhzidaxi = models.CharField(max_length=30, blank=True, null=True, db_column='种子大小', verbose_name='种子大小')
    tasubi = models.CharField(max_length=30, blank=True, null=True, db_column='糖酸比', verbose_name='糖酸比')
    bacudimi = models.CharField(max_length=30, blank=True, null=True, db_column='保存地名', verbose_name='保存地名')
    zhrezhbili = models.CharField(max_length=30, blank=True, null=True, db_column='种仁占比例', verbose_name='种仁占比例')
    yebizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄长', verbose_name='叶柄长')
    guwo = models.CharField(max_length=30, blank=True, null=True, db_column='果窝', verbose_name='果窝')
    yepihodu = models.CharField(max_length=30, blank=True, null=True, db_column='叶片厚度', verbose_name='叶片厚度')
    yojisu = models.CharField(max_length=30, blank=True, null=True, db_column='有机酸', verbose_name='有机酸')
    zhkexiwe = models.CharField(max_length=30, blank=True, null=True, db_column='种壳纤维', verbose_name='种壳纤维')
    huyuta = models.CharField(max_length=30, blank=True, null=True, db_column='还原糖', verbose_name='还原糖')
    zhjiju = models.CharField(max_length=30, blank=True, null=True, db_column='中间距', verbose_name='中间距')
    xiqihubase = models.CharField(max_length=30, blank=True, null=True, db_column='谢前花瓣色', verbose_name='谢前花瓣色')
    guroxiwe = models.CharField(max_length=30, blank=True, null=True, db_column='果肉纤维', verbose_name='果肉纤维')
    zhtishsh = models.CharField(max_length=30, blank=True, null=True, db_column='枝条生势', verbose_name='枝条生势')
    gushdaxi = models.CharField(max_length=30, blank=True, null=True, db_column='果实大小', verbose_name='果实大小')
    ligoyowu = models.CharField(max_length=30, blank=True, null=True, db_column='裂沟有无', verbose_name='裂沟有无')
    zhhu = models.CharField(max_length=30, blank=True, null=True, db_column='种喙', verbose_name='种喙')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_芒果'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class wujing(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    nacaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐藏性', verbose_name='耐藏性')
    gexi = models.CharField(max_length=30, blank=True, null=True, db_column='根形', verbose_name='根形')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    yecu = models.CharField(max_length=30, blank=True, null=True, db_column='叶簇', verbose_name='叶簇')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    gezh = models.CharField(max_length=30, blank=True, null=True, db_column='根重', verbose_name='根重')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    xumi = models.CharField(max_length=50, blank=True, null=True, db_column='学名', verbose_name='学名')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶型', verbose_name='叶型')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    gerozh = models.CharField(max_length=30, blank=True, null=True, db_column='根肉质', verbose_name='根肉质')
    gepise = models.CharField(max_length=30, blank=True, null=True, db_column='根皮色', verbose_name='根皮色')
    geshfe = models.CharField(max_length=30, blank=True, null=True, db_column='根水分', verbose_name='根水分')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    shzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='生长期', verbose_name='生长期')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    gerose = models.CharField(max_length=30, blank=True, null=True, db_column='根肉色', verbose_name='根肉色')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_芜菁'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class wujingganlan(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    rozhgexi = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根形', verbose_name='肉质根形')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    geroshfe = models.CharField(max_length=30, blank=True, null=True, db_column='根肉水分', verbose_name='根肉水分')
    yemilafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶面蜡粉', verbose_name='叶面蜡粉')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    rozhgezh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根长', verbose_name='肉质根长')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='收获期', verbose_name='收获期')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    gerokoga = models.CharField(max_length=30, blank=True, null=True, db_column='根肉口感', verbose_name='根肉口感')
    gedishbuzh = models.CharField(max_length=30, blank=True, null=True, db_column='根地上部长', verbose_name='根地上部长')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    dishbupise = models.CharField(max_length=30, blank=True, null=True, db_column='地上部皮色', verbose_name='地上部皮色')
    yecu = models.CharField(max_length=30, blank=True, null=True, db_column='叶簇', verbose_name='叶簇')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    rozhgecu = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根粗', verbose_name='肉质根粗')
    dixibupise = models.CharField(max_length=30, blank=True, null=True, db_column='地下部皮色', verbose_name='地下部皮色')
    yemicima = models.CharField(max_length=30, blank=True, null=True, db_column='叶面刺毛', verbose_name='叶面刺毛')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶型', verbose_name='叶型')
    yx = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    gerozh = models.CharField(max_length=30, blank=True, null=True, db_column='根肉质', verbose_name='根肉质')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    yepizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶片长', verbose_name='叶片长')
    naihanxing = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    yepiku = models.CharField(max_length=30, blank=True, null=True, db_column='叶片宽', verbose_name='叶片宽')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    dagezh = models.CharField(max_length=30, blank=True, null=True, db_column='单根重', verbose_name='单根重')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')
    gerose = models.CharField(max_length=30, blank=True, null=True, db_column='根肉色', verbose_name='根肉色')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_芜菁甘蓝'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class zhima(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    jigaromali = models.CharField(max_length=30, blank=True, null=True, db_column='茎秆茸毛量', verbose_name='茎秆茸毛量')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    yosu = models.CharField(max_length=30, blank=True, null=True, db_column='油酸', verbose_name='油酸')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    nazixi = models.CharField(max_length=30, blank=True, null=True, db_column='耐渍性', verbose_name='耐渍性')
    zolvsu = models.CharField(max_length=30, blank=True, null=True, db_column='棕榈酸', verbose_name='棕榈酸')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    chshjigase = models.CharField(max_length=30, blank=True, null=True, db_column='成熟茎秆色', verbose_name='成熟茎秆色')
    hayoli = models.CharField(max_length=30, blank=True, null=True, db_column='含油量', verbose_name='含油量')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    meyeyehush = models.CharField(max_length=30, blank=True, null=True, db_column='每叶腋花数', verbose_name='每叶腋花数')
    yizhsu = models.CharField(max_length=30, blank=True, null=True, db_column='硬脂酸', verbose_name='硬脂酸')
    shguchdu = models.CharField(max_length=30, blank=True, null=True, db_column='蒴果长度', verbose_name='蒴果长度')
    chdihulayu = models.CharField(max_length=30, blank=True, null=True, db_column='产地或来源', verbose_name='产地或来源')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    jidikubi = models.CharField(max_length=30, blank=True, null=True, db_column='茎点枯病', verbose_name='茎点枯病')
    shgulesh = models.CharField(max_length=30, blank=True, null=True, db_column='蒴果棱数', verbose_name='蒴果棱数')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    xumi = models.CharField(max_length=50, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    dabazhhali = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质含量', verbose_name='蛋白质含量')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    yayosu = models.CharField(max_length=30, blank=True, null=True, db_column='亚油酸', verbose_name='亚油酸')
    shyurish = models.CharField(max_length=30, blank=True, null=True, db_column='生育日数', verbose_name='生育日数')
    lishxi = models.CharField(max_length=30, blank=True, null=True, db_column='裂蒴性', verbose_name='裂蒴性')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    zhpise = models.CharField(max_length=30, blank=True, null=True, db_column='种皮色', verbose_name='种皮色')
    kuwebi = models.CharField(max_length=30, blank=True, null=True, db_column='枯萎病', verbose_name='枯萎病')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_芝麻'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class gailan(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    dizhzhshsh = models.CharField(max_length=30, blank=True, null=True, db_column='定植至始收', verbose_name='定植至始收')
    yemilafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶面蜡粉', verbose_name='叶面蜡粉')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    zhtacu = models.CharField(max_length=30, blank=True, null=True, db_column='主薹粗', verbose_name='主薹粗')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    yelike = models.CharField(max_length=30, blank=True, null=True, db_column='叶裂刻', verbose_name='叶裂刻')
    dizhqi = models.CharField(max_length=30, blank=True, null=True, db_column='定植期', verbose_name='定植期')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    dazhtash = models.CharField(max_length=30, blank=True, null=True, db_column='单株薹数', verbose_name='单株薹数')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    xilipidush = models.CharField(max_length=30, blank=True, null=True, db_column='小裂片对数', verbose_name='小裂片对数')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    moshqi = models.CharField(max_length=30, blank=True, null=True, db_column='末收期', verbose_name='末收期')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    zhtaga = models.CharField(max_length=30, blank=True, null=True, db_column='主薹高', verbose_name='主薹高')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    shshqi = models.CharField(max_length=30, blank=True, null=True, db_column='始收期', verbose_name='始收期')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    zhtase = models.CharField(max_length=30, blank=True, null=True, db_column='主薹色', verbose_name='主薹色')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    naihanxing = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    yeyi = models.CharField(max_length=30, blank=True, null=True, db_column='叶翼', verbose_name='叶翼')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_芥蓝'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class yansui(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    dazhyesh = models.CharField(max_length=30, blank=True, null=True, db_column='单株叶数', verbose_name='单株叶数')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    yebizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄长', verbose_name='叶柄长')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶长', verbose_name='叶长')
    yeku = models.CharField(max_length=30, blank=True, null=True, db_column='叶宽', verbose_name='叶宽')
    dazhzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株重', verbose_name='单株重')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yeji = models.CharField(max_length=30, blank=True, null=True, db_column='叶角', verbose_name='叶角')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_芫荽'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class huayecai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    huqiheji = models.CharField(max_length=30, blank=True, null=True, db_column='花球横径', verbose_name='花球横径')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    huqipizh = models.CharField(max_length=30, blank=True, null=True, db_column='花球品质', verbose_name='花球品质')
    dizhzhshsh = models.CharField(max_length=30, blank=True, null=True, db_column='定植至始收', verbose_name='定植至始收')
    yemilafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶面蜡粉', verbose_name='叶面蜡粉')
    huqixizh = models.CharField(max_length=30, blank=True, null=True, db_column='花球形状', verbose_name='花球形状')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    wayesh = models.CharField(max_length=30, blank=True, null=True, db_column='外叶数', verbose_name='外叶数')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    dizhqi = models.CharField(max_length=30, blank=True, null=True, db_column='定植期', verbose_name='定植期')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    huqizoji = models.CharField(max_length=30, blank=True, null=True, db_column='花球纵径', verbose_name='花球纵径')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    huqijishdu = models.CharField(max_length=30, blank=True, null=True, db_column='花球紧实度', verbose_name='花球紧实度')
    xumi = models.CharField(max_length=50, blank=True, null=True, db_column='学名', verbose_name='学名')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='收获期', verbose_name='收获期')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    naihanxing = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    huqise = models.CharField(max_length=30, blank=True, null=True, db_column='花球色', verbose_name='花球色')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    qimiroma = models.CharField(max_length=30, blank=True, null=True, db_column='球面茸毛', verbose_name='球面茸毛')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    romase = models.CharField(max_length=30, blank=True, null=True, db_column='茸毛色', verbose_name='茸毛色')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    huqizh = models.CharField(max_length=30, blank=True, null=True, db_column='花球重', verbose_name='花球重')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_花椰菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class huasheng(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    hayoli = models.CharField(max_length=30, blank=True, null=True, db_column='含油量', verbose_name='含油量')
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    sang = models.CharField(max_length=30, blank=True, null=True, db_column='谷氨酸', verbose_name='谷氨酸')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zolvsu = models.CharField(max_length=30, blank=True, null=True, db_column='棕榈酸', verbose_name='棕榈酸')
    jiansu = models.CharField(max_length=30, blank=True, null=True, db_column='精氨酸', verbose_name='精氨酸')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    dazhshchlv = models.CharField(max_length=30, blank=True, null=True, db_column='单株生产率', verbose_name='单株生产率')
    las = models.CharField(max_length=30, blank=True, null=True, db_column='酪氨酸', verbose_name='酪氨酸')
    kagejixich = models.CharField(max_length=30, blank=True, null=True, db_column='抗根结线虫', verbose_name='抗根结线虫')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='类型', verbose_name='类型')
    yizhsu = models.CharField(max_length=30, blank=True, null=True, db_column='硬脂酸', verbose_name='硬脂酸')
    zuansu = models.CharField(max_length=30, blank=True, null=True, db_column='组氨酸', verbose_name='组氨酸')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    shyusu = models.CharField(max_length=30, blank=True, null=True, db_column='山芋酸', verbose_name='山芋酸')
    yayosu = models.CharField(max_length=30, blank=True, null=True, db_column='亚油酸', verbose_name='亚油酸')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    kayeheba = models.CharField(max_length=30, blank=True, null=True, db_column='抗叶黑斑', verbose_name='抗叶黑斑')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    xuyufafa = models.CharField(max_length=30, blank=True, null=True, db_column='选育方法', verbose_name='选育方法')
    bebiansu = models.CharField(max_length=30, blank=True, null=True, db_column='苯丙氨酸', verbose_name='苯丙氨酸')
    yueguang  = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    dabazhhali = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质含量', verbose_name='蛋白质含量')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    yosu = models.CharField(max_length=30, blank=True, null=True, db_column='油酸', verbose_name='油酸')
    liansu = models.CharField(max_length=30, blank=True, null=True, db_column='亮氨酸', verbose_name='亮氨酸')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    hushsu = models.CharField(max_length=30, blank=True, null=True, db_column='花生酸', verbose_name='花生酸')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    baguzh = models.CharField(max_length=30, blank=True, null=True, db_column='百果重', verbose_name='百果重')
    kaqiku = models.CharField(max_length=30, blank=True, null=True, db_column='抗青枯', verbose_name='抗青枯')
    gaansu = models.CharField(max_length=30, blank=True, null=True, db_column='甘氨酸', verbose_name='甘氨酸')
    xiansu = models.CharField(max_length=30, blank=True, null=True, db_column='缬氨酸', verbose_name='缬氨酸')
    seansu = models.CharField(max_length=30, blank=True, null=True, db_column='色氨酸', verbose_name='色氨酸')
    kayeheban = models.CharField(max_length=30, blank=True, null=True, db_column='抗叶褐斑', verbose_name='抗叶褐斑')
    fuansu = models.CharField(max_length=30, blank=True, null=True, db_column='脯氨酸', verbose_name='脯氨酸')
    barezh = models.CharField(max_length=30, blank=True, null=True, db_column='百仁重', verbose_name='百仁重')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝型', verbose_name='分枝型')
    kaha = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱', verbose_name='抗旱')
    naiasan = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    chrelv = models.CharField(max_length=30, blank=True, null=True, db_column='出仁率', verbose_name='出仁率')
    kala = models.CharField(max_length=30, blank=True, null=True, db_column='抗涝', verbose_name='抗涝')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    kahuxixi = models.CharField(max_length=30, blank=True, null=True, db_column='开花习性', verbose_name='开花习性')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    hushxisu = models.CharField(max_length=30, blank=True, null=True, db_column='花生烯酸', verbose_name='花生烯酸')
    bidubi = models.CharField(max_length=30, blank=True, null=True, db_column='病毒病', verbose_name='病毒病')
    kaxibi = models.CharField(max_length=30, blank=True, null=True, db_column='抗锈病', verbose_name='抗锈病')
    yiliansu = models.CharField(max_length=30, blank=True, null=True, db_column='异亮氨酸', verbose_name='异亮氨酸')
    zhjiga = models.CharField(max_length=30, blank=True, null=True, db_column='主茎高', verbose_name='主茎高')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_花生'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class qincai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    yebirozh = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄肉质', verbose_name='叶柄肉质')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    yebizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄长', verbose_name='叶柄长')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    dazhzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株重', verbose_name='单株重')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yebiku = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄宽', verbose_name='叶柄宽')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    yebiho = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄厚', verbose_name='叶柄厚')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yebidumi = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄断面', verbose_name='叶柄断面')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zapejiji = models.CharField(max_length=50, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_芹菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class xiancai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhzhta = models.CharField(max_length=30, blank=True, null=True, db_column='生长状态', verbose_name='生长状态')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    roma = models.CharField(max_length=30, blank=True, null=True, db_column='茸毛', verbose_name='茸毛')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    dazhzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株重', verbose_name='单株重')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    yeji = models.CharField(max_length=30, blank=True, null=True, db_column='叶角', verbose_name='叶角')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_苋菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class zhuma(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    xiji = models.CharField(max_length=30, blank=True, null=True, db_column='锈脚', verbose_name='锈脚')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    xipihodu = models.CharField(max_length=30, blank=True, null=True, db_column='鲜皮厚度', verbose_name='鲜皮厚度')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    cilese = models.CharField(max_length=30, blank=True, null=True, db_column='雌蕾色', verbose_name='雌蕾色')
    gexi = models.CharField(max_length=30, blank=True, null=True, db_column='根型', verbose_name='根型')
    huyebi = models.CharField(max_length=30, blank=True, null=True, db_column='花叶病', verbose_name='花叶病')
    maguse = models.CharField(max_length=30, blank=True, null=True, db_column='麻骨色', verbose_name='麻骨色')
    yumachli = models.CharField(max_length=30, blank=True, null=True, db_column='原麻产量', verbose_name='原麻产量')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    fezhli = models.CharField(max_length=30, blank=True, null=True, db_column='分株力', verbose_name='分株力')
    cilexileqi = models.CharField(max_length=30, blank=True, null=True, db_column='雌蕾现蕾期', verbose_name='雌蕾现蕾期')
    doxi = models.CharField(max_length=30, blank=True, null=True, db_column='蔸型', verbose_name='蔸型')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    daxiweqili = models.CharField(max_length=30, blank=True, null=True, db_column='单纤维强力', verbose_name='单纤维强力')
    shzhzhqidu = models.CharField(max_length=30, blank=True, null=True, db_column='生长整齐度', verbose_name='生长整齐度')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhjuyudu = models.CharField(max_length=30, blank=True, null=True, db_column='生长均匀度', verbose_name='生长均匀度')
    kafexi = models.CharField(max_length=30, blank=True, null=True, db_column='抗风性', verbose_name='抗风性')
    goyichshti = models.CharField(max_length=30, blank=True, null=True, db_column='工艺成熟天', verbose_name='工艺成熟天')
    yemizhwe = models.CharField(max_length=30, blank=True, null=True, db_column='叶面皱纹', verbose_name='叶面皱纹')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    cihukahuqi = models.CharField(max_length=30, blank=True, null=True, db_column='雌花开花期', verbose_name='雌花开花期')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    daxizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='单纤支数', verbose_name='单纤支数')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    xipichmalv = models.CharField(max_length=30, blank=True, null=True, db_column='鲜皮出麻率', verbose_name='鲜皮出麻率')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    yoxizhlv = models.CharField(max_length=30, blank=True, null=True, db_column='有效株率', verbose_name='有效株率')
    jicu = models.CharField(max_length=30, blank=True, null=True, db_column='茎粗', verbose_name='茎粗')
    dawebiha = models.CharField(max_length=20, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    mise = models.CharField(max_length=20, blank=True, null=True, db_column='米色', verbose_name='米色')
    chsurish = models.CharField(max_length=30, blank=True, null=True, db_column='抽穗日数', verbose_name='抽穗日数')
    bewe = models.CharField(max_length=30, blank=True, null=True, db_column='北纬', verbose_name='北纬')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    gach = models.CharField(max_length=30, blank=True, null=True, db_column='高程', verbose_name='高程')
    dazhgazh = models.CharField(max_length=30, blank=True, null=True, db_column='单株秆重', verbose_name='单株秆重')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    doji = models.CharField(max_length=30, blank=True, null=True, db_column='东经', verbose_name='东经')
    zhjijish = models.CharField(max_length=30, blank=True, null=True, db_column='主茎节数', verbose_name='主茎节数')
    cimachdu = models.CharField(max_length=30, blank=True, null=True, db_column='刺毛长度', verbose_name='刺毛长度')
    dazhlizh = models.CharField(max_length=30, blank=True, null=True, db_column='单株粒重', verbose_name='单株粒重')
    cado = models.CharField(max_length=30, blank=True, null=True, db_column='蚕豆', verbose_name='蚕豆')
    zhfasu16 = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪酸160', verbose_name='脂肪酸160')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_苎麻'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class suzi(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    zhzihayolv = models.CharField(max_length=30, blank=True, null=True, db_column='种子含油率', verbose_name='种子含油率')
    gusush = models.CharField(max_length=30, blank=True, null=True, db_column='果穗数', verbose_name='果穗数')
    chdihulayu = models.CharField(max_length=30, blank=True, null=True, db_column='产地或来源', verbose_name='产地或来源')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    biha = models.CharField(max_length=30, blank=True, null=True, db_column='编号', verbose_name='编号')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='类型', verbose_name='类型')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    shyurish = models.CharField(max_length=30, blank=True, null=True, db_column='生育日数', verbose_name='生育日数')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    jijish = models.CharField(max_length=30, blank=True, null=True, db_column='茎节数', verbose_name='茎节数')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    xumi = models.CharField(max_length=70, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zhsuzh = models.CharField(max_length=30, blank=True, null=True, db_column='主穗长', verbose_name='主穗长')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    xuyufafa = models.CharField(max_length=30, blank=True, null=True, db_column='选育方法', verbose_name='选育方法')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_苏子'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class kugua(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单瓜重', verbose_name='单瓜重')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    gumilafe = models.CharField(max_length=30, blank=True, null=True, db_column='瓜面腊粉', verbose_name='瓜面腊粉')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜皮色', verbose_name='商瓜皮色')
    lagucise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜次色', verbose_name='老瓜次色')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    lagubawe = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜斑纹', verbose_name='老瓜斑纹')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    lagupise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜皮色', verbose_name='老瓜皮色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='瓜形', verbose_name='瓜形')
    gucidush = models.CharField(max_length=30, blank=True, null=True, db_column='瓜刺多少', verbose_name='瓜刺多少')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    cishhujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='雌首花节位', verbose_name='雌首花节位')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    shgucise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜次色', verbose_name='商瓜次色')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shgubawe = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜斑纹', verbose_name='商瓜斑纹')
    gulexizh = models.CharField(max_length=30, blank=True, null=True, db_column='瓜棱形状', verbose_name='瓜棱形状')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_苦瓜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class pingguo(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    nezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='内质评价', verbose_name='内质评价')
    keroxita = models.CharField(db_column='可溶性糖％', max_length=30, blank=True, null=True, verbose_name='可溶性糖％')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    tuxi = models.CharField(max_length=30, blank=True, null=True, db_column='图象', verbose_name='图象')
    daguzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='单果重评价', verbose_name='单果重评价')
    gushchshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果实成熟期', verbose_name='果实成熟期')
    chshqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期评价', verbose_name='成熟期评价')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    daguzhg = models.CharField(db_column='单果重G', max_length=30, blank=True, null=True, verbose_name='单果重G')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    zhye = models.CharField(max_length=30, blank=True, null=True, db_column='汁液', verbose_name='汁液')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    shgunili = models.CharField(max_length=30, blank=True, null=True, db_column='始果年龄', verbose_name='始果年龄')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    keroguxiwu = models.CharField(max_length=30, blank=True, null=True, db_column='可溶固形物', verbose_name='可溶固形物')
    shyuqi = models.CharField(db_column='生育期D', max_length=30, blank=True, null=True, verbose_name='生育期D')
    shyuqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='生育期评价', verbose_name='生育期评价')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zaguxipiji = models.CharField(max_length=30, blank=True, null=True, db_column='早果性评价', verbose_name='早果性评价')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    kedidisu = models.CharField(db_column='可滴定酸％', max_length=30, blank=True, null=True, verbose_name='可滴定酸％')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_苹果'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class qiezi(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    qishguse = models.CharField(max_length=30, blank=True, null=True, db_column='青熟果色', verbose_name='青熟果色')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    shhujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='首花节位', verbose_name='首花节位')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    zhzidush = models.CharField(max_length=30, blank=True, null=True, db_column='种子多少', verbose_name='种子多少')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单果重', verbose_name='单果重')
    qigurozh = models.CharField(max_length=30, blank=True, null=True, db_column='青果肉质', verbose_name='青果肉质')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_茄子'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class jingyongwoju(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    rojirozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉茎肉质', verbose_name='肉茎肉质')
    rojishfe = models.CharField(max_length=30, blank=True, null=True, db_column='肉茎水分', verbose_name='肉茎水分')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    rojirose = models.CharField(max_length=30, blank=True, null=True, db_column='肉茎肉色', verbose_name='肉茎肉色')
    rojipise = models.CharField(max_length=30, blank=True, null=True, db_column='肉茎皮色', verbose_name='肉茎皮色')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zapejiji = models.CharField(max_length=50, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    rojixizh = models.CharField(max_length=30, blank=True, null=True, db_column='肉茎形状', verbose_name='肉茎形状')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    rojizh = models.CharField(max_length=30, blank=True, null=True, db_column='肉茎重', verbose_name='肉茎重')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_茎用莴苣'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class jinggaicai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    jilawe = models.CharField(max_length=30, blank=True, null=True, db_column='芥辣味', verbose_name='芥辣味')
    dizhqi = models.CharField(max_length=30, blank=True, null=True, db_column='定植期', verbose_name='定植期')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yebitezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄特征', verbose_name='叶柄特征')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    rojizoji = models.CharField(max_length=30, blank=True, null=True, db_column='肉茎纵径', verbose_name='肉茎纵径')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    yemilafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶面蜡粉', verbose_name='叶面蜡粉')
    kazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='开展度', verbose_name='开展度')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yemicima = models.CharField(max_length=30, blank=True, null=True, db_column='叶面刺毛', verbose_name='叶面刺毛')
    rojilexi = models.CharField(max_length=30, blank=True, null=True, db_column='肉茎类型', verbose_name='肉茎类型')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')
    rojizh = models.CharField(max_length=30, blank=True, null=True, db_column='肉茎重', verbose_name='肉茎重')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='收获期', verbose_name='收获期')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    yeyi = models.CharField(max_length=30, blank=True, null=True, db_column='叶翼', verbose_name='叶翼')
    rojiheji = models.CharField(max_length=30, blank=True, null=True, db_column='肉茎横径', verbose_name='肉茎横径')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    xumi = models.CharField(max_length=50, blank=True, null=True, db_column='学名', verbose_name='学名')
    rojishfe = models.CharField(max_length=30, blank=True, null=True, db_column='肉茎水分', verbose_name='肉茎水分')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    yelike = models.CharField(max_length=30, blank=True, null=True, db_column='叶裂刻', verbose_name='叶裂刻')
    hanbaixing = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    rojipise = models.CharField(max_length=30, blank=True, null=True, db_column='肉茎皮色', verbose_name='肉茎皮色')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    xilipidush = models.CharField(max_length=30, blank=True, null=True, db_column='小裂片对数', verbose_name='小裂片对数')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    rojixizh = models.CharField(max_length=30, blank=True, null=True, db_column='肉茎形状', verbose_name='肉茎形状')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    shzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='生长期', verbose_name='生长期')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_茎芥菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class huixiang(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶长', verbose_name='叶长')
    yeku = models.CharField(max_length=30, blank=True, null=True, db_column='叶宽', verbose_name='叶宽')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_茴香'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class cha(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    yesh = models.CharField(max_length=30, blank=True, null=True, db_column='叶身', verbose_name='叶身')
    hubash = models.CharField(max_length=30, blank=True, null=True, db_column='花瓣数', verbose_name='花瓣数')
    yeji = models.CharField(max_length=30, blank=True, null=True, db_column='叶尖', verbose_name='叶尖')
    kahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱性', verbose_name='抗旱性')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    zhzichshqi = models.CharField(max_length=30, blank=True, null=True, db_column='种子成熟期', verbose_name='种子成熟期')
    yeroho = models.CharField(max_length=30, blank=True, null=True, db_column='叶肉厚', verbose_name='叶肉厚')
    yj = models.CharField(max_length=30, blank=True, null=True, db_column='叶基', verbose_name='叶基')
    shjichwu = models.CharField(max_length=30, blank=True, null=True, db_column='水浸出物', verbose_name='水浸出物')
    yezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶质', verbose_name='叶质')
    fayariqi = models.CharField(max_length=30, blank=True, null=True, db_column='发芽日期', verbose_name='发芽日期')
    zhjidaxi = models.CharField(max_length=30, blank=True, null=True, db_column='种径大小', verbose_name='种径大小')
    xishyase = models.CharField(max_length=30, blank=True, null=True, db_column='新梢颜色', verbose_name='新梢颜色')
    yayeseze = models.CharField(max_length=30, blank=True, null=True, db_column='芽叶色泽', verbose_name='芽叶色泽')
    kagejixich = models.CharField(max_length=30, blank=True, null=True, db_column='抗根结线虫', verbose_name='抗根结线虫')
    ziyulexi = models.CharField(max_length=30, blank=True, null=True, db_column='资源类型', verbose_name='资源类型')
    chdufe = models.CharField(max_length=30, blank=True, null=True, db_column='茶多酚', verbose_name='茶多酚')
    kafeji = models.CharField(max_length=30, blank=True, null=True, db_column='咖啡碱', verbose_name='咖啡碱')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    kayuweyeku = models.CharField(max_length=30, blank=True, null=True, db_column='抗云纹叶枯', verbose_name='抗云纹叶枯')
    yechmidu = models.CharField(max_length=30, blank=True, null=True, db_column='叶齿密度', verbose_name='叶齿密度')
    hubadaxi = models.CharField(max_length=30, blank=True, null=True, db_column='花瓣大小', verbose_name='花瓣大小')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yoxijiwe = models.CharField(max_length=30, blank=True, null=True, db_column='有效积温', verbose_name='有效积温')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    yechshdu = models.CharField(max_length=30, blank=True, null=True, db_column='叶齿深度', verbose_name='叶齿深度')
    yayezhkata = models.CharField(max_length=30, blank=True, null=True, db_column='芽叶展开态', verbose_name='芽叶展开态')
    chchxiqi = models.CharField(max_length=30, blank=True, null=True, db_column='成茶香气', verbose_name='成茶香气')
    hubaseze = models.CharField(max_length=30, blank=True, null=True, db_column='花瓣色泽', verbose_name='花瓣色泽')
    yayeloqixi = models.CharField(max_length=30, blank=True, null=True, db_column='芽叶隆起性', verbose_name='芽叶隆起性')
    erchsuzoli = models.CharField(max_length=30, blank=True, null=True, db_column='儿茶素总量', verbose_name='儿茶素总量')
    fazhfash = models.CharField(max_length=30, blank=True, null=True, db_column='繁殖方式', verbose_name='繁殖方式')
    erchsuyi = models.CharField(max_length=30, blank=True, null=True, db_column='儿茶素一', verbose_name='儿茶素一')
    zhtoliwe = models.CharField(max_length=30, blank=True, null=True, db_column='柱头裂位', verbose_name='柱头裂位')
    erchsusa = models.CharField(max_length=30, blank=True, null=True, db_column='儿茶素三', verbose_name='儿茶素三')
    yeku = models.CharField(max_length=30, blank=True, null=True, db_column='叶宽', verbose_name='叶宽')
    erchsusi = models.CharField(max_length=30, blank=True, null=True, db_column='儿茶素四', verbose_name='儿茶素四')
    hugechdu = models.CharField(max_length=30, blank=True, null=True, db_column='花梗长度', verbose_name='花梗长度')
    hochzofe = models.CharField(max_length=30, blank=True, null=True, db_column='红茶总分', verbose_name='红茶总分')
    erchsuwu = models.CharField(max_length=30, blank=True, null=True, db_column='儿茶素五', verbose_name='儿茶素五')
    huesh = models.CharField(max_length=30, blank=True, null=True, db_column='花萼数', verbose_name='花萼数')
    zhpiseze = models.CharField(max_length=30, blank=True, null=True, db_column='种皮色泽', verbose_name='种皮色泽')
    yezi = models.CharField(max_length=30, blank=True, null=True, db_column='叶姿', verbose_name='叶姿')
    chguxizh = models.CharField(max_length=30, blank=True, null=True, db_column='茶果形状', verbose_name='茶果形状')
    kanghanxing = models.CharField(max_length=30, blank=True, null=True, db_column='抗寒性', verbose_name='抗寒性')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    cixigabi = models.CharField(max_length=30, blank=True, null=True, db_column='雌雄高比', verbose_name='雌雄高比')
    shzi = models.CharField(max_length=30, blank=True, null=True, db_column='树姿', verbose_name='树姿')
    xishchdu = models.CharField(max_length=30, blank=True, null=True, db_column='新梢长度', verbose_name='新梢长度')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    shzhxi = models.CharField(max_length=30, blank=True, null=True, db_column='适制性', verbose_name='适制性')
    fayamidu = models.CharField(max_length=30, blank=True, null=True, db_column='发芽密度', verbose_name='发芽密度')
    zhmepudash = models.CharField(max_length=30, blank=True, null=True, db_column='酯酶谱带数', verbose_name='酯酶谱带数')
    zhlazuzhho = models.CharField(max_length=30, blank=True, null=True, db_column='栅栏组织厚', verbose_name='栅栏组织厚')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='始花期', verbose_name='始花期')
    xishroma = models.CharField(max_length=30, blank=True, null=True, db_column='新梢茸毛', verbose_name='新梢茸毛')
    yemadush = models.CharField(max_length=30, blank=True, null=True, db_column='叶脉对数', verbose_name='叶脉对数')
    xishzhli = models.CharField(max_length=30, blank=True, null=True, db_column='新梢重量', verbose_name='新梢重量')
    fechxi = models.CharField(max_length=30, blank=True, null=True, db_column='丰产性', verbose_name='丰产性')
    huzhchdu = models.CharField(max_length=30, blank=True, null=True, db_column='花柱长度', verbose_name='花柱长度')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    hamizuzhho = models.CharField(max_length=30, blank=True, null=True, db_column='海绵组织厚', verbose_name='海绵组织厚')
    tixizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='萜烯指数', verbose_name='萜烯指数')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    zhmilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种苗来源', verbose_name='种苗来源')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    xishmidu = models.CharField(max_length=30, blank=True, null=True, db_column='新梢密度', verbose_name='新梢密度')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='树型', verbose_name='树型')
    wulochzofe = models.CharField(max_length=30, blank=True, null=True, db_column='乌龙茶总分', verbose_name='乌龙茶总分')
    kabaxibi = models.CharField(max_length=30, blank=True, null=True, db_column='抗白星病', verbose_name='抗白星病')
    yechrudu = models.CharField(max_length=30, blank=True, null=True, db_column='叶齿锐度', verbose_name='叶齿锐度')
    hueseze = models.CharField(max_length=30, blank=True, null=True, db_column='花萼色泽', verbose_name='花萼色泽')
    kamale = models.CharField(max_length=30, blank=True, null=True, db_column='抗螨类', verbose_name='抗螨类')
    hueroma = models.CharField(max_length=30, blank=True, null=True, db_column='花萼茸毛', verbose_name='花萼茸毛')
    zhtolish = models.CharField(max_length=30, blank=True, null=True, db_column='柱头裂数', verbose_name='柱头裂数')
    jijichdu = models.CharField(max_length=30, blank=True, null=True, db_column='节间长度', verbose_name='节间长度')
    kaxilvyech = models.CharField(max_length=30, blank=True, null=True, db_column='抗小绿叶蝉', verbose_name='抗小绿叶蝉')
    erchsuer = models.CharField(max_length=30, blank=True, null=True, db_column='儿茶素二', verbose_name='儿茶素二')
    kalubabi = models.CharField(max_length=30, blank=True, null=True, db_column='抗轮斑病', verbose_name='抗轮斑病')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    shga = models.CharField(max_length=30, blank=True, null=True, db_column='树高', verbose_name='树高')
    yechang = models.CharField(max_length=30, blank=True, null=True, db_column='叶长', verbose_name='叶长')
    huguzhji = models.CharField(max_length=30, blank=True, null=True, db_column='花冠直径', verbose_name='花冠直径')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    shenghuaqi = models.CharField(max_length=30, blank=True, null=True, db_column='盛花期', verbose_name='盛花期')
    anjisu = models.CharField(max_length=30, blank=True, null=True, db_column='氨基酸', verbose_name='氨基酸')
    xirushmu = models.CharField(max_length=30, blank=True, null=True, db_column='雄蕊数目', verbose_name='雄蕊数目')
    lvchzofe = models.CharField(max_length=30, blank=True, null=True, db_column='绿茶总分', verbose_name='绿茶总分')
    beshxi = models.CharField(max_length=30, blank=True, null=True, db_column='倍数性', verbose_name='倍数性')
    zifaroma = models.CharField(max_length=30, blank=True, null=True, db_column='子房茸毛', verbose_name='子房茸毛')
    shchlizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='生产力指数', verbose_name='生产力指数')
    bapiyowu = models.CharField(max_length=30, blank=True, null=True, db_column='苞片有无', verbose_name='苞片有无')
    fezhmidu = models.CharField(max_length=30, blank=True, null=True, db_column='分枝密度', verbose_name='分枝密度')
    yayeroma = models.CharField(max_length=30, blank=True, null=True, db_column='芽叶茸毛', verbose_name='芽叶茸毛')
    chchziwe = models.CharField(max_length=30, blank=True, null=True, db_column='成茶滋味', verbose_name='成茶滋味')
    jishxi = models.CharField(max_length=30, blank=True, null=True, db_column='结实性', verbose_name='结实性')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_茶'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class tonghao(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶长', verbose_name='叶长')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yeji = models.CharField(max_length=30, blank=True, null=True, db_column='叶角', verbose_name='叶角')
    yeku = models.CharField(max_length=30, blank=True, null=True, db_column='叶宽', verbose_name='叶宽')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    dazhzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株重', verbose_name='单株重')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_茼蒿'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class caomei(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    nezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='内质评价', verbose_name='内质评价')
    xiwe = models.CharField(max_length=30, blank=True, null=True, db_column='香味', verbose_name='香味')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    kedidisu = models.CharField(max_length=30, blank=True, null=True, db_column='可滴定酸', verbose_name='可滴定酸')
    daguzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='单果重评价', verbose_name='单果重评价')
    gushchshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果实成熟期', verbose_name='果实成熟期')
    chshqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期评价', verbose_name='成熟期评价')
    guze = models.CharField(max_length=30, blank=True, null=True, db_column='光泽', verbose_name='光泽')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    daguzhg = models.CharField(db_column='单果重G', max_length=30, blank=True, null=True, verbose_name='单果重G')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    zhye = models.CharField(max_length=30, blank=True, null=True, db_column='汁液', verbose_name='汁液')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    keroguxiwu = models.CharField(max_length=30, blank=True, null=True, db_column='可溶固形物', verbose_name='可溶固形物')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    keroxita = models.CharField(max_length=30, blank=True, null=True, db_column='可溶性糖', verbose_name='可溶性糖')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    gushyidu = models.CharField(max_length=30, blank=True, null=True, db_column='果实硬度', verbose_name='果实硬度')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    cashqi = models.CharField(db_column='采收期D', max_length=30, blank=True, null=True, verbose_name='采收期D')
    cashqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='采收期评价', verbose_name='采收期评价')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_草莓'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class lizhi(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    nezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='内质评价', verbose_name='内质评价')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    keshlv = models.CharField(db_column='可食率％', max_length=30, blank=True, null=True, verbose_name='可食率％')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    zhqidu = models.CharField(max_length=30, blank=True, null=True, db_column='整齐度', verbose_name='整齐度')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    gushchshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果实成熟期', verbose_name='果实成熟期')
    chshqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期评价', verbose_name='成熟期评价')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    gushzhye = models.CharField(max_length=30, blank=True, null=True, db_column='果实汁液', verbose_name='果实汁液')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    gushrozh = models.CharField(max_length=30, blank=True, null=True, db_column='果实肉质', verbose_name='果实肉质')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    keroguxiwu = models.CharField(max_length=30, blank=True, null=True, db_column='可溶固形物', verbose_name='可溶固形物')
    gushpiji = models.CharField(max_length=30, blank=True, null=True, db_column='果实评价', verbose_name='果实评价')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    gushdaguzh = models.CharField(max_length=30, blank=True, null=True, db_column='果实单果重', verbose_name='果实单果重')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    hasuli = models.CharField(db_column='含酸量％', max_length=30, blank=True, null=True, verbose_name='含酸量％')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    gushxiqi = models.CharField(max_length=30, blank=True, null=True, db_column='果实香气', verbose_name='果实香气')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_荔枝'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class qiaomai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    yiliansu = models.CharField(max_length=30, blank=True, null=True, db_column='异亮氨酸', verbose_name='异亮氨酸')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    lech = models.CharField(max_length=30, blank=True, null=True, db_column='棱翅', verbose_name='棱翅')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    weshsupp = models.CharField(db_column='维生素PP', max_length=30, blank=True, null=True, verbose_name='维生素PP')
    zhjijish = models.CharField(max_length=30, blank=True, null=True, db_column='主茎节数', verbose_name='主茎节数')
    las = models.CharField(max_length=30, blank=True, null=True, db_column='酪氨酸', verbose_name='酪氨酸')
    xi = models.CharField(max_length=30, blank=True, null=True, db_column='硒', verbose_name='硒')
    bebiansu = models.CharField(max_length=30, blank=True, null=True, db_column='苯丙氨酸', verbose_name='苯丙氨酸')
    zilixizh = models.CharField(max_length=30, blank=True, null=True, db_column='籽粒形状', verbose_name='籽粒形状')
    zhfa = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪', verbose_name='脂肪')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    li = models.CharField(max_length=30, blank=True, null=True, db_column='磷', verbose_name='磷')
    seansu = models.CharField(max_length=30, blank=True, null=True, db_column='色氨酸', verbose_name='色氨酸')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    zhzilayudi = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源地', verbose_name='种子来源地')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    naiasang = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    gaansu = models.CharField(max_length=30, blank=True, null=True, db_column='甘氨酸', verbose_name='甘氨酸')
    gukelv = models.CharField(max_length=30, blank=True, null=True, db_column='谷壳率', verbose_name='谷壳率')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    shyurish = models.CharField(max_length=30, blank=True, null=True, db_column='生育日数', verbose_name='生育日数')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    sang = models.CharField(max_length=30, blank=True, null=True, db_column='谷氨酸', verbose_name='谷氨酸')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='类型', verbose_name='类型')
    jiansu = models.CharField(max_length=30, blank=True, null=True, db_column='精氨酸', verbose_name='精氨酸')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    dafuxi = models.CharField(max_length=30, blank=True, null=True, db_column='倒伏性', verbose_name='倒伏性')
    zhjifezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='主茎分枝数', verbose_name='主茎分枝数')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    weshsu = models.CharField(db_column='维生素E', max_length=30, blank=True, null=True, verbose_name='维生素E')
    fugo = models.CharField(max_length=30, blank=True, null=True, db_column='腹沟', verbose_name='腹沟')
    ti = models.CharField(max_length=30, blank=True, null=True, db_column='铁', verbose_name='铁')
    fuansu = models.CharField(max_length=30, blank=True, null=True, db_column='脯氨酸', verbose_name='脯氨酸')
    ziliyase = models.CharField(max_length=30, blank=True, null=True, db_column='籽粒颜色', verbose_name='籽粒颜色')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    zuansu = models.CharField(max_length=30, blank=True, null=True, db_column='组氨酸', verbose_name='组氨酸')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    xiansu = models.CharField(max_length=30, blank=True, null=True, db_column='缬氨酸', verbose_name='缬氨酸')
    xing = models.CharField(max_length=30, blank=True, null=True, db_column='锌', verbose_name='锌')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    to = models.CharField(max_length=30, blank=True, null=True, db_column='铜', verbose_name='铜')
    dabazh = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    lulixi = models.CharField(max_length=30, blank=True, null=True, db_column='落粒性', verbose_name='落粒性')
    guangansu = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    liansu = models.CharField(max_length=30, blank=True, null=True, db_column='亮氨酸', verbose_name='亮氨酸')
    ga = models.CharField(max_length=30, blank=True, null=True, db_column='钙', verbose_name='钙')
    zohe = models.CharField(max_length=30, blank=True, null=True, db_column='总和', verbose_name='总和')
    dazhlizh = models.CharField(max_length=30, blank=True, null=True, db_column='单株粒重', verbose_name='单株粒重')
    me = models.CharField(max_length=30, blank=True, null=True, db_column='锰', verbose_name='锰')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_荞麦'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class laidou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    lajirish = models.CharField(max_length=30, blank=True, null=True, db_column='老荚日数', verbose_name='老荚日数')
    dajizh = models.CharField(max_length=30, blank=True, null=True, db_column='单荚重', verbose_name='单荚重')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    qijirish = models.CharField(max_length=30, blank=True, null=True, db_column='青荚日数', verbose_name='青荚日数')
    jixi = models.CharField(max_length=30, blank=True, null=True, db_column='荚形', verbose_name='荚形')
    jibixiwe = models.CharField(max_length=30, blank=True, null=True, db_column='荚壁纤维', verbose_name='荚壁纤维')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    nejicise = models.CharField(max_length=30, blank=True, null=True, db_column='嫩荚次色', verbose_name='嫩荚次色')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    yibacise = models.CharField(max_length=30, blank=True, null=True, db_column='翼瓣次色', verbose_name='翼瓣次色')
    zhzixizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子形状', verbose_name='种子形状')
    zhzipise = models.CharField(max_length=30, blank=True, null=True, db_column='种子皮色', verbose_name='种子皮色')
    zhpicise = models.CharField(max_length=30, blank=True, null=True, db_column='种皮次色', verbose_name='种皮次色')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    zhzidaxi = models.CharField(max_length=30, blank=True, null=True, db_column='种子大小', verbose_name='种子大小')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    yibase = models.CharField(max_length=30, blank=True, null=True, db_column='翼瓣色', verbose_name='翼瓣色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    nejise = models.CharField(max_length=30, blank=True, null=True, db_column='嫩荚色', verbose_name='嫩荚色')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    jiku = models.CharField(max_length=30, blank=True, null=True, db_column='荚宽', verbose_name='荚宽')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    jiho = models.CharField(max_length=30, blank=True, null=True, db_column='荚厚', verbose_name='荚厚')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_莱豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class caigua(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单瓜重', verbose_name='单瓜重')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    gumilafe = models.CharField(max_length=30, blank=True, null=True, db_column='瓜面腊粉', verbose_name='瓜面腊粉')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜皮色', verbose_name='商瓜皮色')
    lagucise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜次色', verbose_name='老瓜次色')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    lagubawe = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜斑纹', verbose_name='老瓜斑纹')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    lagupise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜皮色', verbose_name='老瓜皮色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='瓜形', verbose_name='瓜形')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    shgucise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜次色', verbose_name='商瓜次色')
    shcihuwe = models.CharField(max_length=30, blank=True, null=True, db_column='首雌花位', verbose_name='首雌花位')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shgubawe = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜斑纹', verbose_name='商瓜斑纹')
    gulexizh = models.CharField(max_length=30, blank=True, null=True, db_column='瓜棱形状', verbose_name='瓜棱形状')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_菜瓜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class caitai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    dizhqi = models.CharField(max_length=30, blank=True, null=True, db_column='定植期', verbose_name='定植期')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    yezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶长', verbose_name='叶长')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    shshqi = models.CharField(max_length=30, blank=True, null=True, db_column='始收期', verbose_name='始收期')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    zhtaga = models.CharField(max_length=30, blank=True, null=True, db_column='主薹高', verbose_name='主薹高')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    yemicima = models.CharField(max_length=30, blank=True, null=True, db_column='叶面刺毛', verbose_name='叶面刺毛')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')
    zhtacu = models.CharField(max_length=30, blank=True, null=True, db_column='主薹粗', verbose_name='主薹粗')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    moshqi = models.CharField(max_length=30, blank=True, null=True, db_column='末收期', verbose_name='末收期')
    xiwehali = models.CharField(max_length=30, blank=True, null=True, db_column='纤维含量', verbose_name='纤维含量')
    yelipi = models.CharField(max_length=30, blank=True, null=True, db_column='叶裂片', verbose_name='叶裂片')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    xumi = models.CharField(max_length=60, blank=True, null=True, db_column='学名', verbose_name='学名')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    yebiku = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄宽', verbose_name='叶柄宽')
    yelike = models.CharField(max_length=30, blank=True, null=True, db_column='叶裂刻', verbose_name='叶裂刻')
    hanbaixing = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    yebiho = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄厚', verbose_name='叶柄厚')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    dazhtash = models.CharField(max_length=30, blank=True, null=True, db_column='单株薹数', verbose_name='单株薹数')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    yeku = models.CharField(max_length=30, blank=True, null=True, db_column='叶宽', verbose_name='叶宽')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    yebizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄长', verbose_name='叶柄长')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    shzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='生长期', verbose_name='生长期')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_菜薹'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class caidou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kuwebikazh = models.CharField(max_length=30, blank=True, null=True, db_column='枯萎病抗指', verbose_name='枯萎病抗指')
    lajirish = models.CharField(max_length=30, blank=True, null=True, db_column='老荚日数', verbose_name='老荚日数')
    dajizh = models.CharField(max_length=30, blank=True, null=True, db_column='单荚重', verbose_name='单荚重')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shfe = models.CharField(max_length=30, blank=True, null=True, db_column='水分', verbose_name='水分')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    yimi = models.CharField(max_length=60, blank=True, null=True, db_column='译名', verbose_name='译名')
    qijirish = models.CharField(max_length=30, blank=True, null=True, db_column='青荚日数', verbose_name='青荚日数')
    jixi = models.CharField(max_length=30, blank=True, null=True, db_column='荚形', verbose_name='荚形')
    gazhdaba = models.CharField(max_length=30, blank=True, null=True, db_column='干重蛋白', verbose_name='干重蛋白')
    jibixiwe = models.CharField(max_length=30, blank=True, null=True, db_column='荚壁纤维', verbose_name='荚壁纤维')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    tajubikazh = models.CharField(max_length=30, blank=True, null=True, db_column='炭疽病抗指', verbose_name='炭疽病抗指')
    jiho = models.CharField(max_length=30, blank=True, null=True, db_column='荚厚', verbose_name='荚厚')
    yibacise = models.CharField(max_length=30, blank=True, null=True, db_column='翼瓣次色', verbose_name='翼瓣次色')
    zhzixizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子形状', verbose_name='种子形状')
    zhzipise = models.CharField(max_length=30, blank=True, null=True, db_column='种子皮色', verbose_name='种子皮色')
    zhpicise = models.CharField(max_length=30, blank=True, null=True, db_column='种皮次色', verbose_name='种皮次色')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    gazhxiwe = models.CharField(max_length=30, blank=True, null=True, db_column='干重纤维', verbose_name='干重纤维')
    zhzidaxi = models.CharField(max_length=30, blank=True, null=True, db_column='种子大小', verbose_name='种子大小')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    yibase = models.CharField(max_length=30, blank=True, null=True, db_column='翼瓣色', verbose_name='翼瓣色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    nejise = models.CharField(max_length=30, blank=True, null=True, db_column='嫩荚色', verbose_name='嫩荚色')
    xizhdaba = models.CharField(max_length=30, blank=True, null=True, db_column='鲜重蛋白', verbose_name='鲜重蛋白')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    jiku = models.CharField(max_length=30, blank=True, null=True, db_column='荚宽', verbose_name='荚宽')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    nejicise = models.CharField(max_length=30, blank=True, null=True, db_column='嫩荚次色', verbose_name='嫩荚次色')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    xizhxiwe = models.CharField(max_length=30, blank=True, null=True, db_column='鲜重纤维', verbose_name='鲜重纤维')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_菜豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class bocai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶长', verbose_name='叶长')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    yeku = models.CharField(max_length=30, blank=True, null=True, db_column='叶宽', verbose_name='叶宽')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    yebizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄长', verbose_name='叶柄长')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_菠菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class luobo(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    yemicima = models.CharField(max_length=30, blank=True, null=True, db_column='叶面刺毛', verbose_name='叶面刺毛')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    gedishpise = models.CharField(max_length=30, blank=True, null=True, db_column='根地上皮色', verbose_name='根地上皮色')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶型', verbose_name='叶型')
    gerokoga = models.CharField(max_length=30, blank=True, null=True, db_column='根肉口感', verbose_name='根肉口感')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    gedishbuzh = models.CharField(max_length=30, blank=True, null=True, db_column='根地上部长', verbose_name='根地上部长')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    yexing = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    rozhgezh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根长', verbose_name='肉质根长')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')
    gerozhse = models.CharField(max_length=30, blank=True, null=True, db_column='根肉主色', verbose_name='根肉主色')
    rozhgecu = models.CharField(max_length=30, blank=True, null=True, db_column='肉质根粗', verbose_name='肉质根粗')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='收获期', verbose_name='收获期')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    yepizh = models.CharField(max_length=30, blank=True, null=True, db_column='叶片长', verbose_name='叶片长')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    gexi = models.CharField(max_length=30, blank=True, null=True, db_column='根形', verbose_name='根形')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    geroshfe = models.CharField(max_length=30, blank=True, null=True, db_column='根肉水分', verbose_name='根肉水分')
    yecu = models.CharField(max_length=30, blank=True, null=True, db_column='叶簇', verbose_name='叶簇')
    yelike = models.CharField(max_length=30, blank=True, null=True, db_column='叶裂刻', verbose_name='叶裂刻')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    dagezh = models.CharField(max_length=30, blank=True, null=True, db_column='单根重', verbose_name='单根重')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    gerozh = models.CharField(max_length=30, blank=True, null=True, db_column='根肉质', verbose_name='根肉质')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    xilipidush = models.CharField(max_length=30, blank=True, null=True, db_column='小裂片对数', verbose_name='小裂片对数')
    naihanxing = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    gedixipise = models.CharField(max_length=30, blank=True, null=True, db_column='根地下皮色', verbose_name='根地下皮色')
    yepiku = models.CharField(max_length=30, blank=True, null=True, db_column='叶片宽', verbose_name='叶片宽')
    gerocise = models.CharField(max_length=30, blank=True, null=True, db_column='根肉次色', verbose_name='根肉次色')
    shzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='生长期', verbose_name='生长期')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_萝卜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class luokui(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_落葵'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class putao(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    nezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='内质评价', verbose_name='内质评价')
    keroxita = models.CharField(db_column='可溶性糖％', max_length=30, blank=True, null=True, verbose_name='可溶性糖％')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    gusuzhg = models.CharField(db_column='果穗重G', max_length=30, blank=True, null=True, verbose_name='果穗重G')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    zhle = models.CharField(max_length=30, blank=True, null=True, db_column='种类', verbose_name='种类')
    gushchshqi = models.CharField(max_length=30, blank=True, null=True, db_column='果实成熟期', verbose_name='果实成熟期')
    chshqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期评价', verbose_name='成熟期评价')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    zhye = models.CharField(max_length=30, blank=True, null=True, db_column='汁液', verbose_name='汁液')
    gulizhg = models.CharField(db_column='果粒重G', max_length=30, blank=True, null=True, verbose_name='果粒重G')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    gulizhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='果粒重评价', verbose_name='果粒重评价')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    keroguxiwu = models.CharField(max_length=30, blank=True, null=True, db_column='可溶固形物', verbose_name='可溶固形物')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    phzh = models.CharField(db_column='PH值', max_length=30, blank=True, null=True, verbose_name='PH值')
    gusuzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='果穗重评价', verbose_name='果穗重评价')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    kedidisu = models.CharField(db_column='可滴定酸％', max_length=30, blank=True, null=True, verbose_name='可滴定酸％')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_葡萄'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class bima(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    chdihulayu = models.CharField(max_length=30, blank=True, null=True, db_column='产地或来源', verbose_name='产地或来源')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    yoxisush = models.CharField(max_length=30, blank=True, null=True, db_column='有效穗数', verbose_name='有效穗数')
    zishhayolv = models.CharField(max_length=30, blank=True, null=True, db_column='子实含油率', verbose_name='子实含油率')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    yoxifezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='有效分枝数', verbose_name='有效分枝数')
    chrelv = models.CharField(max_length=30, blank=True, null=True, db_column='出仁率', verbose_name='出仁率')
    zhzixizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子形状', verbose_name='种子形状')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    zirehayolv = models.CharField(max_length=30, blank=True, null=True, db_column='子仁含油率', verbose_name='子仁含油率')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    zhpiyase = models.CharField(max_length=30, blank=True, null=True, db_column='种皮颜色', verbose_name='种皮颜色')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    zhjise = models.CharField(max_length=30, blank=True, null=True, db_column='主茎色', verbose_name='主茎色')
    lishxi = models.CharField(max_length=30, blank=True, null=True, db_column='裂蒴性', verbose_name='裂蒴性')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    gusuchdu = models.CharField(max_length=30, blank=True, null=True, db_column='果穗长度', verbose_name='果穗长度')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    shguyowuci = models.CharField(max_length=30, blank=True, null=True, db_column='蒴果有无刺', verbose_name='蒴果有无刺')
    xuyufafa = models.CharField(max_length=30, blank=True, null=True, db_column='选育方法', verbose_name='选育方法')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    sx = models.CharField(max_length=30, blank=True, null=True, db_column='穗形', verbose_name='穗形')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_蓖麻'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class wengcai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_蕹菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class yiyi(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    qita = models.CharField(max_length=30, blank=True, null=True, db_column='其他', verbose_name='其他')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    zhtose = models.CharField(max_length=30, blank=True, null=True, db_column='柱头色', verbose_name='柱头色')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    lebi = models.CharField(max_length=30, blank=True, null=True, db_column='类别', verbose_name='类别')
    chmiqi = models.CharField(max_length=30, blank=True, null=True, db_column='出苗期', verbose_name='出苗期')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    yoxifenish = models.CharField(max_length=30, blank=True, null=True, db_column='有效分蘖数', verbose_name='有效分蘖数')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    huyase = models.CharField(max_length=30, blank=True, null=True, db_column='花药色', verbose_name='花药色')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    xumi = models.CharField(max_length=50, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    yeqise = models.CharField(max_length=30, blank=True, null=True, db_column='叶鞘色', verbose_name='叶鞘色')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_薏苡'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class taigaicai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    jilawe = models.CharField(max_length=30, blank=True, null=True, db_column='芥辣味', verbose_name='芥辣味')
    dizhqi = models.CharField(max_length=30, blank=True, null=True, db_column='定植期', verbose_name='定植期')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    zhtase = models.CharField(max_length=30, blank=True, null=True, db_column='主薹色', verbose_name='主薹色')
    zhziqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子千粒重', verbose_name='种子千粒重')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    zhtaga = models.CharField(max_length=30, blank=True, null=True, db_column='主薹高', verbose_name='主薹高')
    kachxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗虫性', verbose_name='抗虫性')
    yemilafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶面蜡粉', verbose_name='叶面蜡粉')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    yemicima = models.CharField(max_length=30, blank=True, null=True, db_column='叶面刺毛', verbose_name='叶面刺毛')
    narexi = models.CharField(max_length=30, blank=True, null=True, db_column='耐热性', verbose_name='耐热性')
    zhtacu = models.CharField(max_length=30, blank=True, null=True, db_column='主薹粗', verbose_name='主薹粗')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    shhuqi = models.CharField(max_length=30, blank=True, null=True, db_column='收获期', verbose_name='收获期')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    yeyi = models.CharField(max_length=30, blank=True, null=True, db_column='叶翼', verbose_name='叶翼')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    xumi = models.CharField(max_length=50, blank=True, null=True, db_column='学名', verbose_name='学名')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    zhcaxi = models.CharField(max_length=30, blank=True, null=True, db_column='贮藏性', verbose_name='贮藏性')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐寒性', verbose_name='耐寒性')
    fenixi = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖性', verbose_name='分蘖性')
    yelike = models.CharField(max_length=30, blank=True, null=True, db_column='叶裂刻', verbose_name='叶裂刻')
    naihanxing = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    dazhtash = models.CharField(max_length=30, blank=True, null=True, db_column='单株薹数', verbose_name='单株薹数')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    xilipidush = models.CharField(max_length=30, blank=True, null=True, db_column='小裂片对数', verbose_name='小裂片对数')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    shzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='生长期', verbose_name='生长期')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_薹芥菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class taicai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yelipi = models.CharField(max_length=30, blank=True, null=True, db_column='叶裂片', verbose_name='叶裂片')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    zhta = models.CharField(max_length=30, blank=True, null=True, db_column='株态', verbose_name='株态')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    kabixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病性', verbose_name='抗病性')
    dach = models.CharField(max_length=30, blank=True, null=True, db_column='单产', verbose_name='单产')
    dazhzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株重', verbose_name='单株重')
    xumi = models.CharField(max_length=60, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    fazhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='繁种单位', verbose_name='繁种单位')
    zapeshqi = models.CharField(max_length=30, blank=True, null=True, db_column='栽培时期', verbose_name='栽培时期')
    shzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='生长期', verbose_name='生长期')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_薹菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class CaoLI(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    qita = models.CharField(max_length=30, blank=True, null=True, db_column='其它', verbose_name='其它')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    zhhuxuchdu = models.CharField(max_length=30, blank=True, null=True, db_column='主花序长度', verbose_name='主花序长度')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    huxuxi = models.CharField(max_length=30, blank=True, null=True, db_column='花序性', verbose_name='花序性')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    layudi = models.CharField(max_length=30, blank=True, null=True, db_column='来源地', verbose_name='来源地')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    lebi = models.CharField(max_length=30, blank=True, null=True, db_column='类别', verbose_name='类别')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    huxuse = models.CharField(max_length=30, blank=True, null=True, db_column='花序色', verbose_name='花序色')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_藜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class candou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yahabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病评价', verbose_name='蚜害病评价')
    yiliansu = models.CharField(max_length=30, blank=True, null=True, db_column='异亮氨酸', verbose_name='异亮氨酸')
    miansu = models.CharField(max_length=30, blank=True, null=True, db_column='酩氨酸', verbose_name='酩氨酸')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    dajilish = models.CharField(max_length=30, blank=True, null=True, db_column='单荚粒数', verbose_name='单荚粒数')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒型', verbose_name='粒型')
    chbabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='赤斑病评价', verbose_name='赤斑病评价')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    chbabiji = models.CharField(max_length=30, blank=True, null=True, db_column='赤斑病级', verbose_name='赤斑病级')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    xibizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='锈病指数', verbose_name='锈病指数')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    seansu = models.CharField(max_length=30, blank=True, null=True, db_column='色氨酸', verbose_name='色氨酸')
    yoxizh = models.CharField(max_length=30, blank=True, null=True, db_column='有效枝', verbose_name='有效枝')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    las = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    gaansu = models.CharField(max_length=30, blank=True, null=True, db_column='甘氨酸', verbose_name='甘氨酸')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    yahabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病指数', verbose_name='蚜害病指数')
    liansu = models.CharField(max_length=30, blank=True, null=True, db_column='亮氨酸', verbose_name='亮氨酸')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    hebabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='褐斑病评价', verbose_name='褐斑病评价')
    sang = models.CharField(max_length=30, blank=True, null=True, db_column='谷氨酸', verbose_name='谷氨酸')
    jiku = models.CharField(max_length=30, blank=True, null=True, db_column='荚宽', verbose_name='荚宽')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    lx = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    jiansu = models.CharField(max_length=30, blank=True, null=True, db_column='精氨酸', verbose_name='精氨酸')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    juyudu = models.CharField(max_length=30, blank=True, null=True, db_column='均匀度', verbose_name='均匀度')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    hebabiji = models.CharField(max_length=30, blank=True, null=True, db_column='褐斑病级', verbose_name='褐斑病级')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    xibibiji = models.CharField(max_length=30, blank=True, null=True, db_column='锈病病级', verbose_name='锈病病级')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    kalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗涝性', verbose_name='抗涝性')
    fuansu = models.CharField(max_length=30, blank=True, null=True, db_column='脯氨酸', verbose_name='脯氨酸')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    zuansu = models.CharField(max_length=30, blank=True, null=True, db_column='组氨酸', verbose_name='组氨酸')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yaqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='芽期耐盐', verbose_name='芽期耐盐')
    xiansu = models.CharField(max_length=30, blank=True, null=True, db_column='缬氨酸', verbose_name='缬氨酸')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yahabiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病级', verbose_name='蚜害病级')
    xibipiji = models.CharField(max_length=30, blank=True, null=True, db_column='锈病评价', verbose_name='锈病评价')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    hebabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='褐斑病指数', verbose_name='褐斑病指数')
    bebiansu = models.CharField(max_length=30, blank=True, null=True, db_column='苯丙氨酸', verbose_name='苯丙氨酸')
    yueguang = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    chbabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='赤斑病指数', verbose_name='赤斑病指数')
    zohe = models.CharField(max_length=30, blank=True, null=True, db_column='总和', verbose_name='总和')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    miqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='苗期耐盐', verbose_name='苗期耐盐')
    sx = models.CharField(max_length=30, blank=True, null=True, db_column='穗形', verbose_name='穗形')
    suananlao = models.CharField(max_length=30, blank=True, null=True, db_column='酪氨酸', verbose_name='酪氨酸')
    subizh = models.CharField(max_length=30, blank=True, null=True, db_column='穗柄长', verbose_name='穗柄长')
    dabazh = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    laanzhdaba = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨占蛋白', verbose_name='赖氨占蛋白')
    zhfa = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪', verbose_name='脂肪')
    chdu = models.CharField(max_length=30, blank=True, null=True, db_column='锤度', verbose_name='锤度')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    layudi = models.CharField(max_length=30, blank=True, null=True, db_column='来源地', verbose_name='来源地')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    fenixi = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖性', verbose_name='分蘖性')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    yirushji = models.CharField(max_length=30, blank=True, null=True, db_column='引入时间', verbose_name='引入时间')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    sihesubilv = models.CharField(max_length=30, blank=True, null=True, db_column='丝黑穗病率', verbose_name='丝黑穗病率')
    gujikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='灌浆抗寒性', verbose_name='灌浆抗寒性')
    gach = models.CharField(max_length=30, blank=True, null=True, db_column='高程', verbose_name='高程')
    shfe = models.CharField(max_length=30, blank=True, null=True, db_column='水份', verbose_name='水份')
    yikebapidu = models.CharField(max_length=30, blank=True, null=True, db_column='颖壳包皮度', verbose_name='颖壳包皮度')
    yomise = models.CharField(max_length=30, blank=True, null=True, db_column='幼苗色', verbose_name='幼苗色')
    kese = models.CharField(max_length=30, blank=True, null=True, db_column='壳色', verbose_name='壳色')
    miqikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='苗期抗寒性', verbose_name='苗期抗寒性')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_蚕豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class shegua(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单瓜重', verbose_name='单瓜重')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    gumilafe = models.CharField(max_length=30, blank=True, null=True, db_column='瓜面腊粉', verbose_name='瓜面腊粉')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜皮色', verbose_name='商瓜皮色')
    lagucise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜次色', verbose_name='老瓜次色')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    lagubawe = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜斑纹', verbose_name='老瓜斑纹')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    lagupise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜皮色', verbose_name='老瓜皮色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='瓜形', verbose_name='瓜形')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    shgucise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜次色', verbose_name='商瓜次色')
    shcihuwe = models.CharField(max_length=30, blank=True, null=True, db_column='首雌花位', verbose_name='首雌花位')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shgubawe = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜斑纹', verbose_name='商瓜斑纹')
    gulexizh = models.CharField(max_length=30, blank=True, null=True, db_column='瓜棱形状', verbose_name='瓜棱形状')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_蛇瓜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class xigua(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    lagubawe = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜斑纹', verbose_name='老瓜斑纹')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    shgucise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜次色', verbose_name='商瓜次色')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='瓜形', verbose_name='瓜形')
    gulexizh = models.CharField(max_length=30, blank=True, null=True, db_column='瓜棱形状', verbose_name='瓜棱形状')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜皮色', verbose_name='商瓜皮色')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单瓜重', verbose_name='单瓜重')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    lagupise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜皮色', verbose_name='老瓜皮色')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    lagucise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜次色', verbose_name='老瓜次色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    gumilafe = models.CharField(max_length=30, blank=True, null=True, db_column='瓜面腊粉', verbose_name='瓜面腊粉')
    shgubawe = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜斑纹', verbose_name='商瓜斑纹')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    cishhujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='雌首花节位', verbose_name='雌首花节位')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_西瓜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class xihulu(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    lagubawe = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜斑纹', verbose_name='老瓜斑纹')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    shgucise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜次色', verbose_name='商瓜次色')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='瓜形', verbose_name='瓜形')
    gulexizh = models.CharField(max_length=30, blank=True, null=True, db_column='瓜棱形状', verbose_name='瓜棱形状')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜皮色', verbose_name='商瓜皮色')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单瓜重', verbose_name='单瓜重')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    lagupise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜皮色', verbose_name='老瓜皮色')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    lagucise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜次色', verbose_name='老瓜次色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    gumilafe = models.CharField(max_length=30, blank=True, null=True, db_column='瓜面腊粉', verbose_name='瓜面腊粉')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    shgubawe = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜斑纹', verbose_name='商瓜斑纹')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    cishhujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='雌首花节位', verbose_name='雌首花节位')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_西葫芦'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class guzi(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    bafabikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='白发病抗性', verbose_name='白发病抗性')
    guxiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='谷锈严重度', verbose_name='谷锈严重度')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    zhjichdu = models.CharField(max_length=30, blank=True, null=True, db_column='主茎长度', verbose_name='主茎长度')
    laanzhdaba = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨占蛋白', verbose_name='赖氨占蛋白')
    mise = models.CharField(max_length=30, blank=True, null=True, db_column='米色', verbose_name='米色')
    yibehazhsh = models.CharField(max_length=30, blank=True, null=True, db_column='蝇被害指数', verbose_name='蝇被害指数')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    yomiqise = models.CharField(max_length=30, blank=True, null=True, db_column='幼苗鞘色', verbose_name='幼苗鞘色')
    vb = models.CharField(db_column='VB1', max_length=30, blank=True, null=True, verbose_name='VB1')
    dazhsuzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株穗重', verbose_name='单株穗重')
    zhsuchdu = models.CharField(max_length=30, blank=True, null=True, db_column='主穗长度', verbose_name='主穗长度')
    yumimikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='玉米螟抗性', verbose_name='玉米螟抗性')
    two_zhfasu = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪酸182', verbose_name='脂肪酸182')
    laanzhyapi = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨占样品', verbose_name='赖氨占样品')
    sx = models.CharField(max_length=30, blank=True, null=True, db_column='穗型', verbose_name='穗型')
    three_zhfasu = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪酸183', verbose_name='脂肪酸183')
    twovb = models.CharField(db_column='VB2', max_length=30, blank=True, null=True, verbose_name='VB2')
    fenish = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖数', verbose_name='分蘖数')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yumimijibi = models.CharField(max_length=30, blank=True, null=True, db_column='玉米螟级别', verbose_name='玉米螟级别')
    chsurish = models.CharField(max_length=30, blank=True, null=True, db_column='抽穗日数', verbose_name='抽穗日数')
    bafabibilv = models.CharField(max_length=30, blank=True, null=True, db_column='白发病病率', verbose_name='白发病病率')
    doji = models.CharField(max_length=30, blank=True, null=True, db_column='东经', verbose_name='东经')
    one = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪酸181', verbose_name='脂肪酸181')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    guxifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='谷锈反应型', verbose_name='谷锈反应型')
    guwebijibi = models.CharField(max_length=30, blank=True, null=True, db_column='谷瘟病级别', verbose_name='谷瘟病级别')
    qu = models.CharField(max_length=30, blank=True, null=True, db_column='区', verbose_name='区')
    zero_zhfasu = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪酸180', verbose_name='脂肪酸180')
    yikaxijibi = models.CharField(max_length=30, blank=True, null=True, db_column='蝇抗性级别', verbose_name='蝇抗性级别')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    kahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱性', verbose_name='抗旱性')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    xi = models.CharField(max_length=30, blank=True, null=True, db_column='硒', verbose_name='硒')
    bewe = models.CharField(max_length=30, blank=True, null=True, db_column='北纬', verbose_name='北纬')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    hesubilv = models.CharField(max_length=30, blank=True, null=True, db_column='黑穗病率', verbose_name='黑穗病率')
    yomiyese = models.CharField(max_length=30, blank=True, null=True, db_column='幼苗叶色', verbose_name='幼苗叶色')
    yibehazhlv = models.CharField(max_length=30, blank=True, null=True, db_column='蝇被害株率', verbose_name='蝇被害株率')
    dazhgazh = models.CharField(max_length=30, blank=True, null=True, db_column='单株秆重', verbose_name='单株秆重')
    cimachdu = models.CharField(max_length=30, blank=True, null=True, db_column='刺毛长度', verbose_name='刺毛长度')
    xichbizh = models.CharField(max_length=30, blank=True, null=True, db_column='线虫病指', verbose_name='线虫病指')
    susoji = models.CharField(max_length=30, blank=True, null=True, db_column='穗松紧', verbose_name='穗松紧')
    guwebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='谷瘟病抗性', verbose_name='谷瘟病抗性')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    dazhlizh = models.CharField(max_length=30, blank=True, null=True, db_column='单株粒重', verbose_name='单株粒重')
    zhjijish = models.CharField(max_length=30, blank=True, null=True, db_column='主茎节数', verbose_name='主茎节数')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    jinuxi = models.CharField(max_length=30, blank=True, null=True, db_column='粳糯性', verbose_name='粳糯性')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    bafabibiji = models.CharField(max_length=30, blank=True, null=True, db_column='白发病病级', verbose_name='白发病病级')
    zhjizhji = models.CharField(max_length=30, blank=True, null=True, db_column='主茎直径', verbose_name='主茎直径')
    v = models.CharField(db_column='VE', max_length=30, blank=True, null=True, verbose_name='VE')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    sumayipiji = models.CharField(max_length=30, blank=True, null=True, db_column='粟芒蝇评价', verbose_name='粟芒蝇评价')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    gach = models.CharField(max_length=30, blank=True, null=True, db_column='高程', verbose_name='高程')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    yizhjish = models.CharField(max_length=30, blank=True, null=True, db_column='一株茎数', verbose_name='一株茎数')
    zhfasu20 = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪酸200', verbose_name='脂肪酸200')
    zhfasu16 = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪酸160', verbose_name='脂肪酸160')
    xings = models.CharField(max_length=30, blank=True, null=True, db_column='穗形', verbose_name='穗形')
    yexifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='叶锈反应型', verbose_name='叶锈反应型')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    shyurish = models.CharField(max_length=30, blank=True, null=True, db_column='生育日数', verbose_name='生育日数')
    subizh = models.CharField(max_length=30, blank=True, null=True, db_column='穗柄长', verbose_name='穗柄长')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    mixi = models.CharField(max_length=30, blank=True, null=True, db_column='米香', verbose_name='米香')
    shsulv = models.CharField(max_length=30, blank=True, null=True, db_column='双穗率', verbose_name='双穗率')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    chmebibisu = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病病穗', verbose_name='赤霉病病穗')
    babefesh = models.CharField(max_length=30, blank=True, null=True, db_column='白背飞虱', verbose_name='白背飞虱')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    chdu = models.CharField(max_length=30, blank=True, null=True, db_column='锤度', verbose_name='锤度')
    tixifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='条锈反应型', verbose_name='条锈反应型')
    xiji = models.CharField(max_length=30, blank=True, null=True, db_column='籼粳', verbose_name='籼粳')
    balilv = models.CharField(max_length=30, blank=True, null=True, db_column='爆裂率', verbose_name='爆裂率')
    layudi = models.CharField(max_length=30, blank=True, null=True, db_column='来源地', verbose_name='来源地')
    gaxiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈严重度', verbose_name='秆锈严重度')
    miwe = models.CharField(max_length=30, blank=True, null=True, db_column='苗瘟', verbose_name='苗瘟')
    yaqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='芽期抗寒', verbose_name='芽期抗寒')
    fenixi = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖性', verbose_name='分蘖性')
    ma = models.CharField(max_length=30, blank=True, null=True, db_column='芒', verbose_name='芒')
    miqinaha = models.CharField(max_length=30, blank=True, null=True, db_column='苗期耐旱', verbose_name='苗期耐旱')
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    najixi = models.CharField(max_length=30, blank=True, null=True, db_column='耐瘠性', verbose_name='耐瘠性')
    tijikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='田间抗寒性', verbose_name='田间抗寒性')
    jimilv = models.CharField(max_length=30, blank=True, null=True, db_column='精米率', verbose_name='精米率')
    hushxisu = models.CharField(max_length=30, blank=True, null=True, db_column='花生稀酸', verbose_name='花生稀酸')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    gaxifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈反应型', verbose_name='秆锈反应型')
    zhkubi = models.CharField(max_length=30, blank=True, null=True, db_column='长宽比', verbose_name='长宽比')
    sihesubilv = models.CharField(max_length=30, blank=True, null=True, db_column='丝黑穗病率', verbose_name='丝黑穗病率')
    gujikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='灌浆抗寒性', verbose_name='灌浆抗寒性')
    sulish = models.CharField(max_length=30, blank=True, null=True, db_column='穗粒数', verbose_name='穗粒数')
    chsuqi = models.CharField(max_length=30, blank=True, null=True, db_column='出穗期', verbose_name='出穗期')
    dabapiji = models.CharField(max_length=30, blank=True, null=True, db_column='大斑评价', verbose_name='大斑评价')
    shfe = models.CharField(max_length=30, blank=True, null=True, db_column='水份', verbose_name='水份')
    kese = models.CharField(max_length=30, blank=True, null=True, db_column='壳色', verbose_name='壳色')
    yijise = models.CharField(max_length=30, blank=True, null=True, db_column='颖尖色', verbose_name='颖尖色')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    chdizh = models.CharField(max_length=30, blank=True, null=True, db_column='沉淀值', verbose_name='沉淀值')
    zazhwa = models.CharField(max_length=30, blank=True, null=True, db_column='早中晚', verbose_name='早中晚')
    tijidababi = models.CharField(max_length=30, blank=True, null=True, db_column='田间大斑病', verbose_name='田间大斑病')
    yikebapidu = models.CharField(max_length=30, blank=True, null=True, db_column='颖壳包皮度', verbose_name='颖壳包皮度')
    chmebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病抗性', verbose_name='赤霉病抗性')
    bacudawe_2 = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位_2', verbose_name='保存单位_2')
    zhjiyepish = models.CharField(max_length=30, blank=True, null=True, db_column='主茎叶片数', verbose_name='主茎叶片数')
    shbiha = models.CharField(max_length=30, blank=True, null=True, db_column='省编号', verbose_name='省编号')
    bafefayixi = models.CharField(max_length=30, blank=True, null=True, db_column='白粉反应型', verbose_name='白粉反应型')
    wekubi = models.CharField(max_length=30, blank=True, null=True, db_column='纹枯病', verbose_name='纹枯病')
    feyusheng = models.CharField(max_length=30, blank=True, null=True, db_column='α生育酚', verbose_name='α生育酚')
    yomise = models.CharField(max_length=30, blank=True, null=True, db_column='幼苗色', verbose_name='幼苗色')
    dochxi = models.CharField(max_length=30, blank=True, null=True, db_column='冬春性', verbose_name='冬春性')
    yijiwazh = models.CharField(max_length=30, blank=True, null=True, db_column='颖尖弯直', verbose_name='颖尖弯直')
    tijixibabi = models.CharField(max_length=30, blank=True, null=True, db_column='田间小斑病', verbose_name='田间小斑病')
    dafuxi = models.CharField(max_length=30, blank=True, null=True, db_column='倒伏性', verbose_name='倒伏性')
    chmebibizh = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病病指', verbose_name='赤霉病病指')
    fafajizuhe = models.CharField(max_length=30, blank=True, null=True, db_column='方法及组合', verbose_name='方法及组合')
    shqikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟期抗寒性', verbose_name='熟期抗寒性')
    yirushji = models.CharField(max_length=30, blank=True, null=True, db_column='引入时间', verbose_name='引入时间')
    yuchnixi = models.CharField(max_length=30, blank=True, null=True, db_column='育成年限', verbose_name='育成年限')
    mazh = models.CharField(max_length=30, blank=True, null=True, db_column='芒长', verbose_name='芒长')
    tijihefebi = models.CharField(max_length=30, blank=True, null=True, db_column='田间黑粉病', verbose_name='田间黑粉病')
    miqikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='苗期抗寒性', verbose_name='苗期抗寒性')
    gefusubiji = models.CharField(max_length=30, blank=True, null=True, db_column='根腐穗病级', verbose_name='根腐穗病级')
    camilv = models.CharField(max_length=30, blank=True, null=True, db_column='糙米率', verbose_name='糙米率')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_谷子'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class doushu(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    jixi = models.CharField(max_length=30, blank=True, null=True, db_column='荚形', verbose_name='荚形')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    dajizh = models.CharField(max_length=30, blank=True, null=True, db_column='单荚重', verbose_name='单荚重')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_豆薯'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class jiangdou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    yahabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病评价', verbose_name='蚜害病评价')
    yiliansu = models.CharField(max_length=30, blank=True, null=True, db_column='异亮氨酸', verbose_name='异亮氨酸')
    miansu = models.CharField(max_length=30, blank=True, null=True, db_column='酩氨酸', verbose_name='酩氨酸')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    dajilish = models.CharField(max_length=30, blank=True, null=True, db_column='单荚粒数', verbose_name='单荚粒数')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    yebabiji = models.CharField(max_length=30, blank=True, null=True, db_column='叶斑病级', verbose_name='叶斑病级')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    xibizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='锈病指数', verbose_name='锈病指数')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    yebabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='叶斑病指数', verbose_name='叶斑病指数')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    seansu = models.CharField(max_length=30, blank=True, null=True, db_column='色氨酸', verbose_name='色氨酸')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    yueguang = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    naias = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    gaansu = models.CharField(max_length=30, blank=True, null=True, db_column='甘氨酸', verbose_name='甘氨酸')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    sang = models.CharField(max_length=30, blank=True, null=True, db_column='谷氨酸', verbose_name='谷氨酸')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    yebabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='叶斑病评价', verbose_name='叶斑病评价')
    shqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='熟期抗旱', verbose_name='熟期抗旱')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    zuansu = models.CharField(max_length=30, blank=True, null=True, db_column='组氨酸', verbose_name='组氨酸')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    xibiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='锈病严重度', verbose_name='锈病严重度')
    qihuse = models.CharField(max_length=30, blank=True, null=True, db_column='脐环色', verbose_name='脐环色')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    xibipubilv = models.CharField(max_length=30, blank=True, null=True, db_column='锈病普遍率', verbose_name='锈病普遍率')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    fuansu = models.CharField(max_length=30, blank=True, null=True, db_column='脯氨酸', verbose_name='脯氨酸')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    yaqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='芽期抗旱', verbose_name='芽期抗旱')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yaqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='芽期耐盐', verbose_name='芽期耐盐')
    xiansu = models.CharField(max_length=30, blank=True, null=True, db_column='缬氨酸', verbose_name='缬氨酸')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    xibipiji = models.CharField(max_length=30, blank=True, null=True, db_column='锈病评价', verbose_name='锈病评价')
    yahabiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病级', verbose_name='蚜害病级')
    bebiansu = models.CharField(max_length=30, blank=True, null=True, db_column='苯丙氨酸', verbose_name='苯丙氨酸')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    liansu = models.CharField(max_length=30, blank=True, null=True, db_column='亮氨酸', verbose_name='亮氨酸')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    zohe = models.CharField(max_length=30, blank=True, null=True, db_column='总和', verbose_name='总和')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    jiansu = models.CharField(max_length=30, blank=True, null=True, db_column='精氨酸', verbose_name='精氨酸')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    miqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='苗期耐盐', verbose_name='苗期耐盐')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_豇豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class wandou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    miansu = models.CharField(max_length=30, blank=True, null=True, db_column='酩氨酸', verbose_name='酩氨酸')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    yueguang = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    jixi = models.CharField(max_length=30, blank=True, null=True, db_column='荚型', verbose_name='荚型')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    bafebipiji = models.CharField(max_length=30, blank=True, null=True, db_column='白粉病评价', verbose_name='白粉病评价')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    seansu = models.CharField(max_length=30, blank=True, null=True, db_column='色氨酸', verbose_name='色氨酸')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    dajilish = models.CharField(max_length=30, blank=True, null=True, db_column='单荚粒数', verbose_name='单荚粒数')
    gaansu = models.CharField(max_length=30, blank=True, null=True, db_column='甘氨酸', verbose_name='甘氨酸')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    sang = models.CharField(max_length=30, blank=True, null=True, db_column='谷氨酸', verbose_name='谷氨酸')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    yuchnife = models.CharField(max_length=30, blank=True, null=True, db_column='育成年份', verbose_name='育成年份')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    shqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='熟期抗旱', verbose_name='熟期抗旱')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    xuyudawe = models.CharField(max_length=30, blank=True, null=True, db_column='选育单位', verbose_name='选育单位')
    naias = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    zuansu = models.CharField(max_length=30, blank=True, null=True, db_column='组氨酸', verbose_name='组氨酸')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    pzname = models.CharField(max_length=50, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yiliansu = models.CharField(max_length=30, blank=True, null=True, db_column='异亮氨酸', verbose_name='异亮氨酸')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    bafebiji = models.CharField(max_length=30, blank=True, null=True, db_column='白粉病级', verbose_name='白粉病级')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    xibibiji = models.CharField(max_length=30, blank=True, null=True, db_column='锈病病级', verbose_name='锈病病级')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    fuansu = models.CharField(max_length=30, blank=True, null=True, db_column='脯氨酸', verbose_name='脯氨酸')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    yaqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='芽期抗旱', verbose_name='芽期抗旱')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yaqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='芽期耐盐', verbose_name='芽期耐盐')
    xiansu = models.CharField(max_length=30, blank=True, null=True, db_column='缬氨酸', verbose_name='缬氨酸')
    bafebizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='白粉病指数', verbose_name='白粉病指数')
    yahabiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病级', verbose_name='蚜害病级')
    xibipiji = models.CharField(max_length=30, blank=True, null=True, db_column='锈病评价', verbose_name='锈病评价')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    yahabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病评价', verbose_name='蚜害病评价')
    bebiansu = models.CharField(max_length=30, blank=True, null=True, db_column='苯丙氨酸', verbose_name='苯丙氨酸')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    liansu = models.CharField(max_length=30, blank=True, null=True, db_column='亮氨酸', verbose_name='亮氨酸')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    zohe = models.CharField(max_length=30, blank=True, null=True, db_column='总和', verbose_name='总和')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    jiansu = models.CharField(max_length=30, blank=True, null=True, db_column='精氨酸', verbose_name='精氨酸')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    miqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='苗期耐盐', verbose_name='苗期耐盐')
    yahabizh = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病指', verbose_name='蚜害病指')
    las = models.CharField(max_length=30, blank=True, null=True, db_column='酪氨酸', verbose_name='酪氨酸')
    lx = models.CharField(max_length=30, blank=True, null=True, db_column='粒型', verbose_name='粒型')
    jicudaxi = models.CharField(max_length=30, blank=True, null=True, db_column='茎粗大小', verbose_name='茎粗大小')
    yexifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='叶锈反应型', verbose_name='叶锈反应型')
    dabazh = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    hebabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='褐斑病指数', verbose_name='褐斑病指数')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    zhfa = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪', verbose_name='脂肪')
    chbabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='赤斑病指数', verbose_name='赤斑病指数')
    layu = models.CharField(max_length=30, blank=True, null=True, db_column='来源', verbose_name='来源')
    bewe = models.CharField(max_length=30, blank=True, null=True, db_column='北纬', verbose_name='北纬')
    yahabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病指数', verbose_name='蚜害病指数')
    xikeroxita = models.CharField(max_length=30, blank=True, null=True, db_column='鲜可溶性糖', verbose_name='鲜可溶性糖')
    tixifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='条锈反应型', verbose_name='条锈反应型')
    juyudu = models.CharField(max_length=30, blank=True, null=True, db_column='均匀度', verbose_name='均匀度')
    shrose = models.CharField(max_length=30, blank=True, null=True, db_column='薯肉色', verbose_name='薯肉色')
    chmebibisu = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病病穗', verbose_name='赤霉病病穗')
    xibizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='锈病指数', verbose_name='锈病指数')
    diyese = models.CharField(max_length=30, blank=True, null=True, db_column='顶叶色', verbose_name='顶叶色')
    ma = models.CharField(max_length=30, blank=True, null=True, db_column='芒', verbose_name='芒')
    yoxizh = models.CharField(max_length=30, blank=True, null=True, db_column='有效枝', verbose_name='有效枝')
    majise = models.CharField(max_length=30, blank=True, null=True, db_column='脉基色', verbose_name='脉基色')
    tijikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='田间抗寒性', verbose_name='田间抗寒性')
    kalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗涝性', verbose_name='抗涝性')
    xicudaba = models.CharField(max_length=30, blank=True, null=True, db_column='鲜粗蛋白', verbose_name='鲜粗蛋白')
    gaxifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈反应型', verbose_name='秆锈反应型')
    chbabiji = models.CharField(max_length=30, blank=True, null=True, db_column='赤斑病级', verbose_name='赤斑病级')
    nayaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐盐性', verbose_name='耐盐性')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    hebabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='褐斑病评价', verbose_name='褐斑病评价')
    bijise = models.CharField(max_length=30, blank=True, null=True, db_column='柄基色', verbose_name='柄基色')
    gach = models.CharField(max_length=30, blank=True, null=True, db_column='高程', verbose_name='高程')
    shxi = models.CharField(db_column='\r\n\r\n熟性', max_length=30, blank=True, null=True, verbose_name='\r\n\r\n熟性')
    nazhxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐贮性', verbose_name='耐贮性')
    chdizh = models.CharField(max_length=30, blank=True, null=True, db_column='沉淀值', verbose_name='沉淀值')
    shux = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    hogalv = models.CharField(max_length=30, blank=True, null=True, db_column='烘干率', verbose_name='烘干率')
    chmebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病抗性', verbose_name='赤霉病抗性')
    jiku = models.CharField(max_length=30, blank=True, null=True, db_column='荚宽', verbose_name='荚宽')
    chli = models.CharField(max_length=30, blank=True, null=True, db_column='产量', verbose_name='产量')
    doji = models.CharField(max_length=30, blank=True, null=True, db_column='东经', verbose_name='东经')
    hebabiji = models.CharField(max_length=30, blank=True, null=True, db_column='褐斑病级', verbose_name='褐斑病级')
    jiduroma = models.CharField(max_length=30, blank=True, null=True, db_column='茎端茸毛', verbose_name='茎端茸毛')
    dochxi = models.CharField(max_length=30, blank=True, null=True, db_column='冬春性', verbose_name='冬春性')
    chbabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='赤斑病评价', verbose_name='赤斑病评价')
    yepiku = models.CharField(max_length=30, blank=True, null=True, db_column='叶片宽', verbose_name='叶片宽')
    chmebibizh = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病病指', verbose_name='赤霉病病指')
    jibufezh = models.CharField(max_length=30, blank=True, null=True, db_column='基部分枝', verbose_name='基部分枝')
    kese = models.CharField(max_length=30, blank=True, null=True, db_column='壳色', verbose_name='壳色')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    gefusubiji = models.CharField(max_length=30, blank=True, null=True, db_column='根腐穗病级', verbose_name='根腐穗病级')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_豌豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class yuegua(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    lagubawe = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜斑纹', verbose_name='老瓜斑纹')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    shgucise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜次色', verbose_name='商瓜次色')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='瓜形', verbose_name='瓜形')
    gulexizh = models.CharField(max_length=30, blank=True, null=True, db_column='瓜棱形状', verbose_name='瓜棱形状')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜皮色', verbose_name='商瓜皮色')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单瓜重', verbose_name='单瓜重')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    lagupise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜皮色', verbose_name='老瓜皮色')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    lagucise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜次色', verbose_name='老瓜次色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    gumilafe = models.CharField(max_length=30, blank=True, null=True, db_column='瓜面腊粉', verbose_name='瓜面腊粉')
    shgubawe = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜斑纹', verbose_name='商瓜斑纹')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    cishhujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='雌首花节位', verbose_name='雌首花节位')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_越瓜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class lajiao(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    tajubizh = models.CharField(max_length=30, blank=True, null=True, db_column='炭疽病指', verbose_name='炭疽病指')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    zhgufaxi = models.CharField(max_length=30, blank=True, null=True, db_column='着果方向', verbose_name='着果方向')
    shshgupise = models.CharField(max_length=30, blank=True, null=True, db_column='食熟果皮色', verbose_name='食熟果皮色')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    cmbizh = models.CharField(db_column='CMV病指', max_length=30, blank=True, null=True, verbose_name='CMV病指')
    cmfabilv = models.CharField(db_column='CMV发病率', max_length=30, blank=True, null=True, verbose_name='CMV发病率')
    guroho = models.CharField(max_length=30, blank=True, null=True, db_column='果肉厚', verbose_name='果肉厚')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    tmfabilv = models.CharField(db_column='TMV发病率', max_length=30, blank=True, null=True, verbose_name='TMV发病率')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    lashzhguse = models.CharField(max_length=30, blank=True, null=True, db_column='老熟种果色', verbose_name='老熟种果色')
    wapibaho = models.CharField(max_length=30, blank=True, null=True, db_column='外皮薄厚', verbose_name='外皮薄厚')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单果重', verbose_name='单果重')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    shhujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='首花节位', verbose_name='首花节位')
    tmbizh = models.CharField(db_column='TMV病指', max_length=30, blank=True, null=True, verbose_name='TMV病指')
    gushshfe = models.CharField(max_length=30, blank=True, null=True, db_column='果实水分', verbose_name='果实水分')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    gawuzh = models.CharField(max_length=30, blank=True, null=True, db_column='干物质', verbose_name='干物质')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    lajisu = models.CharField(max_length=30, blank=True, null=True, db_column='辣椒素', verbose_name='辣椒素')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    tajufabilv = models.CharField(max_length=30, blank=True, null=True, db_column='炭疽发病率', verbose_name='炭疽发病率')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_辣椒'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class suanjiang(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    shhujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='始花节位', verbose_name='始花节位')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    guse = models.CharField(max_length=30, blank=True, null=True, db_column='果色', verbose_name='果色')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    zhzidush = models.CharField(max_length=30, blank=True, null=True, db_column='种子多少', verbose_name='种子多少')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单果重', verbose_name='单果重')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    zhfu = models.CharField(max_length=30, blank=True, null=True, db_column='株幅', verbose_name='株幅')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_酸浆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class jinhuacai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yeyu = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘', verbose_name='叶缘')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    yemi = models.CharField(max_length=30, blank=True, null=True, db_column='叶面', verbose_name='叶面')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_金花菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class zhangjiangdou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    lajirish = models.CharField(max_length=30, blank=True, null=True, db_column='老荚日数', verbose_name='老荚日数')
    dajizh = models.CharField(max_length=30, blank=True, null=True, db_column='单荚重', verbose_name='单荚重')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    qijirish = models.CharField(max_length=30, blank=True, null=True, db_column='青荚日数', verbose_name='青荚日数')
    jixi = models.CharField(max_length=30, blank=True, null=True, db_column='荚形', verbose_name='荚形')
    jibixiwe = models.CharField(max_length=30, blank=True, null=True, db_column='荚壁纤维', verbose_name='荚壁纤维')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    jiho = models.CharField(max_length=30, blank=True, null=True, db_column='荚厚', verbose_name='荚厚')
    yibacise = models.CharField(max_length=30, blank=True, null=True, db_column='翼瓣次色', verbose_name='翼瓣次色')
    zhzixizh = models.CharField(max_length=30, blank=True, null=True, db_column='种子形状', verbose_name='种子形状')
    zhzipise = models.CharField(max_length=30, blank=True, null=True, db_column='种子皮色', verbose_name='种子皮色')
    nejise = models.CharField(max_length=30, blank=True, null=True, db_column='嫩荚色', verbose_name='嫩荚色')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    zhzidaxi = models.CharField(max_length=30, blank=True, null=True, db_column='种子大小', verbose_name='种子大小')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    yibase = models.CharField(max_length=30, blank=True, null=True, db_column='翼瓣色', verbose_name='翼瓣色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    zhpicise = models.CharField(max_length=30, blank=True, null=True, db_column='种皮次色', verbose_name='种皮次色')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    jiku = models.CharField(max_length=30, blank=True, null=True, db_column='荚宽', verbose_name='荚宽')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    nejicise = models.CharField(max_length=30, blank=True, null=True, db_column='嫩荚次色', verbose_name='嫩荚次色')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_长豇豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class qingma(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    zhpise = models.CharField(max_length=30, blank=True, null=True, db_column='种皮色', verbose_name='种皮色')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    shyurish = models.CharField(max_length=30, blank=True, null=True, db_column='生育日数', verbose_name='生育日数')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    jijichdu = models.CharField(max_length=30, blank=True, null=True, db_column='节间长度', verbose_name='节间长度')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='茎色', verbose_name='茎色')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶型', verbose_name='叶型')
    jicu = models.CharField(max_length=30, blank=True, null=True, db_column='茎粗', verbose_name='茎粗')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_青麻'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class jiucai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    yelafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶蜡粉', verbose_name='叶蜡粉')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    yeqiyase = models.CharField(max_length=30, blank=True, null=True, db_column='叶鞘颜色', verbose_name='叶鞘颜色')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    xiqi = models.CharField(max_length=30, blank=True, null=True, db_column='香气', verbose_name='香气')
    yeta = models.CharField(max_length=30, blank=True, null=True, db_column='叶态', verbose_name='叶态')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    lawe = models.CharField(max_length=30, blank=True, null=True, db_column='辣味', verbose_name='辣味')
    yeku = models.CharField(max_length=30, blank=True, null=True, db_column='叶宽', verbose_name='叶宽')
    dazhzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株重', verbose_name='单株重')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    fenixi = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖性', verbose_name='分蘖性')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_韭菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class jiucong(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    yelafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶蜡粉', verbose_name='叶蜡粉')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    wapiseze = models.CharField(max_length=30, blank=True, null=True, db_column='外皮色泽', verbose_name='外皮色泽')
    shzhzhta = models.CharField(max_length=30, blank=True, null=True, db_column='生长状态', verbose_name='生长状态')
    xiqi = models.CharField(max_length=30, blank=True, null=True, db_column='香气', verbose_name='香气')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    yecu = models.CharField(max_length=30, blank=True, null=True, db_column='叶粗', verbose_name='叶粗')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    yezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶长', verbose_name='叶长')
    fenixi = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖性', verbose_name='分蘖性')
    lawe = models.CharField(max_length=30, blank=True, null=True, db_column='辣味', verbose_name='辣味')
    dazhzh = models.CharField(max_length=30, blank=True, null=True, db_column='单株重', verbose_name='单株重')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    huguse = models.CharField(max_length=30, blank=True, null=True, db_column='花冠色', verbose_name='花冠色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_韭葱'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class fandou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    sang = models.CharField(max_length=30, blank=True, null=True, db_column='谷氨酸', verbose_name='谷氨酸')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    jiansu = models.CharField(max_length=30, blank=True, null=True, db_column='精氨酸', verbose_name='精氨酸')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    zohe = models.CharField(max_length=30, blank=True, null=True, db_column='总和', verbose_name='总和')
    las = models.CharField(max_length=30, blank=True, null=True, db_column='酪氨酸', verbose_name='酪氨酸')
    yiliansu = models.CharField(max_length=30, blank=True, null=True, db_column='异亮氨酸', verbose_name='异亮氨酸')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    seansu = models.CharField(max_length=30, blank=True, null=True, db_column='色氨酸', verbose_name='色氨酸')
    zuansu = models.CharField(max_length=30, blank=True, null=True, db_column='组氨酸', verbose_name='组氨酸')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bebiansu = models.CharField(max_length=30, blank=True, null=True, db_column='苯丙氨酸', verbose_name='苯丙氨酸')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    yueguang = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    liansu = models.CharField(max_length=30, blank=True, null=True, db_column='亮氨酸', verbose_name='亮氨酸')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    gaansu = models.CharField(max_length=30, blank=True, null=True, db_column='甘氨酸', verbose_name='甘氨酸')
    dajilish = models.CharField(max_length=30, blank=True, null=True, db_column='单荚粒数', verbose_name='单荚粒数')
    xiansu = models.CharField(max_length=30, blank=True, null=True, db_column='缬氨酸', verbose_name='缬氨酸')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    fuansu = models.CharField(max_length=30, blank=True, null=True, db_column='脯氨酸', verbose_name='脯氨酸')
    naias = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_饭豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class JiaoXiang(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    nezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='内质评价', verbose_name='内质评价')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    gushsh = models.CharField(max_length=30, blank=True, null=True, db_column='果梳数', verbose_name='果梳数')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    zhqidu = models.CharField(max_length=30, blank=True, null=True, db_column='整齐度', verbose_name='整齐度')
    gushshpiji = models.CharField(max_length=30, blank=True, null=True, db_column='果梳数评价', verbose_name='果梳数评价')
    shyuqitish = models.CharField(max_length=30, blank=True, null=True, db_column='生育期天数', verbose_name='生育期天数')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    zota = models.CharField(db_column='总糖％', max_length=30, blank=True, null=True, verbose_name='总糖％')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    keroguxiwu = models.CharField(max_length=30, blank=True, null=True, db_column='可溶固形物', verbose_name='可溶固形物')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    shyuqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='生育期评价', verbose_name='生育期评价')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zosu = models.CharField(db_column='总酸％', max_length=30, blank=True, null=True, verbose_name='总酸％')
    guzhzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='果指长评价', verbose_name='果指长评价')
    guxiwupiji = models.CharField(max_length=30, blank=True, null=True, db_column='固形物评价', verbose_name='固形物评价')
    gusuzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='果穗长评价', verbose_name='果穗长评价')
    guzhzhcm = models.CharField(db_column='果指长CM', max_length=30, blank=True, null=True, verbose_name='果指长CM')
    gusuzhcm = models.CharField(db_column='果穗长CM', max_length=30, blank=True, null=True, verbose_name='果穗长CM')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    xizh = models.CharField(max_length=30, blank=True, null=True, db_column='形状', verbose_name='形状')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_香蕉'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class malingshu(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    tirajish = models.CharField(max_length=30, blank=True, null=True, db_column='天然结实', verbose_name='天然结实')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    pv = models.CharField(db_column='PVY', max_length=30, blank=True, null=True, verbose_name='PVY')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    fechxi = models.CharField(max_length=30, blank=True, null=True, db_column='丰产性', verbose_name='丰产性')
    wayibikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='晚疫病抗性', verbose_name='晚疫病抗性')
    daxi = models.CharField(max_length=30, blank=True, null=True, db_column='大小', verbose_name='大小')
    zhjididi = models.CharField(max_length=30, blank=True, null=True, db_column='征集地点', verbose_name='征集地点')
    difehali = models.CharField(max_length=30, blank=True, null=True, db_column='淀粉含量', verbose_name='淀粉含量')
    bidukagaxi = models.CharField(max_length=30, blank=True, null=True, db_column='病毒抗感性', verbose_name='病毒抗感性')
    zhshpizh = models.CharField(max_length=30, blank=True, null=True, db_column='蒸食品质', verbose_name='蒸食品质')
    rose = models.CharField(max_length=30, blank=True, null=True, db_column='肉色', verbose_name='肉色')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    xizh = models.CharField(max_length=30, blank=True, null=True, db_column='形状', verbose_name='形状')
    qibe = models.CharField(max_length=60, blank=True, null=True, db_column='亲本', verbose_name='亲本')
    pise = models.CharField(max_length=30, blank=True, null=True, db_column='皮色', verbose_name='皮色')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    nachxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐储性', verbose_name='耐储性')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    qita = models.CharField(max_length=30, blank=True, null=True, db_column='其它', verbose_name='其它')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    pizhlayu = models.CharField(max_length=30, blank=True, null=True, db_column='品种来源', verbose_name='品种来源')
    xpv = models.CharField(db_column='PVX', max_length=30, blank=True, null=True, verbose_name='PVX')
    piguhudu = models.CharField(max_length=30, blank=True, null=True, db_column='皮光滑度', verbose_name='皮光滑度')
    yayashqi = models.CharField(max_length=30, blank=True, null=True, db_column='芽眼深浅', verbose_name='芽眼深浅')
    solidawe = models.CharField(max_length=30, blank=True, null=True, db_column='送留单位', verbose_name='送留单位')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    zhqidu = models.CharField(max_length=30, blank=True, null=True, db_column='整齐度', verbose_name='整齐度')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_马铃薯'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class gaoliang(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    sx = models.CharField(max_length=30, blank=True, null=True, db_column='穗形', verbose_name='穗形')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    kahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱性', verbose_name='抗旱性')
    shbiha = models.CharField(max_length=30, blank=True, null=True, db_column='省编号', verbose_name='省编号')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    bewe = models.CharField(max_length=30, blank=True, null=True, db_column='北纬', verbose_name='北纬')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    yomise = models.CharField(max_length=30, blank=True, null=True, db_column='幼苗色', verbose_name='幼苗色')
    suzh = models.CharField(max_length=30, blank=True, null=True, db_column='穗长', verbose_name='穗长')
    yumimikaji = models.CharField(max_length=30, blank=True, null=True, db_column='玉米螟抗级', verbose_name='玉米螟抗级')
    shyurish = models.CharField(max_length=30, blank=True, null=True, db_column='生育日数', verbose_name='生育日数')
    shfe = models.CharField(max_length=30, blank=True, null=True, db_column='水份', verbose_name='水份')
    yaqise = models.CharField(max_length=30, blank=True, null=True, db_column='芽鞘色', verbose_name='芽鞘色')
    sulizh = models.CharField(max_length=30, blank=True, null=True, db_column='穗粒重', verbose_name='穗粒重')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    zhkelv = models.CharField(max_length=30, blank=True, null=True, db_column='着壳率', verbose_name='着壳率')
    jizhlv = models.CharField(max_length=30, blank=True, null=True, db_column='角质率', verbose_name='角质率')
    jicu = models.CharField(max_length=30, blank=True, null=True, db_column='茎粗', verbose_name='茎粗')
    galiyakaji = models.CharField(max_length=30, blank=True, null=True, db_column='高粱蚜抗级', verbose_name='高粱蚜抗级')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    xins = models.CharField(max_length=30, blank=True, null=True, db_column='穗型', verbose_name='穗型')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    pzname = models.CharField(max_length=50, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    sihesubilv = models.CharField(max_length=30, blank=True, null=True, db_column='丝黑穗病率', verbose_name='丝黑穗病率')
    yubiha = models.CharField(max_length=30, blank=True, null=True, db_column='原编号', verbose_name='原编号')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    gujikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='灌浆抗寒性', verbose_name='灌浆抗寒性')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    miqikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='苗期抗寒性', verbose_name='苗期抗寒性')
    zhmase = models.CharField(max_length=30, blank=True, null=True, db_column='主脉色', verbose_name='主脉色')
    fenixi = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖性', verbose_name='分蘖性')
    miqinayaxi = models.CharField(max_length=30, blank=True, null=True, db_column='苗期耐盐性', verbose_name='苗期耐盐性')
    dani = models.CharField(max_length=30, blank=True, null=True, db_column='单宁', verbose_name='单宁')
    chdu = models.CharField(max_length=30, blank=True, null=True, db_column='锤度', verbose_name='锤度')
    layudi = models.CharField(max_length=30, blank=True, null=True, db_column='来源地', verbose_name='来源地')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    yaqinayaxi = models.CharField(max_length=30, blank=True, null=True, db_column='芽期耐盐性', verbose_name='芽期耐盐性')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    najixi = models.CharField(max_length=30, blank=True, null=True, db_column='耐瘠性', verbose_name='耐瘠性')
    subizh = models.CharField(max_length=30, blank=True, null=True, db_column='穗柄长', verbose_name='穗柄长')
    doji = models.CharField(max_length=30, blank=True, null=True, db_column='东经', verbose_name='东经')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    laanzhdaba = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨占蛋白', verbose_name='赖氨占蛋白')
    kese = models.CharField(max_length=30, blank=True, null=True, db_column='壳色', verbose_name='壳色')
    dafuxi = models.CharField(max_length=30, blank=True, null=True, db_column='倒伏性', verbose_name='倒伏性')
    laanzhyapi = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨占样品', verbose_name='赖氨占样品')
    yirushji = models.CharField(max_length=30, blank=True, null=True, db_column='引入时间', verbose_name='引入时间')
    gach = models.CharField(max_length=30, blank=True, null=True, db_column='高程', verbose_name='高程')
    yikebapidu = models.CharField(max_length=30, blank=True, null=True, db_column='颖壳包皮度', verbose_name='颖壳包皮度')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    sihesukaji = models.CharField(max_length=30, blank=True, null=True, db_column='丝黑穗抗级', verbose_name='丝黑穗抗级')
    dawebiha = models.CharField(max_length=30, blank=True, null=True, db_column='单位编号', verbose_name='单位编号')
    tijidababi = models.CharField(max_length=30, blank=True, null=True, db_column='田间大斑病', verbose_name='田间大斑病')
    yexifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='叶锈反应型', verbose_name='叶锈反应型')
    tahuli = models.CharField(max_length=30, blank=True, null=True, db_column='糖化力', verbose_name='糖化力')
    mixi = models.CharField(max_length=30, blank=True, null=True, db_column='米香', verbose_name='米香')
    balilv = models.CharField(max_length=30, blank=True, null=True, db_column='爆裂率', verbose_name='爆裂率')
    nalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝性', verbose_name='耐涝性')
    sumidu = models.CharField(max_length=30, blank=True, null=True, db_column='穗密度', verbose_name='穗密度')
    babefesh = models.CharField(max_length=30, blank=True, null=True, db_column='白背飞虱', verbose_name='白背飞虱')
    shsulv = models.CharField(max_length=30, blank=True, null=True, db_column='双穗率', verbose_name='双穗率')
    chmebibisu = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病病穗', verbose_name='赤霉病病穗')
    kahajibi = models.CharField(max_length=30, blank=True, null=True, db_column='抗旱级别', verbose_name='抗旱级别')
    mise = models.CharField(max_length=30, blank=True, null=True, db_column='米色', verbose_name='米色')
    dabafayixi = models.CharField(max_length=30, blank=True, null=True, db_column='大斑反应型', verbose_name='大斑反应型')
    yexipubilv = models.CharField(max_length=30, blank=True, null=True, db_column='叶锈普遍率', verbose_name='叶锈普遍率')
    fenili = models.CharField(max_length=30, blank=True, null=True, db_column='分蘖力', verbose_name='分蘖力')
    xiji = models.CharField(max_length=30, blank=True, null=True, db_column='籼粳', verbose_name='籼粳')
    cuzodife = models.CharField(max_length=30, blank=True, null=True, db_column='粗总淀粉', verbose_name='粗总淀粉')
    tixifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='条锈反应型', verbose_name='条锈反应型')
    tiwebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='条纹病抗性', verbose_name='条纹病抗性')
    miwe = models.CharField(max_length=30, blank=True, null=True, db_column='苗瘟', verbose_name='苗瘟')
    qibelayu = models.CharField(max_length=30, blank=True, null=True, db_column='亲本来源', verbose_name='亲本来源')
    gaxiyazhdu = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈严重度', verbose_name='秆锈严重度')
    dochxi = models.CharField(max_length=30, blank=True, null=True, db_column='冬春性', verbose_name='冬春性')
    miqinaha = models.CharField(max_length=30, blank=True, null=True, db_column='苗期耐旱', verbose_name='苗期耐旱')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    ma = models.CharField(max_length=30, blank=True, null=True, db_column='芒', verbose_name='芒')
    tiwebibilv = models.CharField(max_length=30, blank=True, null=True, db_column='条纹病病率', verbose_name='条纹病病率')
    jimilv = models.CharField(max_length=30, blank=True, null=True, db_column='精米率', verbose_name='精米率')
    aihuyemibi = models.CharField(max_length=30, blank=True, null=True, db_column='矮花叶苗病', verbose_name='矮花叶苗病')
    tijikahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='田间抗寒性', verbose_name='田间抗寒性')
    maxi = models.CharField(max_length=30, blank=True, null=True, db_column='芒性', verbose_name='芒性')
    zhkubi = models.CharField(max_length=30, blank=True, null=True, db_column='长宽比', verbose_name='长宽比')
    hushxisu = models.CharField(max_length=30, blank=True, null=True, db_column='花生稀酸', verbose_name='花生稀酸')
    gaxifayixi = models.CharField(max_length=30, blank=True, null=True, db_column='秆锈反应型', verbose_name='秆锈反应型')
    shmichdu = models.CharField(max_length=30, blank=True, null=True, db_column='水敏称度', verbose_name='水敏称度')
    chsuqi = models.CharField(max_length=30, blank=True, null=True, db_column='出穗期', verbose_name='出穗期')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    sulish = models.CharField(max_length=30, blank=True, null=True, db_column='穗粒数', verbose_name='穗粒数')
    yijise = models.CharField(max_length=30, blank=True, null=True, db_column='颖尖色', verbose_name='颖尖色')
    dabapiji = models.CharField(max_length=30, blank=True, null=True, db_column='大斑评价', verbose_name='大斑评价')
    gefusubiji = models.CharField(max_length=30, blank=True, null=True, db_column='根腐穗病级', verbose_name='根腐穗病级')
    pilu = models.CharField(max_length=30, blank=True, null=True, db_column='皮裸', verbose_name='皮裸')
    zazhwa = models.CharField(max_length=30, blank=True, null=True, db_column='早中晚', verbose_name='早中晚')
    zhjiyepish = models.CharField(max_length=30, blank=True, null=True, db_column='主茎叶片数', verbose_name='主茎叶片数')
    chdizh = models.CharField(max_length=30, blank=True, null=True, db_column='沉淀值', verbose_name='沉淀值')
    nalajibi = models.CharField(max_length=30, blank=True, null=True, db_column='耐涝级别', verbose_name='耐涝级别')
    bacudawe_2 = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位_2', verbose_name='保存单位_2')
    xisufezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='雄穗分枝数', verbose_name='雄穗分枝数')
    chmebikaxi = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病抗性', verbose_name='赤霉病抗性')
    wekubi = models.CharField(max_length=30, blank=True, null=True, db_column='纹枯病', verbose_name='纹枯病')
    zolvsu = models.CharField(max_length=30, blank=True, null=True, db_column='棕榈酸', verbose_name='棕榈酸')
    bafefayixi = models.CharField(max_length=30, blank=True, null=True, db_column='白粉反应型', verbose_name='白粉反应型')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='棱型', verbose_name='棱型')
    yijiwazh = models.CharField(max_length=30, blank=True, null=True, db_column='颖尖弯直', verbose_name='颖尖弯直')
    feyush = models.CharField(max_length=30, blank=True, null=True, db_column='α生育酚', verbose_name='α生育酚')
    layugu = models.CharField(max_length=30, blank=True, null=True, db_column='来源国', verbose_name='来源国')
    huhufabilv = models.CharField(max_length=30, blank=True, null=True, db_column='黄花发病率', verbose_name='黄花发病率')
    fafajizuhe = models.CharField(max_length=30, blank=True, null=True, db_column='方法及组合', verbose_name='方法及组合')
    tijixibabi = models.CharField(max_length=30, blank=True, null=True, db_column='田间小斑病', verbose_name='田间小斑病')
    chmebibizh = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病病指', verbose_name='赤霉病病指')
    qufejichwu = models.CharField(max_length=30, blank=True, null=True, db_column='全粉浸出物', verbose_name='全粉浸出物')
    mazh = models.CharField(max_length=30, blank=True, null=True, db_column='芒长', verbose_name='芒长')
    xibapiji = models.CharField(max_length=30, blank=True, null=True, db_column='小斑评价', verbose_name='小斑评价')
    yuchnixi = models.CharField(max_length=30, blank=True, null=True, db_column='育成年限', verbose_name='育成年限')
    hhhhd = models.CharField(max_length=30, blank=True, null=True, db_column='黄花黄化度', verbose_name='黄花黄化度')
    camilv = models.CharField(max_length=30, blank=True, null=True, db_column='糙米率', verbose_name='糙米率')
    aihuyepiji = models.CharField(max_length=30, blank=True, null=True, db_column='矮花叶评价', verbose_name='矮花叶评价')
    qita = models.CharField(max_length=30, blank=True, null=True, db_column='其它', verbose_name='其它')
    chmebisulv = models.CharField(max_length=30, blank=True, null=True, db_column='赤霉病穗率', verbose_name='赤霉病穗率')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_高粱'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class yingzuidou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    daansu = models.CharField(max_length=30, blank=True, null=True, db_column='蛋氨酸', verbose_name='蛋氨酸')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    sang = models.CharField(max_length=30, blank=True, null=True, db_column='谷氨酸', verbose_name='谷氨酸')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')
    jiansu = models.CharField(max_length=30, blank=True, null=True, db_column='精氨酸', verbose_name='精氨酸')
    biansu = models.CharField(max_length=30, blank=True, null=True, db_column='丙氨酸', verbose_name='丙氨酸')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    zohe = models.CharField(max_length=30, blank=True, null=True, db_column='总和', verbose_name='总和')
    las = models.CharField(max_length=30, blank=True, null=True, db_column='酪氨酸', verbose_name='酪氨酸')
    tidoansu = models.CharField(max_length=30, blank=True, null=True, db_column='天冬氨酸', verbose_name='天冬氨酸')
    yiliansu = models.CharField(max_length=30, blank=True, null=True, db_column='异亮氨酸', verbose_name='异亮氨酸')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    seansu = models.CharField(max_length=30, blank=True, null=True, db_column='色氨酸', verbose_name='色氨酸')
    zhfa = models.CharField(max_length=30, blank=True, null=True, db_column='脂肪', verbose_name='脂肪')
    zuansu = models.CharField(max_length=30, blank=True, null=True, db_column='组氨酸', verbose_name='组氨酸')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    zodife = models.CharField(max_length=30, blank=True, null=True, db_column='总淀粉', verbose_name='总淀粉')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    suansu = models.CharField(max_length=30, blank=True, null=True, db_column='苏氨酸', verbose_name='苏氨酸')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bebiansu = models.CharField(max_length=30, blank=True, null=True, db_column='苯丙氨酸', verbose_name='苯丙氨酸')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    yueguang = models.CharField(max_length=30, blank=True, null=True, db_column='胱氨酸', verbose_name='胱氨酸')
    cilidife = models.CharField(max_length=30, blank=True, null=True, db_column='支链淀粉', verbose_name='支链淀粉')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    dabazh = models.CharField(max_length=30, blank=True, null=True, db_column='蛋白质', verbose_name='蛋白质')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    liansu = models.CharField(max_length=30, blank=True, null=True, db_column='亮氨酸', verbose_name='亮氨酸')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    gaansu = models.CharField(max_length=30, blank=True, null=True, db_column='甘氨酸', verbose_name='甘氨酸')
    dajilish = models.CharField(max_length=30, blank=True, null=True, db_column='单荚粒数', verbose_name='单荚粒数')
    xiansu = models.CharField(max_length=30, blank=True, null=True, db_column='缬氨酸', verbose_name='缬氨酸')
    zhlidife = models.CharField(max_length=30, blank=True, null=True, db_column='直链淀粉', verbose_name='直链淀粉')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    fuansu = models.CharField(max_length=30, blank=True, null=True, db_column='脯氨酸', verbose_name='脯氨酸')
    naias = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    siansu = models.CharField(max_length=30, blank=True, null=True, db_column='丝氨酸', verbose_name='丝氨酸')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    jicudaxi = models.CharField(max_length=30, blank=True, null=True, db_column='茎粗大小', verbose_name='茎粗大小')
    yahabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病评价', verbose_name='蚜害病评价')
    jixi = models.CharField(max_length=30, blank=True, null=True, db_column='荚型', verbose_name='荚型')
    zhxi = models.CharField(max_length=30, blank=True, null=True, db_column='株型', verbose_name='株型')
    hebabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='褐斑病指数', verbose_name='褐斑病指数')
    miqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='苗期耐盐', verbose_name='苗期耐盐')
    layu = models.CharField(max_length=30, blank=True, null=True, db_column='来源', verbose_name='来源')
    xibipiji = models.CharField(max_length=30, blank=True, null=True, db_column='锈病评价', verbose_name='锈病评价')
    jicu = models.CharField(max_length=30, blank=True, null=True, db_column='茎粗', verbose_name='茎粗')
    hebabiji = models.CharField(max_length=30, blank=True, null=True, db_column='褐斑病级', verbose_name='褐斑病级')
    xibibiji = models.CharField(max_length=30, blank=True, null=True, db_column='锈病病级', verbose_name='锈病病级')
    nahaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐旱性', verbose_name='耐旱性')
    yahabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病指数', verbose_name='蚜害病指数')
    bafebipiji = models.CharField(max_length=30, blank=True, null=True, db_column='白粉病评价', verbose_name='白粉病评价')
    shrose = models.CharField(max_length=30, blank=True, null=True, db_column='薯肉色', verbose_name='薯肉色')
    juyudu = models.CharField(max_length=30, blank=True, null=True, db_column='均匀度', verbose_name='均匀度')
    bafebiji = models.CharField(max_length=30, blank=True, null=True, db_column='白粉病级', verbose_name='白粉病级')
    diyese = models.CharField(max_length=30, blank=True, null=True, db_column='顶叶色', verbose_name='顶叶色')
    chbabizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='赤斑病指数', verbose_name='赤斑病指数')
    yaqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='芽期抗旱', verbose_name='芽期抗旱')
    majise = models.CharField(max_length=30, blank=True, null=True, db_column='脉基色', verbose_name='脉基色')
    yahabiji = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病级', verbose_name='蚜害病级')
    zuzhmazh = models.CharField(max_length=30, blank=True, null=True, db_column='最长蔓长', verbose_name='最长蔓长')
    kalaxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗涝性', verbose_name='抗涝性')
    bafebizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='白粉病指数', verbose_name='白粉病指数')
    bijise = models.CharField(max_length=30, blank=True, null=True, db_column='柄基色', verbose_name='柄基色')
    chbabiji = models.CharField(max_length=30, blank=True, null=True, db_column='赤斑病级', verbose_name='赤斑病级')
    nayaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐盐性', verbose_name='耐盐性')
    yuchnife = models.CharField(max_length=20, blank=True, null=True, db_column='育成年份', verbose_name='育成年份')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')
    yahabizh = models.CharField(max_length=30, blank=True, null=True, db_column='蚜害病指', verbose_name='蚜害病指')
    shwekaxi1 = models.CharField(max_length=30, blank=True, null=True, db_column='薯瘟抗性1', verbose_name='薯瘟抗性1')
    yoxizh = models.CharField(max_length=30, blank=True, null=True, db_column='有效枝', verbose_name='有效枝')
    nazhxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐贮性', verbose_name='耐贮性')
    shqikaha = models.CharField(max_length=30, blank=True, null=True, db_column='熟期抗旱', verbose_name='熟期抗旱')
    hogalv = models.CharField(max_length=30, blank=True, null=True, db_column='烘干率', verbose_name='烘干率')
    xibizhsh = models.CharField(max_length=30, blank=True, null=True, db_column='锈病指数', verbose_name='锈病指数')
    xuyudawe = models.CharField(max_length=30, blank=True, null=True, db_column='选育单位', verbose_name='选育单位')
    chli = models.CharField(max_length=30, blank=True, null=True, db_column='产量', verbose_name='产量')
    guan = models.CharField(max_length=30, blank=True, null=True, db_column='谷氨', verbose_name='谷氨')
    gu = models.CharField(max_length=30, blank=True, null=True, db_column='谷', verbose_name='谷')
    yaqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='芽期耐盐', verbose_name='芽期耐盐')
    jiduroma = models.CharField(max_length=30, blank=True, null=True, db_column='茎端茸毛', verbose_name='茎端茸毛')
    lx = models.CharField(max_length=30, blank=True, null=True, db_column='粒型', verbose_name='粒型')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    yepiku = models.CharField(max_length=30, blank=True, null=True, db_column='叶片宽', verbose_name='叶片宽')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    jibufezh = models.CharField(max_length=30, blank=True, null=True, db_column='基部分枝', verbose_name='基部分枝')
    chbabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='赤斑病评价', verbose_name='赤斑病评价')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    hebabipiji = models.CharField(max_length=30, blank=True, null=True, db_column='褐斑病评价', verbose_name='褐斑病评价')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_鹰嘴豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class huanggua(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单瓜重', verbose_name='单瓜重')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    shmefabilv = models.CharField(max_length=30, blank=True, null=True, db_column='霜霉发病率', verbose_name='霜霉发病率')
    gumilafe = models.CharField(max_length=30, blank=True, null=True, db_column='瓜面腊粉', verbose_name='瓜面腊粉')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜皮色', verbose_name='商瓜皮色')
    lagucise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜次色', verbose_name='老瓜次色')
    yibikazh = models.CharField(max_length=30, blank=True, null=True, db_column='疫病抗指', verbose_name='疫病抗指')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    lagubawe = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜斑纹', verbose_name='老瓜斑纹')
    yibifabilv = models.CharField(max_length=30, blank=True, null=True, db_column='疫病发病率', verbose_name='疫病发病率')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    gucise = models.CharField(max_length=30, blank=True, null=True, db_column='瓜刺色', verbose_name='瓜刺色')
    lagupise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜皮色', verbose_name='老瓜皮色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='瓜形', verbose_name='瓜形')
    gucidush = models.CharField(max_length=30, blank=True, null=True, db_column='瓜刺多少', verbose_name='瓜刺多少')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    cishhujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='雌首花节位', verbose_name='雌首花节位')
    shmebikazh = models.CharField(max_length=30, blank=True, null=True, db_column='霜霉病抗指', verbose_name='霜霉病抗指')
    kuwefabilv = models.CharField(max_length=30, blank=True, null=True, db_column='枯萎发病率', verbose_name='枯萎发病率')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    bafefabilv = models.CharField(max_length=30, blank=True, null=True, db_column='白粉发病率', verbose_name='白粉发病率')
    kuwebikazh = models.CharField(max_length=30, blank=True, null=True, db_column='枯萎病抗指', verbose_name='枯萎病抗指')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    shgucise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜次色', verbose_name='商瓜次色')
    bafebikazh = models.CharField(max_length=30, blank=True, null=True, db_column='白粉病抗指', verbose_name='白粉病抗指')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shgubawe = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜斑纹', verbose_name='商瓜斑纹')
    gulexizh = models.CharField(max_length=30, blank=True, null=True, db_column='瓜棱形状', verbose_name='瓜棱形状')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_黄瓜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class huanghuacai(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    pizh = models.CharField(max_length=30, blank=True, null=True, db_column='品质', verbose_name='品质')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    yotu = models.CharField(max_length=30, blank=True, null=True, db_column='用途', verbose_name='用途')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_黄花菜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class huangma(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    lali = models.CharField(max_length=30, blank=True, null=True, db_column='拉力', verbose_name='拉力')
    zhjise = models.CharField(max_length=30, blank=True, null=True, db_column='中茎色', verbose_name='中茎色')
    heditajubi = models.CharField(max_length=30, blank=True, null=True, db_column='黑点炭疽病', verbose_name='黑点炭疽病')
    zhzichshqi = models.CharField(max_length=30, blank=True, null=True, db_column='种子成熟期', verbose_name='种子成熟期')
    zhsh = models.CharField(max_length=30, blank=True, null=True, db_column='支数', verbose_name='支数')
    xiwemuch = models.CharField(max_length=30, blank=True, null=True, db_column='纤维亩产', verbose_name='纤维亩产')
    hojise = models.CharField(max_length=30, blank=True, null=True, db_column='后茎色', verbose_name='后茎色')
    yeya = models.CharField(max_length=30, blank=True, null=True, db_column='腋芽', verbose_name='腋芽')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    tuyese = models.CharField(max_length=30, blank=True, null=True, db_column='托叶色', verbose_name='托叶色')
    zhgapizh = models.CharField(max_length=30, blank=True, null=True, db_column='株干皮重', verbose_name='株干皮重')
    mijise = models.CharField(max_length=30, blank=True, null=True, db_column='苗茎色', verbose_name='苗茎色')
    zhjimazh = models.CharField(max_length=30, blank=True, null=True, db_column='株精麻重', verbose_name='株精麻重')
    zhqilizh = models.CharField(max_length=30, blank=True, null=True, db_column='种千粒重', verbose_name='种千粒重')
    tajubi = models.CharField(max_length=30, blank=True, null=True, db_column='炭疽病', verbose_name='炭疽病')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    jicu = models.CharField(max_length=30, blank=True, null=True, db_column='茎粗', verbose_name='茎粗')
    lexi = models.CharField(max_length=30, blank=True, null=True, db_column='类型', verbose_name='类型')
    huese = models.CharField(max_length=30, blank=True, null=True, db_column='花萼色', verbose_name='花萼色')
    xipiho = models.CharField(max_length=30, blank=True, null=True, db_column='鲜皮厚', verbose_name='鲜皮厚')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    zhxipizh = models.CharField(max_length=30, blank=True, null=True, db_column='株鲜皮重', verbose_name='株鲜皮重')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    chmiqi = models.CharField(max_length=30, blank=True, null=True, db_column='出苗期', verbose_name='出苗期')
    yese = models.CharField(max_length=30, blank=True, null=True, db_column='叶色', verbose_name='叶色')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    jixi = models.CharField(max_length=30, blank=True, null=True, db_column='茎形', verbose_name='茎形')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    jiguqi = models.CharField(max_length=30, blank=True, null=True, db_column='结果期', verbose_name='结果期')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    gushse = models.CharField(max_length=30, blank=True, null=True, db_column='果实色', verbose_name='果实色')
    yebise = models.CharField(max_length=30, blank=True, null=True, db_column='叶柄色', verbose_name='叶柄色')
    goyichshqi = models.CharField(max_length=30, blank=True, null=True, db_column='工艺成熟期', verbose_name='工艺成熟期')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    kahuqi = models.CharField(max_length=30, blank=True, null=True, db_column='开花期', verbose_name='开花期')
    xileqi = models.CharField(max_length=30, blank=True, null=True, db_column='现蕾期', verbose_name='现蕾期')
    fezhga = models.CharField(max_length=30, blank=True, null=True, db_column='分枝高', verbose_name='分枝高')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_黄麻'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class shuji(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    sx = models.CharField(max_length=30, blank=True, null=True, db_column='穗型', verbose_name='穗型')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    shyurish = models.CharField(max_length=30, blank=True, null=True, db_column='生育日数', verbose_name='生育日数')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    chmiqi = models.CharField(max_length=30, blank=True, null=True, db_column='出苗期', verbose_name='出苗期')
    cuzhfa = models.CharField(max_length=30, blank=True, null=True, db_column='粗脂肪', verbose_name='粗脂肪')
    zhsuzh = models.CharField(max_length=30, blank=True, null=True, db_column='主穗长', verbose_name='主穗长')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    lulixi = models.CharField(max_length=30, blank=True, null=True, db_column='落粒性', verbose_name='落粒性')
    nayaxi = models.CharField(max_length=30, blank=True, null=True, db_column='耐盐性', verbose_name='耐盐性')
    chsuqi = models.CharField(max_length=30, blank=True, null=True, db_column='抽穗期', verbose_name='抽穗期')
    zhjijish = models.CharField(max_length=30, blank=True, null=True, db_column='主茎节数', verbose_name='主茎节数')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    qilizh = models.CharField(max_length=30, blank=True, null=True, db_column='千粒重', verbose_name='千粒重')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    naias = models.CharField(max_length=30, blank=True, null=True, db_column='赖氨酸', verbose_name='赖氨酸')
    yaqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='芽期耐盐', verbose_name='芽期耐盐')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=50, blank=True, null=True, db_column='译名', verbose_name='译名')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    hesubi = models.CharField(max_length=30, blank=True, null=True, db_column='黑穗病', verbose_name='黑穗病')
    dafuxi = models.CharField(max_length=30, blank=True, null=True, db_column='倒伏性', verbose_name='倒伏性')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    mise = models.CharField(max_length=30, blank=True, null=True, db_column='米色', verbose_name='米色')
    dazhlizh = models.CharField(max_length=30, blank=True, null=True, db_column='单株粒重', verbose_name='单株粒重')
    huxuse = models.CharField(max_length=30, blank=True, null=True, db_column='花序色', verbose_name='花序色')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    miqinaya = models.CharField(max_length=30, blank=True, null=True, db_column='苗期耐盐', verbose_name='苗期耐盐')
    cudaba = models.CharField(max_length=30, blank=True, null=True, db_column='粗蛋白', verbose_name='粗蛋白')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_黍稷'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class lidou(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    dajilish = models.CharField(max_length=30, blank=True, null=True, db_column='单荚粒数', verbose_name='单荚粒数')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    xumi = models.CharField(max_length=60, blank=True, null=True, db_column='学名', verbose_name='学名')
    yapilexi = models.CharField(max_length=30, blank=True, null=True, db_column='样品类型', verbose_name='样品类型')
    huse = models.CharField(max_length=30, blank=True, null=True, db_column='花色', verbose_name='花色')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    kubiha = models.CharField(max_length=30, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    qushyurish = models.CharField(max_length=30, blank=True, null=True, db_column='全生育日数', verbose_name='全生育日数')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    bozhqi = models.CharField(max_length=30, blank=True, null=True, db_column='播种期', verbose_name='播种期')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    jise = models.CharField(max_length=30, blank=True, null=True, db_column='荚色', verbose_name='荚色')
    lise = models.CharField(max_length=30, blank=True, null=True, db_column='粒色', verbose_name='粒色')
    zhga = models.CharField(max_length=30, blank=True, null=True, db_column='株高', verbose_name='株高')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    dazhjish = models.CharField(max_length=30, blank=True, null=True, db_column='单株荚数', verbose_name='单株荚数')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    balizh = models.CharField(max_length=30, blank=True, null=True, db_column='百粒重', verbose_name='百粒重')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    dazhchli = models.CharField(max_length=30, blank=True, null=True, db_column='单株产量', verbose_name='单株产量')
    fezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='分枝数', verbose_name='分枝数')
    jizh = models.CharField(max_length=30, blank=True, null=True, db_column='荚长', verbose_name='荚长')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    lixi = models.CharField(max_length=30, blank=True, null=True, db_column='粒形', verbose_name='粒形')
    chshqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期', verbose_name='成熟期')
    jijixixi = models.CharField(max_length=30, blank=True, null=True, db_column='结荚习性', verbose_name='结荚习性')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_黎豆'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class heizinangua(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    kanixi = models.CharField(max_length=30, blank=True, null=True, db_column='抗逆性', verbose_name='抗逆性')
    lagubawe = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜斑纹', verbose_name='老瓜斑纹')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    kabichxi = models.CharField(max_length=30, blank=True, null=True, db_column='抗病虫性', verbose_name='抗病虫性')
    bacubiha = models.CharField(max_length=30, blank=True, null=True, db_column='保存编号', verbose_name='保存编号')
    bezh = models.CharField(max_length=30, blank=True, null=True, db_column='备注', verbose_name='备注')
    shgucise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜次色', verbose_name='商瓜次色')
    zhzilayu = models.CharField(max_length=30, blank=True, null=True, db_column='种子来源', verbose_name='种子来源')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='瓜形', verbose_name='瓜形')
    gulexizh = models.CharField(max_length=30, blank=True, null=True, db_column='瓜棱形状', verbose_name='瓜棱形状')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    shgupise = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜皮色', verbose_name='商瓜皮色')
    daguzh = models.CharField(max_length=30, blank=True, null=True, db_column='单瓜重', verbose_name='单瓜重')
    yexi = models.CharField(max_length=30, blank=True, null=True, db_column='叶形', verbose_name='叶形')
    shyuqi = models.CharField(max_length=30, blank=True, null=True, db_column='生育期', verbose_name='生育期')
    lagupise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜皮色', verbose_name='老瓜皮色')
    much = models.CharField(max_length=30, blank=True, null=True, db_column='亩产', verbose_name='亩产')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    lagucise = models.CharField(max_length=30, blank=True, null=True, db_column='老瓜次色', verbose_name='老瓜次色')
    zhzhkubiha = models.CharField(max_length=30, blank=True, null=True, db_column='种质库编号', verbose_name='种质库编号')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    zapejiji = models.CharField(max_length=30, blank=True, null=True, db_column='栽培季节', verbose_name='栽培季节')
    shxi = models.CharField(max_length=30, blank=True, null=True, db_column='熟性', verbose_name='熟性')
    fezhxi = models.CharField(max_length=30, blank=True, null=True, db_column='分枝性', verbose_name='分枝性')
    gumilafe = models.CharField(max_length=30, blank=True, null=True, db_column='瓜面腊粉', verbose_name='瓜面腊粉')
    shgubawe = models.CharField(max_length=30, blank=True, null=True, db_column='商瓜斑纹', verbose_name='商瓜斑纹')
    shzhxixi = models.CharField(max_length=30, blank=True, null=True, db_column='生长习性', verbose_name='生长习性')
    cishhujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='雌首花节位', verbose_name='雌首花节位')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_黑子南瓜'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class longyan(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    zhhuta = models.CharField(max_length=30, blank=True, null=True, db_column='转化糖', verbose_name='转化糖')
    chshriqi = models.CharField(max_length=30, blank=True, null=True, db_column='成熟日期', verbose_name='成熟日期')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    keroguxiwu = models.CharField(max_length=30, blank=True, null=True, db_column='可溶固形物', verbose_name='可溶固形物')
    pzname = models.CharField(max_length=30, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    hasuli = models.CharField(max_length=30, blank=True, null=True, db_column='含酸量', verbose_name='含酸量')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    wagupiji = models.CharField(max_length=30, blank=True, null=True, db_column='外观评价', verbose_name='外观评价')
    zhye = models.CharField(max_length=30, blank=True, null=True, db_column='汁液', verbose_name='汁液')
    nezhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='内质评价', verbose_name='内质评价')
    weshsuc = models.CharField(db_column='维生素C', max_length=30, blank=True, null=True, verbose_name='维生素C')
    fewe = models.CharField(max_length=30, blank=True, null=True, db_column='风味', verbose_name='风味')
    teyijiyotu = models.CharField(max_length=30, blank=True, null=True, db_column='特异及用途', verbose_name='特异及用途')
    daguzhpiji = models.CharField(max_length=30, blank=True, null=True, db_column='单果重评价', verbose_name='单果重评价')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    rozh = models.CharField(max_length=30, blank=True, null=True, db_column='肉质', verbose_name='肉质')
    guxi = models.CharField(max_length=30, blank=True, null=True, db_column='果形', verbose_name='果形')
    chshqipiji = models.CharField(max_length=30, blank=True, null=True, db_column='成熟期评价', verbose_name='成熟期评价')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    yimi = models.CharField(max_length=30, blank=True, null=True, db_column='译名', verbose_name='译名')
    daguzhg = models.CharField(db_column='单果重G', max_length=30, blank=True, null=True, verbose_name='单果重G')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    seze = models.CharField(max_length=30, blank=True, null=True, db_column='色泽', verbose_name='色泽')
    zhqidu = models.CharField(max_length=30, blank=True, null=True, db_column='整齐度', verbose_name='整齐度')
    keshlv = models.CharField(db_column='可食率％', max_length=30, blank=True, null=True, verbose_name='可食率％')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_龙眼'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class longshelanma(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    zhmigadu = models.CharField(max_length=30, blank=True, null=True, db_column='种苗高度', verbose_name='种苗高度')
    kemi = models.CharField(max_length=30, blank=True, null=True, db_column='科名', verbose_name='科名')
    nijuwe = models.CharField(max_length=30, blank=True, null=True, db_column='年均温', verbose_name='年均温')
    shyifeli = models.CharField(max_length=30, blank=True, null=True, db_column='适应肥力', verbose_name='适应肥力')
    xiwechdu = models.CharField(max_length=30, blank=True, null=True, db_column='纤维长度', verbose_name='纤维长度')
    nizezhyepi = models.CharField(max_length=30, blank=True, null=True, db_column='年增长叶片', verbose_name='年增长叶片')
    yizhdawe = models.CharField(max_length=30, blank=True, null=True, db_column='引种单位', verbose_name='引种单位')
    bacujuwedu = models.CharField(max_length=30, blank=True, null=True, db_column='保存均温度', verbose_name='保存均温度')
    kahali = models.CharField(max_length=30, blank=True, null=True, db_column='抗寒力', verbose_name='抗寒力')
    tujiyogumo = models.CharField(max_length=30, blank=True, null=True, db_column='推荐用规莫', verbose_name='推荐用规莫')
    bacujiwe = models.CharField(max_length=30, blank=True, null=True, db_column='保存经纬', verbose_name='保存经纬')
    dizh = models.CharField(max_length=30, blank=True, null=True, db_column='定植', verbose_name='定植')
    sh = models.CharField(max_length=30, blank=True, null=True, db_column='省', verbose_name='省')
    nipijuyuli = models.CharField(max_length=30, blank=True, null=True, db_column='年平均雨量', verbose_name='年平均雨量')
    nichgaxiwe = models.CharField(max_length=30, blank=True, null=True, db_column='年产干纤维', verbose_name='年产干纤维')
    pijidawe = models.CharField(max_length=30, blank=True, null=True, db_column='评价单位', verbose_name='评价单位')
    xiwenayali = models.CharField(max_length=30, blank=True, null=True, db_column='纤维耐盐力', verbose_name='纤维耐盐力')
    riwechshyi = models.CharField(max_length=30, blank=True, null=True, db_column='日温差适应', verbose_name='日温差适应')
    haxiwelv = models.CharField(max_length=30, blank=True, null=True, db_column='含纤维率', verbose_name='含纤维率')
    xiwetali = models.CharField(max_length=30, blank=True, null=True, db_column='纤维弹力', verbose_name='纤维弹力')
    zhqizezhye = models.CharField(max_length=30, blank=True, null=True, db_column='周期增长叶', verbose_name='周期增长叶')
    zhqigaxiwe = models.CharField(max_length=30, blank=True, null=True, db_column='周期干纤维', verbose_name='周期干纤维')
    shmi = models.CharField(max_length=30, blank=True, null=True, db_column='属名', verbose_name='属名')
    toyibiha = models.CharField(max_length=10, db_column='统一编号', verbose_name='统一编号')
    xumi = models.CharField(max_length=40, blank=True, null=True, db_column='学名', verbose_name='学名')
    yepishhalv = models.CharField(max_length=30, blank=True, null=True, db_column='叶片受害率', verbose_name='叶片受害率')
    yepiyase = models.CharField(max_length=30, blank=True, null=True, db_column='叶片颜色', verbose_name='叶片颜色')
    yowujigu = models.CharField(max_length=30, blank=True, null=True, db_column='有无结果', verbose_name='有无结果')
    zhzhpumiji = models.CharField(max_length=30, blank=True, null=True, db_column='种质圃面积', verbose_name='种质圃面积')
    lixiweshyi = models.CharField(max_length=30, blank=True, null=True, db_column='零下温适应', verbose_name='零下温适应')
    kafeneli = models.CharField(max_length=30, blank=True, null=True, db_column='抗风能力', verbose_name='抗风能力')
    yirushji = models.CharField(max_length=30, blank=True, null=True, db_column='引入时间', verbose_name='引入时间')
    shzhzhqi = models.CharField(max_length=30, blank=True, null=True, db_column='生长周期', verbose_name='生长周期')
    zhzhrupuli = models.CharField(max_length=30, blank=True, null=True, db_column='种质入圃量', verbose_name='种质入圃量')
    yuchdi = models.CharField(max_length=30, blank=True, null=True, db_column='原产地', verbose_name='原产地')
    haba = models.CharField(max_length=30, blank=True, null=True, db_column='海拔', verbose_name='海拔')
    shzhmidu = models.CharField(max_length=30, blank=True, null=True, db_column='始植密度', verbose_name='始植密度')
    zhhaju = models.CharField(max_length=30, blank=True, null=True, db_column='株行距', verbose_name='株行距')
    xiya = models.CharField(max_length=30, blank=True, null=True, db_column='吸芽', verbose_name='吸芽')
    bamagabilv = models.CharField(max_length=30, blank=True, null=True, db_column='斑马感病率', verbose_name='斑马感病率')
    bacuhaba = models.CharField(max_length=30, blank=True, null=True, db_column='保存海拔', verbose_name='保存海拔')
    yeyujuci = models.CharField(max_length=30, blank=True, null=True, db_column='叶缘锯刺', verbose_name='叶缘锯刺')
    bibazezhsh = models.CharField(max_length=30, blank=True, null=True, db_column='病斑增长数', verbose_name='病斑增长数')
    yezh = models.CharField(max_length=30, blank=True, null=True, db_column='叶长', verbose_name='叶长')
    yirucali = models.CharField(max_length=30, blank=True, null=True, db_column='引入材料', verbose_name='引入材料')
    kafubineli = models.CharField(max_length=30, blank=True, null=True, db_column='抗腐病能力', verbose_name='抗腐病能力')
    juduzudiwe = models.CharField(max_length=30, blank=True, null=True, db_column='绝对最低温', verbose_name='绝对最低温')
    zhyashli = models.CharField(max_length=30, blank=True, null=True, db_column='珠芽数量', verbose_name='珠芽数量')
    yeku = models.CharField(max_length=30, blank=True, null=True, db_column='叶宽', verbose_name='叶宽')
    bacudawe = models.CharField(max_length=30, blank=True, null=True, db_column='保存单位', verbose_name='保存单位')
    jiwedu = models.CharField(max_length=30, blank=True, null=True, db_column='经纬度', verbose_name='经纬度')
    xiwelali = models.CharField(max_length=30, blank=True, null=True, db_column='纤维拉力', verbose_name='纤维拉力')
    chbazish = models.CharField(max_length=30, blank=True, null=True, db_column='产孢子数', verbose_name='产孢子数')
    nefochjusi = models.CharField(max_length=30, blank=True, null=True, db_column='能否产菌丝', verbose_name='能否产菌丝')
    yepilafe = models.CharField(max_length=30, blank=True, null=True, db_column='叶片腊粉', verbose_name='叶片腊粉')
    niyuli = models.CharField(max_length=30, blank=True, null=True, db_column='年雨量', verbose_name='年雨量')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库_龙舌兰麻'
        unique_together = (('id', 'toyibiha'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name


class ZwyczytxpjjdDbList(models.Model):

    title = models.CharField(max_length=20, blank=False, null=False, db_column='标题', verbose_name='标题')
    table = models.CharField(max_length=60, blank=False, null=False, db_column='表名', verbose_name='表名')
    model = models.CharField(max_length=60, blank=False, null=False, db_column='模型', verbose_name='模型')

    class Meta:
        db_table = '作物遗传资源特性评价鉴定数据库列表'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class ZwkjwxDb(models.Model):
    """
    中文农业科技文摘数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    title = models.CharField(max_length=256, db_column='题名', verbose_name='题名')
    author = models.CharField(max_length=512, db_column='作者', verbose_name='作者')
    unit = models.CharField(max_length=512, db_column='作者单位', verbose_name='作者单位')
    qkname = models.CharField(max_length=128, db_column='期刊名称', verbose_name='期刊名称')
    year = models.CharField(max_length=16, db_column='年份', verbose_name='年份')
    juan = models.CharField(max_length=16, db_column='卷', verbose_name='卷')
    qi = models.CharField(max_length=16, db_column='期', verbose_name='期')
    page = models.CharField(max_length=16, db_column='页码', verbose_name='页码')
    num = models.CharField(max_length=16, db_column='页数', verbose_name='页数')
    keywords = models.CharField(max_length=512, db_column='关键词', verbose_name='关键词')
    gntykh = models.CharField(max_length=32, db_column='国内统一刊号', verbose_name='国内统一刊号')
    issn = models.CharField(max_length=32, db_column='ISSN', verbose_name='ISSN')
    zwflh = models.CharField(max_length=32, db_column='中图分类号', verbose_name='中图分类号')
    abstract = models.TextField(db_column='摘要', verbose_name='摘要')
    ywname = models.CharField(max_length=512, db_column='英文题名', verbose_name='英文题名')
    ywauthor = models.CharField(max_length=1024, db_column='英文作者', verbose_name='英文作者')
    ywgjc = models.CharField(max_length=1024, db_column='英文关键词', verbose_name='英文关键词')
    ywzy = models.TextField(db_column='英文摘要', verbose_name='英文摘要')
    qkywname = models.CharField(max_length=512, db_column='期刊英文名称', verbose_name='期刊英文名称')
    xmjjname = models.CharField(max_length=512, db_column='项目基金名称', verbose_name='项目基金名称')

    class Meta:
        db_table = '中文农业科技文摘数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class NygjDb(models.Model):
    """
    农业古籍数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    reportid = models.CharField(max_length=64, db_column='记录号', verbose_name='记录号')
    category = models.CharField(max_length=64, db_column='分类', verbose_name='分类')
    title = models.CharField(max_length=128, db_column='标题书名', verbose_name='标题书名')
    author = models.CharField(max_length=64, db_column='作者', verbose_name='作者')
    infotype = models.CharField(max_length=64, db_column='信息类型', verbose_name='信息类型')
    resource = models.CharField(max_length=64, db_column='信息来源', verbose_name='信息来源')
    pubtime = models.CharField(max_length=32, db_column='出版日期', verbose_name='出版日期')
    publish = models.CharField(max_length=128, db_column='出版者', verbose_name='出版者')
    cbd = models.CharField(max_length=64, db_column='出版地', verbose_name='出版地')
    ztxt = models.CharField(max_length=64, db_column='载体形态', verbose_name='载体形态')
    dlh = models.CharField(max_length=64, db_column='登录号', verbose_name='登录号')
    keywords = models.CharField(max_length=128, db_column='关键词', verbose_name='关键词')
    content = models.TextField(db_column='正文文摘', verbose_name='正文文摘')
    fujian = models.CharField(max_length=256, db_column='附件', verbose_name='附件')

    class Meta:
        db_table = '农业古籍数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class NygjtpDb(models.Model):
    """
    农业古籍图片数据库
    """
    reportid = models.ForeignKey(NygjDb, db_column='记录号', verbose_name='记录号', null=True, blank=True)
    page = models.IntegerField(verbose_name="页码", db_column="页码", null=True, blank=True)
    image = models.ImageField(upload_to='agridata/images', db_column='链接', verbose_name="链接", null=True, blank=True)

    class Meta:
        db_table = '农业古籍图片数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class GjnykyhzxmDb(models.Model):
    """
    国际农业科研项目数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    title = models.CharField(max_length=256, blank=False, null=False, db_column='项目名称', verbose_name='项目名称')
    desc = models.TextField(db_column='项目简介', verbose_name='项目简介')
    unit = models.CharField(max_length=256, blank=False, null=False, db_column='承担机构', verbose_name='承担机构')
    keywords = models.CharField(max_length=128, db_column='关键词', verbose_name='关键词')
    advance = models.TextField(db_column='研究进展', verbose_name='研究进展')
    resource = models.CharField(max_length=64, db_column='项目来源', verbose_name='项目来源')
    organization = models.CharField(max_length=	128, db_column='资助机构', verbose_name='资助机构')
    member = models.TextField(db_column='项目成员', verbose_name='项目成员')
    period = models.CharField(max_length=32, db_column='起止时间', verbose_name='起止时间')
    category = models.CharField(max_length=256, db_column='专业分类', verbose_name='专业分类')

    class Meta:
        db_table = '国际农业科研项目数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class GnnykyhzxmDb(models.Model):
    """
    国内农业科研项目数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    title = models.CharField(max_length=256, blank=False, null=False, db_column='项目名称', verbose_name='项目名称')
    desc = models.TextField(db_column='项目简介', verbose_name='项目简介')
    unit = models.CharField(max_length=256, blank=False, null=False, db_column='承担单位', verbose_name='承担单位')
    member = models.CharField(max_length=64, db_column='研究人员', verbose_name='研究人员')
    resource = models.CharField(max_length=128, db_column='项目来源', verbose_name='项目来源')
    category = models.CharField(max_length=64, db_column='项目类型', verbose_name='项目类型')
    fund = models.CharField(max_length=32, db_column='项目经费', verbose_name='项目经费')
    start = models.CharField(max_length=10, db_column='开始时间', verbose_name='开始时间')
    end = models.CharField(max_length=10, db_column='结束时间', verbose_name='结束时间')

    class Meta:
        db_table = '国内农业科研项目数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class NyhjkjcgDb(models.Model):
    """
    农业获奖科技成果数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    title = models.CharField(max_length=256, blank=False, null=False, db_column='成果名称', verbose_name='成果名称')
    realizer = models.TextField(db_column='完成人', verbose_name='完成人')
    unit = models.TextField(db_column='完成单位', verbose_name='完成单位')
    keywords = models.CharField(max_length=128, db_column='关键词', verbose_name='关键词')
    desc = models.TextField(db_column='简要技术说明', verbose_name='简要技术说明')
    category = models.CharField(max_length=32, db_column='成果类别', verbose_name='成果类别')
    reference = models.TextField(db_column='推荐单位', verbose_name='推荐单位')
    location = models.CharField(max_length=32, db_column='奖励地区', verbose_name='奖励地区')
    year = models.CharField(max_length=16, db_column='奖励年度', verbose_name='奖励年度')
    name = models.CharField(max_length=32, db_column='奖励名称', verbose_name='奖励名称')
    grade = models.CharField(max_length=32, db_column='奖励等级', verbose_name='奖励等级')
    register = models.CharField(max_length=32, db_column='成果登记时间', verbose_name='成果登记时间')
    setime = models.CharField(max_length=32, db_column='研究起止时间', verbose_name='研究起止时间')
    cgtxxs = models.CharField(max_length=16, db_column='成果体现形式', verbose_name='成果体现形式')
    cgscjd = models.CharField(max_length=16, db_column='成果所处阶段', verbose_name='成果所处阶段')
    cgsx = models.CharField(max_length=16, db_column='成果属性', verbose_name='成果属性')
    cgsp = models.CharField(max_length=16, db_column='成果水平', verbose_name='成果水平')
    yjxs = models.CharField(max_length=16, db_column='研究形式', verbose_name='研究形式')
    ztfl = models.CharField(max_length=32, db_column='中图分类', verbose_name='中图分类')
    ktly = models.CharField(max_length=16, db_column='课题来源', verbose_name='课题来源')
    ktlxmc = models.CharField(max_length=128, db_column='课题立项名称', verbose_name='课题立项名称')
    ktlxbh = models.CharField(max_length=32, db_column='课题立项编号', verbose_name='课题立项编号')
    jftr = models.CharField(max_length=16, db_column='经费实际投入额（万元）', verbose_name='经费实际投入额')
    pjfs = models.CharField(max_length=16, db_column='评价方式', verbose_name='评价方式')
    pjdw = models.CharField(max_length=64, db_column='评价单位', verbose_name='评价单位')
    pjrq = models.CharField(max_length=32, db_column='评价日期', verbose_name='评价日期')
    zscqxs = models.CharField(max_length=16, db_column='知识产权形式', verbose_name='研究形式')
    yyzt = models.CharField(max_length=16, db_column='应用状态', verbose_name='应用状态')
    zrfw = models.CharField(max_length=16, db_column='转让范围', verbose_name='转让范围')
    tgyys = models.CharField(max_length=16, db_column='推广形式', verbose_name='推广形式')
    lxr = models.CharField(max_length=32, db_column='联系人', verbose_name='联系人')
    phone = models.CharField(max_length=64, db_column='联系人电话', verbose_name='联系人电话')
    email = models.CharField(max_length=256, db_column='联系人email', verbose_name='联系人email')
    address = models.CharField(max_length=512, db_column='单位通讯地址', verbose_name='单位通讯地址')
    postcode = models.CharField(max_length=6, db_column='邮政编码', verbose_name='邮政编码')
    unitphone = models.CharField(max_length=64, db_column='单位电话', verbose_name='单位电话')
    unitfax = models.CharField(max_length=64, db_column='单位传真', verbose_name='单位传真')
    unitnet = models.URLField(max_length=128, db_column='单位网址', verbose_name='单位网址')
    cooperator = models.TextField(db_column='合作完成单位', verbose_name='合作完成单位')

    class Meta:
        db_table = '农业获奖科技成果数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class NykjrcDb(models.Model):
    """
    农业科技人才数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    name = models.CharField(max_length=32, blank=False, null=False, db_column='姓名', verbose_name='姓名')
    gender = models.CharField(max_length=2, db_column='性别', verbose_name='性别')
    birthday = models.CharField(max_length=32, db_column='出生日期', verbose_name='出生日期')
    education = models.CharField(max_length=32, db_column='学历', verbose_name='学历')
    jobtitle = models.CharField(max_length=32, db_column='职称', verbose_name='职称')
    duty = models.CharField(max_length=256, db_column='职务', verbose_name='职务')
    eduback = models.TextField(db_column='教育背景', verbose_name='教育背景')
    direction = models.CharField(max_length=256, db_column='研究方向', verbose_name='研究方向')
    field = models.CharField(max_length=256, db_column='专业领域', verbose_name='专业领域')
    subject = models.CharField(max_length=64, db_column='学科分类', verbose_name='学科分类')
    unit = models.CharField(max_length=256, db_column='工作单位', verbose_name='工作单位')
    desc = models.TextField(db_column='本人简介', verbose_name='本人简介')
    contri = models.TextField(db_column='主要成就', verbose_name='主要成就')
    location = models.CharField(max_length=32, db_column='所在地区', verbose_name='所在地区')
    unit_type = models.CharField(max_length=32, db_column='单位属性', verbose_name='单位属性')
    unitaddress = models.CharField(max_length=256, db_column='单位地址', verbose_name='单位地址')
    postcode = models.CharField(max_length=6, db_column='单位邮编', verbose_name='单位邮编')

    class Meta:
        db_table = '农业科技人才数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class NykjjgDb(models.Model):
    """
    农业科技机构数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    unitid = models.CharField(max_length=64, db_column='机构编号', verbose_name='机构编号')
    gfmc = models.CharField(max_length=256, db_column='规范名称', verbose_name='规范名称')
    ywmc = models.CharField(max_length=256, db_column='英文名称', verbose_name='英文名称')
    qtmc = models.CharField(max_length=512, db_column='其他名称', verbose_name='其他名称')
    clnf = models.CharField(max_length=32, db_column='成立年份', verbose_name='成立年份')
    jglx = models.CharField(max_length=32, db_column='机构类型', verbose_name='机构类型')
    szdq = models.CharField(max_length=256, db_column='所在地区', verbose_name='所在地区')
    sjdw = models.CharField(max_length=256, db_column='上级单位', verbose_name='上级单位')
    desc = models.TextField(db_column='机构简介', verbose_name='机构简介')
    ywjs = models.TextField(db_column='英文简介', verbose_name='英文简介')
    field = models.CharField(max_length=512, db_column='研究领域', verbose_name='研究领域')
    xkfl = models.CharField(max_length=512, db_column='学科分类', verbose_name='学科分类')
    rcdw = models.TextField(db_column='人才队伍', verbose_name='人才队伍')
    jgsz = models.TextField(db_column='机构设置', verbose_name='机构设置')
    kjpt = models.TextField(db_column='科技平台', verbose_name='科技平台')
    zycg = models.TextField(db_column='主要成果', verbose_name='主要成果')
    zbqk = models.TextField(db_column='主办期刊', verbose_name='主办期刊')
    address = models.CharField(max_length=256, db_column='通讯地址', verbose_name='通讯地址')
    postcode = models.CharField(max_length=6, db_column='邮政编码', verbose_name='邮政编码')
    phone = models.CharField(max_length=256, db_column='联系电话', verbose_name='联系电话')
    email = models.CharField(max_length=256, db_column='电子邮箱', verbose_name='电子邮箱')
    fax = models.CharField(max_length=64, db_column='传真', verbose_name='传真')
    net = models.CharField(max_length=256, db_column='网址', verbose_name='网址')

    class Meta:
        db_table = '农业科技机构数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class WwkjwxDb(models.Model):
    """
    外文农业科技文摘数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    title = models.CharField(max_length=1000, db_column='题名', verbose_name='题名')
    author = models.CharField(max_length=1000, db_column='作者', verbose_name='作者')
    keywords = models.CharField(max_length=1000, db_column='关键词', verbose_name='关键词')
    abstract = models.TextField(db_column='摘要', verbose_name='摘要')
    qkname = models.CharField(max_length=300, db_column='期刊名称', verbose_name='期刊名称')
    year = models.CharField(max_length=10, db_column='年', verbose_name='年')
    juan = models.CharField(max_length=100, db_column='卷', verbose_name='卷')
    qi = models.CharField(max_length=100, db_column='期', verbose_name='期')
    start_page = models.CharField(max_length=100, db_column='起如页', verbose_name='起如页')
    end_page = models.CharField(max_length=100, db_column='终止页', verbose_name='终止页')
    issn = models.CharField(max_length=20, db_column='issn号', verbose_name='issn号')

    class Meta:
        db_table = '外文农业科技文摘数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class YjnyDb(models.Model):
    """
    有机农业数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    reportid = models.CharField(max_length=32, db_column='记录号', verbose_name='记录号')
    title = models.CharField(max_length=256, db_column='题名', verbose_name='题名')
    author = models.CharField(max_length=64, db_column='作者', verbose_name='作者')
    keywords = models.CharField(max_length=256, db_column='关键词', verbose_name='关键词')
    category = models.CharField(max_length=64, db_column='分类', verbose_name='分类')
    infotype = models.CharField(max_length=16, db_column='信息类型', verbose_name='信息类型')
    resource = models.CharField(max_length=128, db_column='信息来源', verbose_name='信息来源')
    datetimes = models.CharField(max_length=32, db_column='出版日期', verbose_name='出版日期')
    gslb = models.CharField(max_length=64, db_column='归属类别', verbose_name='归属类别')
    zwflh = models.CharField(max_length=64, db_column='中图分类号', verbose_name='中图分类号')
    szzdw = models.CharField(max_length=128, db_column='首作者单位', verbose_name='首作者单位')
    content = models.TextField(db_column='正文', verbose_name='正文')

    class Meta:
        db_table = '有机农业数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class NybzhczgfDb(models.Model):
    """
    农业标准和操作规范数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    bzid = models.CharField(max_length=32, db_column='标准编号', verbose_name='标准编号')
    bzname = models.CharField(max_length=128, db_column='标准名称', verbose_name='标准名称')
    fbrq = models.CharField(max_length=10, db_column='发布日期', verbose_name='发布日期')
    ssrq = models.CharField(max_length=10, db_column='实施日期', verbose_name='实施日期')
    bzlx = models.CharField(max_length=32, db_column='标准类型', verbose_name='标准类型')
    fbdw = models.CharField(max_length=128, db_column='发布单位', verbose_name='发布单位')
    qcdw = models.CharField(max_length=128, db_column='起草单位', verbose_name='起草单位')
    qcr = models.CharField(max_length=128, db_column='起草人', verbose_name='起草人')
    bzgs = models.TextField(db_column='标准概述（300字以内）', verbose_name='标准概述（300字以内）')
    content = models.TextField(db_column='全文', verbose_name='全文')

    class Meta:
        db_table = '农业标准和操作规范数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class NykjzcfgDb(models.Model):
    """
    农业科技政策法规数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    zcfgmc = models.CharField(max_length=128, db_column='政策法规名称', verbose_name='政策法规名称')
    fbdw = models.CharField(max_length=128, db_column='发布单位', verbose_name='发布单位')
    content = models.TextField(db_column='全文', verbose_name='全文')
    keywords = models.CharField(max_length=128, db_column='关键词', verbose_name='关键词')
    wh = models.CharField(max_length=32, db_column='文号', verbose_name='文号')
    reource = models.CharField(max_length=128, db_column='来源', verbose_name='来源')
    lyljdz = models.CharField(max_length=128, db_column='来源链接地址', verbose_name='来源链接地址')

    class Meta:
        db_table = '农业科技政策法规数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class XqfzffDb(models.Model):
    """
    畜禽常见疾病及防治方法数据库
    """
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    sjhm = models.CharField(max_length=5, db_column='数据号码', verbose_name='数据号码')
    jbmc = models.CharField(max_length=128, db_column='疾病名称', verbose_name='疾病名称')
    xqmc = models.CharField(max_length=	32, db_column='畜禽名称', verbose_name='畜禽名称')
    jblb = models.CharField(max_length=128, db_column='疾病科别', verbose_name='疾病科别')
    abstract = models.TextField(db_column='概述', verbose_name='概述')
    keywords = models.CharField(max_length=256, db_column='关键词', verbose_name='关键词')
    bingyin = models.TextField(db_column='病因', verbose_name='病因')
    byft = models.CharField(max_length=128, db_column='病因附图', verbose_name='病因附图')
    lybx = models.TextField(db_column='流行病学', verbose_name='流行病学')
    blx = models.TextField(db_column='病理学', verbose_name='病理学')
    blxt = models.CharField(max_length=128, db_column='病理学图', verbose_name='病理学图')
    zhenzhuang = models.TextField(db_column='症状', verbose_name='症状')
    zzt = models.CharField(max_length=128, db_column='症状图', verbose_name='症状图')
    zhenduan = models.TextField(db_column='诊断', verbose_name='诊断')
    zhiliao = models.TextField(db_column='治疗', verbose_name='治疗')
    fzcs = models.TextField(db_column='防制措施', verbose_name='防制措施')
    zwflh = models.CharField(max_length=32, db_column='中图分类号', verbose_name='中图分类号')

    class Meta:
        db_table = '畜禽常见疾病及防治方法数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class YearBooksDes(models.Model):
    year = models.CharField(primary_key=True, max_length=4, db_column='年鉴年份', verbose_name='年鉴年份')
    index = models.CharField(max_length=20, db_column='编号', verbose_name='编号')
    chinese = models.CharField(max_length=40, db_column='年鉴中文名', verbose_name='年鉴中文名')
    english = models.CharField(max_length=60, db_column='年鉴英文名', verbose_name='年鉴英文名')
    author = models.CharField(max_length=20, db_column='责任说明', verbose_name='责任说明')
    unit = models.CharField(max_length=60, db_column='主编单位', verbose_name='主编单位')
    pubtime = models.CharField(max_length=20, db_column='出版日期', verbose_name='出版日期')
    page = models.CharField(max_length=20, db_column='页数', verbose_name='页数')
    money = models.CharField(max_length=20, db_column='人民币定价', verbose_name='人民币定价')
    desc = models.TextField(db_column='内容简介', verbose_name='内容简介')
    image = models.ImageField(upload_to="yearbooks/images/", db_column='封面', verbose_name='封面')

    class Meta:
        db_table = '农业统计年鉴概述'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class YearBooksContent(models.Model):
    year = models.ForeignKey(YearBooksDes, db_column='年鉴年份', verbose_name='年鉴年份')
    index = models.IntegerField(db_column='顺序', verbose_name='顺序')
    content = models.CharField(max_length=40, db_column='目录', verbose_name='目录')

    class Meta:
        db_table = '农业统计年鉴目录'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class YearBooks(models.Model):
    id = models.IntegerField(db_column='id', verbose_name='id', blank=True, null=True)
    title = models.CharField(max_length=60, db_column='标题', verbose_name='标题')
    category = models.CharField(max_length=60, db_column='目录', verbose_name='目录')
    page = models.CharField(max_length=20, db_column='年鉴页码', verbose_name='年鉴页码')
    identify = models.CharField(primary_key=True, max_length=20, db_column='编号', verbose_name='编号')
    year = models.ForeignKey(YearBooksDes, db_column='年鉴年份', verbose_name='年鉴年份')
    caj = models.FilePathField(db_column='CAJ', verbose_name='CAJ', blank=True, null=True)
    pdf = models.FilePathField(db_column='PDF', verbose_name='PDF', blank=True, null=True)
    excel = models.FilePathField(db_column='EXCEL', verbose_name='EXCEL', blank=True, null=True)

    class Meta:
        db_table = '农业统计年鉴详情'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class AgriTechDes(models.Model):
    index = models.IntegerField(db_column='显示顺序', verbose_name='显示顺序', blank=True, null=True)
    selectid = models.CharField(max_length=40, db_column='查询号码', verbose_name='查询号码', blank=True, null=True)
    id = models.CharField(max_length=40, db_column='元数据标识符', verbose_name='元数据标识符', blank=True, null=True)
    title = models.CharField(primary_key=True, max_length=60, db_column='数据集名称', verbose_name='数据集名称')
    english = models.CharField(max_length=100, db_column='数据集英文名称', verbose_name='数据集英文名称', blank=True, null=True)
    language = models.CharField(max_length=40, db_column='数据集语种', verbose_name='数据集语种	', blank=True, null=True)
    endtime = models.CharField(max_length=40, db_column='数据集完成日期', verbose_name='数据集完成日期', blank=True, null=True)
    category = models.CharField(max_length=40, db_column='数据集分类', verbose_name='数据集分类	', blank=True, null=True)
    keywords = models.CharField(max_length=100, db_column='关键词', verbose_name='关键词', blank=True, null=True)
    abstract = models.CharField(max_length=200, db_column='数据集摘要', verbose_name='数据集摘要', blank=True, null=True)
    resource = models.CharField(max_length=100, db_column='数据来源', verbose_name='数据来源', blank=True, null=True)
    link = models.CharField(max_length=100, db_column='在线链接地址', verbose_name='在线链接地址', blank=True, null=True)
    update = models.CharField(max_length=40, db_column='维护和更新频率', verbose_name='维护和更新频率', blank=True, null=True)
    limit = models.CharField(max_length=40, db_column='数据集使用局限性', verbose_name='数据集使用局限性', blank=True, null=True)
    safelimit = models.CharField(max_length=40, db_column='数据集安全限制分级', verbose_name='数据集安全限制分级', blank=True, null=True)
    uselimit = models.CharField(max_length=40, db_column='数据集使用限制', verbose_name='数据集使用限制', blank=True, null=True)
    accesslimit = models.CharField(max_length=40, db_column='数据集访问限制', verbose_name='数据集访问限制', blank=True, null=True)
    unit = models.CharField(max_length=40, db_column='负责单位', verbose_name='负责单位', blank=True, null=True)
    dutyer = models.CharField(max_length=40, db_column='负责人', verbose_name='负责人', blank=True, null=True)
    duty = models.CharField(max_length=40, db_column='职责', verbose_name='职责', blank=True, null=True)
    country = models.CharField(max_length=40, db_column='国家', verbose_name='国家', blank=True, null=True)
    city = models.CharField(max_length=40, db_column='城市', verbose_name='城市', blank=True, null=True)
    address = models.CharField(max_length=40, db_column='地址', verbose_name='地址', blank=True, null=True)
    post = models.CharField(max_length=40, db_column='邮政编码', verbose_name='邮政编码', blank=True, null=True)
    email = models.CharField(max_length=40, db_column='电子邮件地址', verbose_name='电子邮件地址', blank=True, null=True)
    phone = models.CharField(max_length=40, db_column='电话', verbose_name='电话', blank=True, null=True)
    fax = models.CharField(max_length=40, db_column='传真', verbose_name='传真', blank=True, null=True)
    click_num = models.IntegerField(default=0, verbose_name="点击数", db_column='点击数')
    fav_num = models.IntegerField(default=0, verbose_name="收藏数", db_column='收藏数')

    class Meta:
        db_table = '农业科技数据概述'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class AgriTechContent(models.Model):
    title = models.ForeignKey(AgriTechDes, db_column='数据集名称', verbose_name='数据集名称', blank=True, null=True)
    index = models.IntegerField(db_column='顺序', verbose_name='顺序', blank=True, null=True)
    content = models.CharField(max_length=30, db_column='目录', verbose_name='目录', blank=True, null=True)
    fieldtype = models.CharField(max_length=20, db_column='字段类型', verbose_name='字段类型', blank=True, null=True)
    fieldlength = models.CharField(max_length=10, db_column='字段长度', verbose_name='字段长度', blank=True, null=True)
    display = models.IntegerField(default=0, db_column='是否显示', verbose_name='是否显示', blank=True, null=True)
    english = models.CharField(max_length=20, db_column='字段', verbose_name='字段', blank=True, null=True)

    class Meta:
        db_table = '农业科技数据目录'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class FieldContent(models.Model):
    title = models.CharField(max_length=30, db_column='数据集名称', verbose_name='数据集名称', blank=True, null=True)
    index = models.IntegerField(db_column='顺序', verbose_name='顺序', blank=True, null=True)
    content = models.CharField(max_length=30, db_column='目录', verbose_name='目录', blank=True, null=True)
    fieldtype = models.CharField(max_length=20, db_column='字段类型', verbose_name='字段类型', blank=True, null=True)
    fieldlength = models.CharField(max_length=10, db_column='字段长度', verbose_name='字段长度', blank=True, null=True)
    display = models.IntegerField(default=0, db_column='是否显示', verbose_name='是否显示', blank=True, null=True)
    english = models.CharField(max_length=20, db_column='字段', verbose_name='字段', blank=True, null=True)

    class Meta:
        db_table = '字段数据目录'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class GjnydbDes(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=0)
    title = models.CharField(max_length=60, db_column='数据集名称', verbose_name='数据集名称', blank=True, null=True)
    category = models.CharField(max_length=10, db_column='类别', verbose_name='类别', blank=True, null=True)
    index = models.IntegerField(db_column='显示顺序', verbose_name='显示顺序', default=0, blank=True, null=True)
    records = models.IntegerField(db_column='记录数', verbose_name='记录数', default=0, blank=True, null=True)
    click_num = models.IntegerField(default=0, verbose_name="点击数", db_column='点击数', blank=True, null=True)
    fav_num = models.IntegerField(default=0, verbose_name="收藏数", db_column='收藏数', blank=True, null=True)
    resource = models.CharField(max_length=100, db_column='来源', verbose_name='来源', blank=True, null=True)
    down_num = models.CharField(max_length=20, db_column='下载次数', verbose_name='下载次数', blank=True, null=True)
    pubtime = models.CharField(max_length=20, db_column='发布时间', verbose_name='发布时间', blank=True, null=True)
    desc = models.CharField(max_length=200, db_column='简介', verbose_name='简介', blank=True, null=True)

    class Meta:
        db_table = '国家农业数据集概述'
        verbose_name = db_table
        verbose_name_plural = verbose_name


class CsvHtmls(models.Model):
    slug = models.CharField(max_length=60, db_column='标题', verbose_name='标题', blank=True, null=True)
    file = models.FileField(upload_to="text/", max_length=60, db_column='下载', verbose_name='下载', blank=True, null=True)
    category = models.CharField(max_length=60, db_column='类别', verbose_name='类别', blank=True, null=True)

    class Meta:
        db_table = '下载文件'
        verbose_name = db_table
        verbose_name_plural = verbose_name
