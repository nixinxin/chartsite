from django.db import models

# Create your models here.


class GwyjzwzzzyDb(models.Model):
    """
    国外引进作物种质资源数据库
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
        db_table = "国外引进作物种质资源数据库"
        verbose_name = "国外引进作物种质资源数据库"
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
    county = models.CharField(max_length=20, null=True, blank=True, verbose_name='区县', db_column="区县")
    provincecode = models.IntegerField(null=True, blank=True, verbose_name='省份编码', db_column="省份编码")
    citycode = models.IntegerField(null=True, blank=True, verbose_name='城市编码', db_column="城市编码")
    countycode = models.IntegerField(null=True, blank=True, verbose_name='区县编码', db_column="区县编码")
    alias = models.CharField(max_length=10, null=True, blank=True, verbose_name='别名', db_column="别名")

    class Meta:
        db_table = "行政区划清单"
        verbose_name = "行政区划清单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.county


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
        verbose_name = "农业统计指标"
        verbose_name_plural = verbose_name
        unique_together = (("index", 'values', 'location', 'year'), )

    def __str__(self):
        return self.index


class MytxDb(models.Model):
    """
    农作物名、优、特新品种数据库
    """
    category = models.CharField(max_length=20, null=True, blank=True, verbose_name="作物类别", db_column="作物类别")
    brands = models.CharField(max_length=20, null=True, blank=True, verbose_name="作物品种", db_column="作物品种")
    name = models.CharField(max_length=40, primary_key=True, null=False, verbose_name="作物名称", db_column="作物名称")
    desc = models.TextField(verbose_name='基本情况', null=True, blank=True, db_column="基本情况")
    feature = models.TextField(verbose_name='特征特性', null=True, blank=True, db_column="特征特性")
    raiser = models.CharField(max_length=80,  null=True, blank=True, verbose_name="培育者", db_column="培育者")
    location_T = models.TextField(verbose_name='地区及技术', null=True, blank=True, db_column="地区及技术")
    brands_category = models.CharField(max_length=20, null=True, blank=True, verbose_name="品种类别", db_column="品种类别")
    examine = models.TextField(null=True, blank=True, verbose_name="审查情况", db_column='审查情况')
    get_day = models.CharField(max_length=10, null=True, blank=True, verbose_name="资源采集日", db_column="资源采集日")

    class Meta:
        db_table = "农作物名、优、特新品种数据库"
        verbose_name = "农作物名、优、特新品种数据库"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ZgnytdkcDb(models.Model):
    """
    中国农业天敌昆虫数据库
    """
    id = models.IntegerField(primary_key=True)
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

    class Meta:
        db_table = '中国农业天敌昆虫数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgnyyhswDb_image(models.Model):
    """
    中国农业有害生物数据库_图片
    """
    name = models.CharField(max_length=40, blank=True, null=True, db_column='名称', verbose_name="名称")
    species = models.CharField(max_length=40, blank=True, null=True, db_column='种类', verbose_name="种类")
    link = models.CharField(max_length=60, blank=True, null=True, db_column='链接', verbose_name="链接")

    class Meta:
        db_table = '中国农业有害生物数据库_图片'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ZgnttdzzDb(models.Model):
    """
    中国农田天敌蜘蛛数据库
    """
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

    class Meta:
        db_table = '中国农田天敌蜘蛛数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgnthsDb(models.Model):
    """
    中国农田害鼠数据库
    """
    id = models.IntegerField(primary_key=True)
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

    class Meta:
        db_table = '中国农田害鼠数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgyclschcDb(models.Model):
    """
    中国叶菜类蔬菜害虫数据库
    """
    id = models.IntegerField(primary_key=True)
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

    class Meta:
        db_table = '中国叶菜类蔬菜害虫数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgwlrqwswDb(models.Model):
    """
    中国外来入侵微生物数据库
    """
    id = models.IntegerField(primary_key=True)
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
        db_table = '中国外来入侵微生物数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgwlrqkcDb(models.Model):
    """
    中国外来入侵昆虫数据库
    """
    id = models.IntegerField(primary_key=True)
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

    class Meta:
        db_table = '中国外来入侵昆虫数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgwlrqzwDb(models.Model):
    """
    中国外来入侵植物数据库
    """
    id = models.IntegerField(primary_key=True, db_column='编号', verbose_name='编号')
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

    class Meta:
        db_table = '中国外来入侵植物数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZghdzcDb(models.Model):
    """
    中国旱地杂草数据库
    """
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
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
    title = models.CharField(primary_key=True, max_length=60, db_column='标题', verbose_name='标题')
    location = models.CharField(max_length=60, blank=True, null=True, db_column='地点', verbose_name='地点')
    feature = models.CharField(max_length=100, blank=True, null=True, db_column='特征', verbose_name='特征')
    brands = models.CharField(max_length=60, blank=True, null=True, db_column='地理标志', verbose_name='地理标志')
    desc = models.TextField(blank=True, null=True, db_column='基本介绍', verbose_name='基本介绍')
    layout = models.TextField(blank=True, null=True, db_column='产业布局', verbose_name='产业布局')
    history = models.TextField(blank=True, null=True, db_column='历史', verbose_name='历史')

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
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
    hazard_buwei = models.TextField(blank=True, null=True, db_column='主要危害部位', verbose_name='主要危害部位')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    symptom = models.TextField(blank=True, null=True, db_column='为害症状', verbose_name='为害症状')
    disease_type = models.CharField(max_length=20, blank=True, null=True, db_column='病害类型', verbose_name='病害类型')
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    by_zhname = models.CharField(max_length=60, blank=True, null=True, db_column='病原中文名', verbose_name='病原中文名')
    by_xuename = models.TextField(blank=True, null=True, db_column='病原拉丁学名', verbose_name="病原拉丁学名")
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    byfldw = models.CharField(max_length=30, blank=True, null=True, db_column='病原分类地位', verbose_name='病原分类地位')
    byxttz = models.TextField(blank=True, null=True, db_column='病原形态特征', verbose_name='病原形态特征')
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    pathway_fbtj = models.TextField(blank=True, null=True, db_column='传播途径和发病条件', verbose_name='传播途径和发病条件')

    control_way = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    alias = models.CharField(max_length=30, blank=True, null=True, db_column='别名', verbose_name='别名')

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
    id = models.IntegerField(primary_key=True)
    hazard_buwei = models.TextField(blank=True, null=True, db_column='主要危害部位', verbose_name='主要危害部位')
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    symptom = models.TextField(blank=True, null=True, db_column='为害症状', verbose_name='为害症状')
    disease_type = models.CharField(max_length=20, blank=True, null=True, db_column='病害类型', verbose_name='病害类型')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    by_zhname = models.CharField(max_length=60, blank=True, null=True, db_column='病原中文名', verbose_name='病原中文名')
    by_xuename = models.TextField(blank=True, null=True, db_column='病原拉丁学名', verbose_name='病原拉丁学名')
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    byfldw = models.CharField(max_length=60, blank=True, null=True, db_column='病原分类地位', verbose_name='病原分类地位')
    byxttz = models.TextField(blank=True, null=True, db_column='病原形态特征', verbose_name='病原形态特征')
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    alias = models.CharField(max_length=40, blank=True, null=True, db_column='别名', verbose_name='别名')
    control_way = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    pathway_fbtj = models.TextField(blank=True, null=True, db_column='传播途径和发病条件', verbose_name='传播途径和发病条件')

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
    id = models.IntegerField(primary_key=True)
    hazard_buwei = models.TextField(blank=True, null=True, db_column='主要危害部位', verbose_name='主要危害部位')
    distribution = models.TextField(blank=True, null=True, db_column='地理分布', verbose_name='地理分布')
    symptom = models.TextField(blank=True, null=True, db_column='为害症状', verbose_name='为害症状')
    disease_type = models.CharField(max_length=30, blank=True, null=True, db_column='病害类型', verbose_name='病害类型')
    zhname = models.CharField(max_length=60, blank=True, null=True, db_column='中文名', verbose_name="中文名")
    by_zhname = models.CharField(max_length=60, blank=True, null=True, db_column='病原中文名', verbose_name='病原中文名')
    by_xuename = models.TextField(blank=True, null=True, db_column='病原拉丁学名', verbose_name='病原拉丁学名')
    major_hazard = models.TextField(blank=True, null=True, db_column='主要危害作物', verbose_name="主要危害作物")
    alias = models.CharField(max_length=30, blank=True, null=True, db_column='别名', verbose_name='别名')
    byfldw = models.CharField(max_length=30, blank=True, null=True, db_column='病原分类地位', verbose_name='病原分类地位')
    byxttz = models.TextField(blank=True, null=True, db_column='病原形态特征', verbose_name='病原形态特征')
    related_articles = models.TextField(blank=True, null=True, db_column='相关文献', verbose_name="相关文献")
    control_way = models.TextField(blank=True, null=True, db_column='防治方法', verbose_name="防治方法")
    english = models.CharField(max_length=60, blank=True, null=True, db_column='英文名', verbose_name="英文名")
    report_id = models.CharField(max_length=10, blank=True, null=True, db_column='记录号', verbose_name="记录号")
    pathway_fbtj = models.TextField(blank=True, null=True, db_column='传播途径和发病条件', verbose_name='传播途径和发病条件')

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
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
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

    class Meta:
        db_table = '中国经济作物细菌病害数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgpgtlhcDb(models.Model):
    """
    中国苹果、桃、梨害虫数据库
    """
    id = models.IntegerField(primary_key=True)
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

    class Meta:
        db_table = '中国苹果、桃、梨害虫数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zhname


class ZgxzqhDb(models.Model):
    """
    中国行政区划数据库
    """
    citycode = models.IntegerField(blank=True, null=True, db_column='城市编码', verbose_name='城市编码')
    adcode = models.CharField(primary_key=True, max_length=6, db_column='地址编码',  verbose_name='地址编码')
    name = models.CharField(max_length=20, primary_key=True, db_column='位置名称', verbose_name='位置名称')
    center = models.CharField(max_length=30, primary_key=True, db_column='中心坐标', verbose_name='中心坐标')
    level = models.CharField(max_length=10, blank=True, null=True, db_column='位置级别', verbose_name='位置级别')

    class Meta:
        managed = False
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
    title = models.CharField(max_length=50, blank=True, null=True, db_column='标题', verbose_name='标题')
    pici = models.CharField(max_length=10, blank=True, null=True, db_column='批次', verbose_name='批次')
    content = models.TextField(blank=True, null=True, db_column='内容', verbose_name='内容')
    link = models.CharField(max_length=80, blank=True, null=True, db_column='链接', verbose_name='链接')
    source = models.CharField(max_length=40, blank=True, null=True, db_column='来源', verbose_name='来源')
    clicks = models.CharField(max_length=10, blank=True, null=True, db_column='点击次数', verbose_name='点击次数')
    datetime = models.CharField(max_length=20, blank=True, null=True, db_column='日期', verbose_name='日期')

    class Meta:
        db_table = '中国重要农业文化遗产'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Zgzynywhyc_image(models.Model):
    """
    中国重要农业文化遗产_图片
    """
    title = models.CharField(max_length=40, blank=True, null=True, db_column='标题', verbose_name='标题')
    image_num = models.IntegerField(blank=True, null=True, db_column='图片号', verbose_name='图片号')
    pici = models.CharField(max_length=20, blank=True, null=True, db_column='批次', verbose_name='批次')
    path = models.CharField(max_length=50, blank=True, null=True, db_column='路径', verbose_name='路径')

    class Meta:
        db_table = '中国重要农业文化遗产_图片'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ZwwzfbDb(models.Model):
    """
    作物物种分布数据库
    """
    title = models.CharField(max_length=50, blank=True, null=True, db_column='标题', verbose_name='标题')
    category = models.CharField(max_length=30, blank=True, null=True, db_column='种类', verbose_name='种类')
    path = models.CharField(max_length=80, blank=True, null=True, db_column='路径', verbose_name='路径')

    class Meta:
        db_table = '作物物种分布数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class XmzzzzhxzzDb(models.Model):
    """
    小麦种质资源核心种质数据库
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
        db_table = '小麦种质资源核心种质数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class XmxpDb(models.Model):
    """
    小麦系谱数据库
    """
    id = models.IntegerField(primary_key=True)
    unit_id = models.IntegerField(blank=True, null=True, db_column='品资所编号', verbose_name='品资所编号')
    name = models.CharField(max_length=40, blank=True, null=True, db_column='品种名称', verbose_name='品种名称')
    family = models.CharField(max_length=100, blank=True, null=True, db_column='系谱', verbose_name='系谱')
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
    水稻种质资源核心种质数据库
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
        db_table = '水稻种质资源核心种质数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SdycpzjqpxDb(models.Model):
    """
    水稻育成品种及其系谱数据库
    """
    kucode = models.CharField(max_length=10, blank=True, null=True, db_column='库编号', verbose_name='库编号')
    totalcode = models.CharField(primary_key=True, max_length=10, db_column='统一编号', verbose_name='统一编号')
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
        unique_together = (('totalcode', 'name'),)
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class YmxpzbhDb(models.Model):
    """
    玉米新品种保护数据库
    """
    id = models.IntegerField(primary_key=True)
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
    玉米种质资源核心种质数据库
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
        db_table = '玉米种质资源核心种质数据库'
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
    作物优异资源种质数据库
    """
    name = models.CharField(primary_key=True, max_length=40, db_column='种质名称', verbose_name='种质名称')
    xiaolei = models.CharField(max_length=20, blank=True, null=True, db_column='种质小类', verbose_name='种质小类')
    dalei = models.CharField(max_length=20, blank=True, null=True, db_column='种质大类', verbose_name='种质大类')
    type = models.CharField(max_length=60, blank=True, null=True, db_column='种质类型', verbose_name='种质类型')
    source = models.TextField(blank=True, null=True, db_column='种质来源', verbose_name='种质来源')
    shape = models.TextField(blank=True, null=True, db_column='优异性状', verbose_name='优异性状')
    values = models.TextField(blank=True, null=True, db_column='利用价值', verbose_name='利用价值')
    evaluate_class = models.CharField(max_length=10, blank=True, null=True, db_column='评定等级', verbose_name='评定等级')
    unit = models.CharField(max_length=30, blank=True, null=True, db_column='联系单位', verbose_name='联系单位')

    class Meta:
        db_table = '作物优异资源种质数据库'
        verbose_name = db_table
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
