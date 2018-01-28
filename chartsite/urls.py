"""chartsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.static import serve
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from chart.views import BannerViewset
from chartsite.settings import MEDIA_ROOT
# from chartsite.settings import STATIC_ROOT
from operation.views import UserFavViewset, FeedBackViewset
from users.views import *
from apps.resource.views import *

router = DefaultRouter()

# 配置手机验证码url
router.register(r"phonecodes", PhoneCodeViewset, base_name='phonecodes')

# 配置邮箱验证码url
router.register(r"emailcodes", EmailCodeViewset, base_name='emailcodes')


# 配置图片验证码url
router.register(r"imagecode", ImageCodeViewset, base_name='imagecode')

# 验证用户
router.register(r"users", UserViewset, base_name='users')

# 收藏
router.register(r"userfavs", UserFavViewset, base_name='userfavs')

# 轮播图url
router.register(r"banners", BannerViewset, base_name='banners')

# 留言
router.register(r'messages', FeedBackViewset, base_name='messages')

# 个人中心
router.register(r'personal', PersonalViewset, base_name='personal')

# 验证图片验证码
router.register(r'verify', ImageCodeVerifyViewset, base_name='verify')


# 数据资源列表
router.register(r'resourceList', ResourceListViewSet, base_name='resourceList')

# 国外引进作物种质资源数据库
router.register(r'GwyjzwzzzyDb', GwyjzwzzzyDbListViewSet, base_name='GwyjzwzzzyDb')

# 农产品价格行情数据库
router.register(r'NcpjgDb', NcpjgDbListViewSet, base_name='NcpjgDb')

# 农业统计指标
router.register(r'AgriIndex', AgriIndexViewSet, base_name='AgriIndex')

# 农作物名优特新品种数据库
router.register(r'MytxDb', MytxDbViewSet, base_name='MytxDb')

# 农作物名优特新品种数据库
router.register(r'ZgnytdkcDb', ZgnytdkcDbViewSet, base_name='ZgnytdkcDb')

# 中国农业有害生物图片数据库
router.register(r'ZgnyyhswDbTp', ZgnyyhswDbTpViewSet, base_name='ZgnyyhswDbTp')

# 中国农田天敌蜘蛛数据库
router.register(r'ZgnttdzzDb', ZgnttdzzDbViewSet, base_name='ZgnttdzzDb')

# 中国农田害鼠数据库
router.register(r'ZgnthsDb', ZgnthsDbViewSet, base_name='ZgnthsDb')

# 中国叶菜类蔬菜害虫数据库
router.register(r'ZgyclschcDb', ZgyclschcDbViewSet, base_name='ZgyclschcDb')

# 中国外来入侵微生物数据库
router.register(r'ZgwlrqwswDb', ZgwlrqwswDbViewSet, base_name='ZgwlrqwswDb')

# 中国外来入侵昆虫数据库
router.register(r'ZgwlrqkcDb', ZgwlrqkcDbViewSet, base_name='ZgwlrqkcDb')

# 中国外来入侵植物数据库
router.register(r'ZgwlrqzwDb', ZgwlrqzwDbViewSet, base_name='ZgwlrqzwDb')

# 中国旱地杂草数据库
router.register(r'ZghdzcDb', ZghdzcDbViewSet, base_name='ZghdzcDb')

# 中国旱粮作物害虫数据库
router.register(r'ZghlzwhcDb', ZghlzwhcDbViewSet, base_name='ZghlzwhcDb')

# 中国果菜类蔬菜害虫数据库
router.register(r'ZggslschcDb', ZggslschcDbViewSet, base_name='ZggslschcDb')

# 中国柑桔害虫数据库
router.register(r'ZggjhcDb', ZggjhcDbViewSet, base_name='ZggjhcDb')

# 中国棉花害虫数据库
router.register(r'ZgmhhcDb', ZgmhhcDbViewSet, base_name='ZgmhhcDb')

# 中国水田杂草数据库
router.register(r'ZgstzcDb', ZgstzcDbViewSet, base_name='ZgstzcDb')

# 中国水稻害虫数据库
router.register(r'ZgsdhcDb', ZgsdhcDbViewSet, base_name='ZgsdhcDb')

# 中国特色农产品
router.register(r'ZgtsNcp', ZgtsNcpViewSet, base_name='ZgtsNcp')

# 中国粮食作物病毒病害数据库
router.register(r'ZglszwbdbhDb', ZglszwbdbhDbViewSet, base_name='ZglszwbdbhDb')

# 中国粮食作物真菌病害数据库
router.register(r'ZglszwzjbhDb', ZglszwzjbhDbViewSet, base_name='ZglszwzjbhDb')

# 中国粮食作物细菌病害数据库
router.register(r'ZglszwxjbhDb', ZglszwxjbhDbViewSet, base_name='ZglszwxjbhDb')

# 中国经济作物病毒病害数据库
router.register(r'ZgjjzwbdbhDb', ZgjjzwbdbhDbViewSet, base_name='ZgjjzwbdbhDb')

# 中国经济作物真菌病害数据库
router.register(r'ZgjjzwzjbhDb', ZgjjzwzjbhDbViewSet, base_name='ZgjjzwzjbhDb')

# 中国经济作物细菌病害数据库
router.register(r'ZgjjzwxjbhDb', ZgjjzwxjbhDbViewSet, base_name='ZgjjzwxjbhDb')

# 中国苹果桃梨害虫数据库
router.register(r'ZgpgtlhcDb', ZgpgtlhcDbViewSet, base_name='ZgpgtlhcDb')

# 中国行政区划数据库
router.register(r'ZgxzqhDb', ZgxzqhDbViewSet, base_name='ZgxzqhDb')

# 中国重要农业文化遗产
router.register(r'ZgzynywhYc', ZgzynywhYcViewSet, base_name='ZgzynywhYc')

# 中国重要农业文化遗产_图片
router.register(r'ZgzynywhycTp', ZgzynywhycTpViewSet, base_name='ZgzynywhycTp')

# 作物物种分布数据库
router.register(r'ZwwzfbDb', ZwwzfbDbViewSet, base_name='ZwwzfbDb')

# 小麦种质资源核心种质数据库
router.register(r'XmzzzzhxzzDb', XmzzzzhxzzDbViewSet, base_name='XmzzzzhxzzDb')

# 小麦系谱数据库
router.register(r'XmxpDb', XmxpDbViewSet, base_name='XmxpDb')

# 小麦育成品种及其系谱数据库
router.register(r'XmxcpzjqxpDb', XmxcpzjqxpDbViewSet, base_name='XmxcpzjqxpDb')

# 水稻种质资源核心种质数据库
router.register(r'SdzzzzhxzzDb', SdzzzzhxzzDbViewSet, base_name='SdzzzzhxzzDb')

# 水稻育成品种及其系谱数据库
router.register(r'SdycpzjqpxDb', SdycpzjqpxDbViewSet, base_name='SdycpzjqpxDb')

# 玉米新品种保护数据库
router.register(r'YmxpzbhDb', YmxpzbhDbViewSet, base_name='YmxpzbhDb')

# 玉米种质资源核心种质数据库
router.register(r'YmzzzzhxzzDb', YmzzzzhxzzDbViewSet, base_name='YmzzzzhxzzDb')

# 现代农业示范区
router.register(r'Xdnysfq', XdnysfqViewSet, base_name='Xdnysfq')

# 作物优异资源种质数据库
router.register(r'ZwyyzyzzDb', ZwyyzyzzDbViewSet, base_name='ZwyyzyzzDb')

# 优异资源综合评价数据库_大麦
router.register(r'Youdamai', YoudamaiViewSet, base_name='Youdamai')

# 优异资源综合评价数据库_玉米
router.register(r'YouYuMi', YouYuMiViewSet, base_name='YouYuMi')

# 优异资源综合评价数据库列表
router.register(r'ZwyczytxpjjdDbList', ZwyczytxpjjdDbListViewSet, base_name='ZwyczytxpjjdDbList')


# 国际农业科研项目数据库
router.register(r'GjnykyhzxmDb', GjnykyhzxmDbViewSet, base_name='GjnykyhzxmDb')

# 国内农业科技项目数据库
router.register(r'GnnykyhzxmDb', GnnykyhzxmDbViewSet, base_name='GnnykyhzxmDb')

# 农业获奖科技成果数据库
router.register(r'NyhjkjcgDb', NyhjkjcgDbViewSet, base_name='NyhjkjcgDb')

# 农业科技人才数据库
router.register(r'NykjrcDb', NykjrcDbViewSet, base_name='NykjrcDb')

# 农业科技机构数据库
router.register(r'NykjjgDb', NykjjgDbViewSet, base_name='NykjjgDb')

# 中文农业科技文摘数据库
router.register(r'ZwkjwxDb', ZwkjwxDbViewSet, base_name='ZwkjwxDb')

# 有机农业数据库
router.register(r'YjnyDb', YjnyDbViewSet, base_name='YjnyDb')

# 农业古籍数据库
router.register(r'NygjDb', NygjDbViewSet, base_name='NygjDb')

# 农业古籍图片数据库
router.register(r'NygjtpDb', NygjtpDbViewSet, base_name='NygjtpDb')

# 农业标准和操作规范数据库
router.register(r'NybzhczgfDb', NybzhczgfDbViewSet, base_name='NybzhczgfDb')

# 农业科技政策法规数据库
router.register(r'NykjzcfgDb', NykjzcfgDbViewSet, base_name='NykjzcfgDb')

# 畜禽常见疾病及防治方法数据库
router.register(r'XqfzffDb', XqfzffDbViewSet, base_name='XqfzffDb')

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # url(r'^static/(?P<path>.*)$',  serve, {"document_root": STATIC_ROOT}),

    # 富文本相关url
    url(r'^ueditor/', include('DjangoUeditor.urls')),

    # # 数据列表页
    url(r'^', include(router.urls)),

    # 登陆url
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # 首页
    url(r'^index/', TemplateView.as_view(template_name="index.html"), name="index"),

    # 不要加$符号
    url(r'docs/', include_docs_urls(title='chartsite')),

    # token机制.drf 自带认证模式
    url(r'^api-token-auth/', obtain_auth_token),

    # jwt认证模式
    url(r'^login/$', obtain_jwt_token),

    # 第三方登陆
    url('', include('social_django.urls', namespace='social')),


    # 用户登录注册页面
    url('^user/register/$', RegisterView.as_view(), name="register"),
    url('^user/login/$', LoginView.as_view(), name="login"),
    url('^user/forget/$', ForgetView.as_view(), name="forget"),
    url(r'^personal/$', PersonalViewset.as_view(), name='personal'),
    url(r'^account/$', AccountView.as_view(), name='account'),
    url(r'^share/$', ShareView.as_view(), name='share'),
    url(r'^service/$', ServiceView.as_view(), name='service'),
    url(r'^invite/$', InviteView.as_view(), name='invite'),
    url(r'^resource/$', ResourceView.as_view(), name='resource'),
    url(r'^visual/$', VisualView.as_view(), name='visual'),
    url(r'^chart/$', ChartView.as_view(), name='chart'),
    url(r'^csvhtml/$', CsvHtmlView.as_view(), name='csvhtml'),

    url(r'^captcha/', include('captcha.urls')),
    url(r'^favicon.ico$', FaviconView.as_view(), name='ico'),
    url(r'^test/$', TemplateViews.as_view(), name='test'),


]


# 全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
