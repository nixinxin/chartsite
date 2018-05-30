from django.conf.urls import url

from .views import *



urlpatterns = [
    url('^logout/$', LogoutView.as_view(), name="logout"),
    url('^register/$', RegisterView.as_view(), name="register"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^forget/$', ForgetView.as_view(), name="forget"),
    url(r'^personal/$', PersonalViewset.as_view(), name='personal'),
    url(r'^account/$', AccountView.as_view(), name='account'),
    url(r'^invite/$', InviteView.as_view(), name='invite'),
]