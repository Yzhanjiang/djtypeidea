# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
# Register your models here.

from  .models import Post,Category,Tag
from djtypeidea.custom_site import custom_site

@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title','category','status','content','owner',
        'create_time','operator'
        ]
    list_filter = ['title','owner']
    # list_display_links = ['category','status']
    search_fields = ['title','category__name']
    save_on_top = True
    show_full_result_count = False
    date_hierarchy = 'create_time'
    # list_editable = ('title',)

    # fields = (
    #     ('category','title'),
    #     'content'
    # )
    # exclude = 'owner'
    fieldsets = (# 跟fields互斥
        ('基础配置',{
            'fields':(('category','title'),'content')
                 }),
        ('高级配置',{
            'classes':('collapse','addon'),
            'fields':('tags',),
        }),
        )
    filter_horizontal = ('tags',)


    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            # '/cus_admin/blog/post/%s/' %obj.id
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.allow_tags = True
    operator.short_description = '操作'

@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Post,PostAdmin)
# admin.site.register(Category,CategoryAdmin)
# admin.site.register(Tag,TagAdmin)

