#!/usr/bin/env python 
#coding:utf8

from django.contrib.admin.sites import  AdminSite


class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea 管理后台'
    index_title =  '首页'

custom_site = CustomSite(name='cus_admin')