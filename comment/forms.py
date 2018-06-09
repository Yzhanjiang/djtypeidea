#!/usr/bin/env python 
#coding:utf8

from django import  forms
from .models import Comment

class CommentForm(forms.ModelForm):
    # target = forms.CharField(max_length=100,widget=forms.widgets.HiddenInput)
    content = forms.CharField(
        label="内容",
        max_length=500,
        widget=forms.widgets.Textarea(attrs={'row':6,'clos':80})
    )
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) <10:
            raise  forms.ValidationError("长度太短。。。。")
        return content

    class Meta:
        model = Comment
        fields = ['nickname','email','website','content']