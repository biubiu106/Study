"""myweb_dj URL Configuration

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
from django.contrib import admin
from django.urls import path

from django.conf.urls import url,include
from app01 import views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$',views.index),# 设置默认主页
    url(r'index/$', views.index),  # 主页
    url(r'login/$', views.login),  # 登录
    url(r'user/$', views.user), # 查看用户
    url(r'userdel-(?P<nid>\d+)/$', views.userdel),  # 删除用户
    url(r'error404/$', views.error404),
    url(r'ajax_menu_dir/', views.ajax_menu_dir), # ajax 获取目录名
    url(r'ajax_menu_files/', views.ajax_menu_files), # ajax 获取文件名

    url(r'videourl/$', views.videoDisplay),

    url(r'pdf-01-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-01-01-'}), # 电路
    url(r'txt-01-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-01-01-'}),

    url(r'pdf-01-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-01-02-'}), # 数电
    url(r'txt-01-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-01-02-'}),

    url(r'pdf-01-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-01-03-'}), # 模电
    url(r'txt-01-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-01-03-'}),

    url(r'pdf-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-02-'}), # C语言基础
    url(r'txt-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-02-'}),

    url(r'pdf-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-03-'}), # 51单片机
    url(r'txt-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-03-'}),

    url(r'pdf-04-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-04-05-'}), # STM32
    url(r'txt-04-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-04-05-'}),

    url(r'pdf-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-05-'}), # 绘制原理图及PCB
    url(r'txt-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-05-'}),

    url(r'pdf-06-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-06-'}), # Linux基础
    url(r'txt-06-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-06-'}),

    url(r'pdf-07-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-07-01-'}), # ARM裸机
    url(r'txt-07-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-07-01-'}),
    url(r'pdf-07-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-07-02-'}),
    url(r'txt-07-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-07-02-'}),
    url(r'pdf-07-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-07-03-'}),
    url(r'txt-07-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-07-03-'}),
    url(r'pdf-07-04-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-07-04-'}),
    url(r'txt-07-04-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-07-04-'}),
    url(r'pdf-07-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-07-05-'}),
    url(r'txt-07-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-07-05-'}),
    url(r'pdf-07-06-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-07-06-'}),
    url(r'txt-07-06-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-07-06-'}),
    url(r'pdf-07-07-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-07-07-'}),
    url(r'txt-07-07-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-07-07-'}),
    url(r'pdf-07-08-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-07-08-'}),
    url(r'txt-07-08-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-07-08-'}),
    url(r'pdf-07-09-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-07-09-'}),
    url(r'txt-07-09-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-07-09-'}),
    url(r'pdf-07-10-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-07-10-'}),
    url(r'txt-07-10-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-07-10-'}),
    url(r'pdf-07-11-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-07-11-'}),
    url(r'txt-07-11-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-07-11-'}),
    url(r'pdf-07-12-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-07-12-'}),
    url(r'txt-07-12-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-07-12-'}),
    url(r'pdf-07-13-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-07-13-'}),
    url(r'txt-07-13-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-07-13-'}),
    url(r'pdf-07-14-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-07-14-'}),
    url(r'txt-07-14-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-07-14-'}),
    url(r'pdf-07-15-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-07-15-'}),
    url(r'txt-07-15-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-07-15-'}),
    url(r'pdf-07-16-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-07-16-'}),
    url(r'txt-07-16-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-07-16-'}),

    url(r'pdf-08-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-08-01-'}), # ARM裸机
    url(r'txt-08-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-08-01-'}),
    url(r'pdf-08-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-08-02-'}),
    url(r'txt-08-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-08-02-'}),
    url(r'pdf-08-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-08-03-'}),
    url(r'txt-08-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-08-03-'}),
    url(r'pdf-08-04-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-08-04-'}),
    url(r'txt-08-04-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-08-04-'}),
    url(r'pdf-08-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-08-05-'}),
    url(r'txt-08-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-08-05-'}),
    url(r'pdf-08-06-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-08-06-'}),
    url(r'txt-08-06-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-08-06-'}),
    url(r'pdf-08-07-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-08-07-'}),
    url(r'txt-08-07-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-08-07-'}),
    url(r'pdf-08-08-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-08-08-'}),
    url(r'txt-08-08-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-08-08-'}),
    url(r'pdf-08-09-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-08-09-'}),
    url(r'txt-08-09-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-08-09-'}),
    url(r'pdf-08-10-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-08-10-'}),
    url(r'txt-08-10-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-08-10-'}),

    url(r'pdf-09-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-09-'}), # C语言数据结构
    url(r'txt-09-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-09-'}),

    url(r'pdf-10-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-01-'}), # uboot和系统移植
    url(r'txt-10-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-01-'}),
    url(r'pdf-10-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-02-'}),
    url(r'txt-10-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-02-'}),
    url(r'pdf-10-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-03-'}),
    url(r'txt-10-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-03-'}),
    url(r'pdf-10-04-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-04-'}),
    url(r'txt-10-04-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-04-'}),
    url(r'pdf-10-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-05-'}),
    url(r'txt-10-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-05-'}),
    url(r'pdf-10-06-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-06-'}),
    url(r'txt-10-06-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-06-'}),
    url(r'pdf-10-07-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-07-'}),
    url(r'txt-10-07-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-07-'}),
    url(r'pdf-10-08-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-08-'}),
    url(r'txt-10-08-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-08-'}),
    url(r'pdf-10-09-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-09-'}),
    url(r'txt-10-09-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-09-'}),
    url(r'pdf-10-10-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-10-'}),
    url(r'txt-10-10-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-10-'}),
    url(r'pdf-10-11-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-11-'}),
    url(r'txt-10-11-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-11-'}),
    url(r'pdf-10-12-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-12-'}),
    url(r'txt-10-12-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-12-'}),
    url(r'pdf-10-13-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-13-'}),
    url(r'txt-10-13-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-13-'}),
    url(r'pdf-10-14-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-14-'}),
    url(r'txt-10-14-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-14-'}),
    url(r'pdf-10-15-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-15-'}),
    url(r'txt-10-15-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-15-'}),
    url(r'pdf-10-16-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-16-'}),
    url(r'txt-10-16-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-16-'}),
    url(r'pdf-10-17-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-17-'}),
    url(r'txt-10-17-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-17-'}),
    url(r'pdf-10-18-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-18-'}),
    url(r'txt-10-18-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-18-'}),
    url(r'pdf-10-19-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-19-'}),
    url(r'txt-10-19-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-19-'}),
    url(r'pdf-10-20-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-10-20-'}),
    url(r'txt-10-20-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-10-20-'}),
    	
    url(r'pdf-11-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-11-01-'}), # linux应用编程和网络编程
    url(r'txt-11-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-11-01-'}),
    url(r'pdf-11-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-11-02-'}),
    url(r'txt-11-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-11-02-'}),
    url(r'pdf-11-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-11-03-'}),
    url(r'txt-11-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-11-03-'}),
    url(r'pdf-11-04-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-11-04-'}),
    url(r'txt-11-04-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-11-04-'}),
    url(r'pdf-11-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-11-05-'}),
    url(r'txt-11-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-11-05-'}),
    url(r'pdf-11-06-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-11-06-'}),
    url(r'txt-11-06-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-11-06-'}),
    url(r'pdf-11-07-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-11-07-'}),
    url(r'txt-11-07-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-11-07-'}),
    url(r'pdf-11-08-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-11-08-'}),
    url(r'txt-11-08-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-11-08-'}),
    url(r'pdf-11-09-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-11-09-'}),
    url(r'txt-11-09-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-11-09-'}),

    url(r'pdf-12-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-12-01-'}), # linux驱动
    url(r'txt-12-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-12-01-'}),
    url(r'pdf-12-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-12-02-'}),
    url(r'txt-12-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-12-02-'}),
    url(r'pdf-12-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-12-03-'}),
    url(r'txt-12-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-12-03-'}),
    url(r'pdf-12-04-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-12-04-'}),
    url(r'txt-12-04-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-12-04-'}),
    url(r'pdf-12-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-12-05-'}),
    url(r'txt-12-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-12-05-'}),
    url(r'pdf-12-06-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-12-06-'}),
    url(r'txt-12-06-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-12-06-'}),
    url(r'pdf-12-07-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-12-07-'}),
    url(r'txt-12-07-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-12-07-'}),
    url(r'pdf-12-08-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-12-08-'}),
    url(r'txt-12-08-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-12-08-'}),
    url(r'pdf-12-09-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-12-09-'}),
    url(r'txt-12-09-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-12-09-'}),
    url(r'pdf-12-10-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-12-10-'}),
    url(r'txt-12-10-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-12-10-'}),
    url(r'pdf-12-11-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-12-11-'}),
    url(r'txt-12-11-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-12-11-'}),

    url(r'pdf-13-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-13-'}), # 图片解码播放器
    url(r'txt-13-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-13-'}),

    url(r'pdf-14-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-14-01-'}), # python基础及应用编程
    url(r'txt-14-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-14-01-'}),
    url(r'pdf-14-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-14-02-'}),
    url(r'txt-14-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-14-02-'}),
    url(r'pdf-14-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-14-03-'}),
    url(r'txt-14-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-14-03-'}),
    url(r'pdf-14-04-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-14-04-'}),
    url(r'txt-14-04-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-14-04-'}),
    url(r'pdf-14-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-14-05-'}),
    url(r'txt-14-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-14-05-'}),
    url(r'pdf-14-06-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-14-06-'}),
    url(r'txt-14-06-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-14-06-'}),
    url(r'pdf-14-07-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-14-07-'}),
    url(r'txt-14-07-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-14-07-'}),
    url(r'pdf-14-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-14-01-'}),
    url(r'txt-14-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-14-01-'}),

    url(r'pdf-15-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-15-01-'}), # WEB开发
    url(r'txt-15-01-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-15-01-'}),
    url(r'pdf-15-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-15-02-'}),
    url(r'txt-15-02-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-15-02-'}),
    url(r'pdf-15-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-15-03-'}),
    url(r'txt-15-03-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-15-03-'}),
    url(r'pdf-15-04-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-15-04-'}),
    url(r'txt-15-04-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-15-04-'}),
    url(r'pdf-15-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-15-05-'}),
    url(r'txt-15-05-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-15-05-'}),

    url(r'pdf-16-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-16-'}),  # C++核心编程
    url(r'txt-16-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-16-'}),

    url(r'pdf-17-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'pdf-17-'}),  # Qt基础
    url(r'txt-17-(?P<nid>\d+)/$', views.displayContent, {'urlToView': 'txt-17-'}),

]
