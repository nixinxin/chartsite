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
from operation.views import UserFavViewset, FeedBackViewset
from users.views import *

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



urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

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
    url('^user/forget/$', ForgetView.as_view(), name="login"),
    url(r'^user/personal/$', PersonalViewset.as_view(), name='personal'),
    url(r'^account/$', AccountView.as_view(), name='account'),
    url(r'^share/$', ShareView.as_view(), name='share'),
    url(r'^service/$', ServiceView.as_view(), name='service'),

    url(r'^captcha/', include('captcha.urls')),
    url(r'^favicon.ico$', FaviconView.as_view(), name='ico'),


]
