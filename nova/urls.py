"""nova URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.global_settings import MEDIA_ROOT
from django.conf.urls import url, include

from django.views.static import serve

from apps.core import admin
from apps.core.views.ContaineView import ContainerView
from apps.users.views.ActiveUserView import ActiveUserView
from apps.users.views.ForgetPwdView import ForgetPwdView
from apps.users.views.IndexView import IndexView
from apps.users.views.LoginView import LoginView
from apps.users.views.LogoutView import LogoutView
from apps.users.views.ModifyPwdView import ModifyPwdView
from apps.users.views.RegisterView import RegisterView
from apps.users.views.ResetView import ResetView

urlpatterns = [
    # url(r'^xadmin/', admin.site.urls),
    # url('admin/', admin.site.urls),
    # url(r'^core', ContainerView.as_view(), name='core'),
    # 配置页面
    url('^$', IndexView.as_view(), name="index"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),

    # 验证用户注册后，在邮件里点击注册链接
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),

    # 退出登录
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    # 课程机构URL配置
    url(r'^org/', include('apps.organization.urls', namespace="org")),

    # 课程相关URL配置
    url(r'^courses/', include('apps.courses.urls', namespace="courses")),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    # url(r'^static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),

    # 课程相关URL配置
    url(r'^pingusers/', include('apps.users.urls', namespace="pingusers")),
]

# 全局 404 页面配置（django 会自动调用这个变量）
handler404 = 'users.views.otherView.page_not_found'
handler500 = 'users.views.otherView.page_error'
