# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from  .models import Link,SideBar
from djtypeidea.custom_site import custom_site
from djtypeidea.custom_admin import BaseOwnerAdmin

# Register your models here.

@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status','weight','owner','created_time')
    # fields = (
    #     'name', 'status'
    # )
admin.site.register(Link,LinkAdmin)

@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'status','content','owner','created_time')
    # fields = (
    #     'name', 'status'
    # )
admin.site.register(SideBar,SideBarAdmin)

