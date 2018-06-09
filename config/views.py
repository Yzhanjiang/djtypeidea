# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Link
from django.views.generic import ListView
from blog.views import CommonMixin
from django.conf import  settings
from comment.forms import CommentForm

# Create your views here.

class LinkView(CommonMixin,ListView):
    queryset = Link.objects.filter(status=1)
    model = Link
    template_name = settings.THEME + '/config/links.html'
    context_object_name = 'links'
    # paginate_by = 3
    # allow_empty = True

    def get_context_data(self,**kwargs):
        kwargs.update({
            'comment_from':CommentForm(),

        })
        return super(ListView,self).get_context_data(**kwargs)


def links(request):
    pass