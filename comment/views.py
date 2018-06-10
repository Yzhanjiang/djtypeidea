# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from  django.shortcuts import render,redirect
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
    http_method_names = ['POST']
    template_name =  settings.THEME + "/comment/result.html"

    def get(self, request, *args, **kwargs):
        return  super(CommentView,self).get(request,*args,**kwargs)


    def get_comments(self):
        target = self.request.path
        comments = Comment.objects.filter(target=target)

        return comments


    def post(self,request,*args,**kwargs):
        comment_form = CommentForm(request.POST)
        target = request.POST.get('target')
        print(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.target = target
            instance.save()

            succeed = True
            return redirect(target)
        else:
            succeed = False
        context = {
            'succeed':succeed,
            'form':comment_form,
            'target':target,

        }
        return self.render_to_response(context)

