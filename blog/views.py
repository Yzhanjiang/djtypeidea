# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

from .models import Post,Tag,Category
from django.http import  Http404

from django.core.paginator import Paginator,EmptyPage



def post_list(request,category_id=None,tag_id=None):
    queryset = Post.objects.all()

    page = request.GET.get('page',1)
    page_size = 1
    try:
        page = int(page)
    except TypeError:
        page = 1
    if category_id :
        queryset = queryset.filter(category_id=category_id)

    elif tag_id:
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

    context = {
        'posts': posts,
    }
    return  render(request,'blog/list.html',context=context)


def post_detail(request,pk=None):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise  Http404("post does not exist")

    context = {
        'post': post,
    }
    return render(request,'blog/detail.html',context=context)