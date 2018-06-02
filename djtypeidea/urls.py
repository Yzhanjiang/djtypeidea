#coding:utf8
"""djtypeidea URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from .custom_site import custom_site

from blog.views import post_list,post_detail,index
from blog.views import IndexView,CategoryView,TagView,PostView
from config.views import links
# from  config.views import  links

urlpatterns = [
    #class view
    url(r'^$',IndexView.as_view(),name="index"),
    url(r'^tag/(?P<tag_id>\d+)/$',TagView.as_view(),name="tag"),
    url(r'^category/(?P<category_id>\d+)/', CategoryView.as_view(), name="category"),
    url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name="detail"),

    #func
    # url(r'^$',post_list,name="index"),
    # url(r'^category/(?P<category_id>\d+)/',post_list,name="category"),
    # url(r'^tag/(?P<tag_id>\d+)/$',post_list,name="tag"),
    # url(r'^post/(?P<pk>\d+)/$',post_detail,name="detail"),
    url(r'links/$',links),
    url(r'^admin/', admin.site.urls),
    url(r'^cus_admin/', custom_site.urls),
]
