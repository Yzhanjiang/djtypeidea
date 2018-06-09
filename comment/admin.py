# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from  .models import Comment
from djtypeidea.custom_site import custom_site
from djtypeidea.custom_admin import BaseOwnerAdmin

# Register your models here.

@admin.register(Comment, site=custom_site)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ( 'content', 'nickname','email')
    # list_display = ('target', 'content', 'nickname','website','email','status','created_time')

admin.site.register(Comment,CommentAdmin)



