# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
# Register your models here.

from  .models import Post,Category,Tag
from djtypeidea.custom_site import custom_site
from  .adminforms import PostAdminForm
from djtypeidea.custom_admin import BaseOwnerAdmin


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm

    list_display = [
        'title','category','status','content','owner',
        'create_time','operator'
        ]
    list_filter = ['title','owner']

    fields = (
            ('category', 'title'),
            'content',
            'status',
            'tags',
    )
    search_fields = ['title','category__name']
    save_on_top = True


    # list_display_links = ['category','status']

    # show_full_result_count = False
    # date_hierarchy = 'create_time'
    # list_editable = ('title',)

    # fields = (
    #     ('category','title'),
    #     'content'
    # )
    # exclude = 'owner'
    # fieldsets = (# 跟fields互斥
    #     ('基础配置',{
    #         'fields':(('category','title'),'content','status')
    #              }),
    #     ('高级配置',{
    #         'classes':('collapse','addon'),
    #         'fields':('tags',),
    #     }),
    #     )
    # filter_horizontal = ('tags',)


    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            # '/cus_admin/blog/post/%s/' %obj.id
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.allow_tags = True
    operator.short_description = '操作'


# class PostInlineAdmin(admin.TabularInline):  # StackedInline  样式不同
#     fields = ('title', 'desc','owner')
#     extra = 3  # 控制额外多几个
#     model = Post

@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = (
        'name', 'status',
        'is_nav',
    )


    # inlines = [
    #     PostInlineAdmin,
    # ]



@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'create_time')
    fields = (
        'name', 'status'
    )

# admin.site.register(Post,PostAdmin)
# admin.site.register(Category,CategoryAdmin)
# admin.site.register(Tag,TagAdmin)

