# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from  django.shortcuts import render
from  django.views.generic import TemplateView
from .forms import CommentForm
from django.conf import  settings
from models import Comment


class CommentShowMinix(object):
    def get_comments(self):
        target = self.request.path
        comments = Comment.objects.filter(target=target)

        return comments
    def get_context_data(self,**kwargs):

        kwargs.update({
            'comment_from':CommentForm(),
            'comment_list':self.get_comments(),
        })

        return  super(CommentShowMinix,self).get_context_data(**kwargs)



class CommentView(TemplateView):
    template_name =  settings.THEME + "/comment/result.html"

    def get(self, request, *args, **kwargs):
        return  super(CommentView,self).get(request,*args,**kwargs)


    def get_comments(self):
        target = self.request.path
        comments = Comment.objects.filter(target=target)

        return comments


    def post(self,request,*args,**kwargs):
        comment_form = CommentForm(request.POST)
        print(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            succeed = True
        else:
            succeed = False
        context = {
            'succeed':succeed,
            'form':comment_form,

        }
        return self.render_to_response(context)

