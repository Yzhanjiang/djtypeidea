# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

from config.models import Post,Tag,Category
from config.models import SideBar
from  comment.models import  Comment

from django.http import  Http404

from django.core.paginator import Paginator,EmptyPage

def get_common_context():
    categories = Category.objects.filter(status=1)
    nav_cates = []
    cates = []
    for cate in categories:
        if cate.is_nav:
            nav_cates.append(cate)
        else:
            cates.append(cate)

    side_bars = SideBar.objects.filter(status=1)

    recently_posts = Post.objects.filter(status=1)[:10]
    # hot_posts = Post.objects.filter(status=1).order_by('views')[:10]
    recently_comments = Comment.objects.filter(status=1)[:10]

    context = {
        'nav_cates': nav_cates,
        'cates': cates,
        'side_bars': side_bars,
        'recently_posts': recently_posts,
        'recently_comments': recently_comments,
    }
    return  context


def index(request):
    pass













def post_list(request,category_id=None,tag_id=None):
    queryset = Post.objects.all()

    page = request.GET.get('page',1)
    page_size = 1
    try:
        page = int(page)
    except TypeError:
        page = 1
    if category_id :
        #分类页面
        queryset = queryset.filter(category_id=category_id)
    elif tag_id:
        #标签页面
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            queryset = []
        else:
            queryset = tag.posts.all()

    else:
        queryset = Post.objects.all()
    paginator = Paginator(queryset, page_size)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # categories = Category.objects.filter(status=1)
    # nav_cates = []
    # cates = []
    # for cate in categories:
    #     if cate.is_nav:
    #         nav_cates.append(cate)
    #     else:
    #         cates.append(cate)
    #
    # side_bars = SideBar.objects.filter(status = 1)
    #
    # recently_posts = Post.objects.filter(status=1)[:10]
    # # hot_posts = Post.objects.filter(status=1).order_by('views')[:10]
    # recently_comments = Comment.objects.filter(status=1)[:10]

    context = {
        'posts': posts,
        # 'nav_cates':nav_cates,
        # 'cates':cates,
        # 'side_bars':side_bars,
        # 'recently_posts':recently_posts,
        # 'recently_comments':recently_comments,
    }
    common_context = get_common_context()
    context.update(common_context)

    return  render(request,'blog/list.html',context=context)


def post_detail(request,pk=None):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise  Http404("post does not exist")

    categories = Category.objects.filter(status=1)
    nav_cates = []
    cates = []
    for cate in categories:
        if cate.is_nav:
            nav_cates.append(cate)
        else:
            cates.append(cate)

    side_bars = SideBar.objects.filter(status=1)

    recently_posts = Post.objects.filter(status=1)[:10]
    # hot_posts = Post.objects.filter(status=1).order_by('views')[:10]
    recently_comments = Comment.objects.filter(status=1)[:10]

    context = {
        'post': post,
        # 'nav_cates': nav_cates,
        # 'cates': cates,
        # 'side_bars': side_bars,
        # 'recently_posts': recently_posts,
        # 'recently_comments': recently_comments,
    }
    common_context = get_common_context()
    context.update(common_context)


    return render(request,'blog/detail.html',context=context)