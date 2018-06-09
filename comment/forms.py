#!/usr/bin/env python 
#coding:utf8

from django import  forms
from .models import Comment

class CommentForm(forms.ModelForm):
    # target = forms.CharField(max_length=100,widget=forms.widgets.HiddenInput)

    nickname = forms.CharField(
        label='昵称',
        max_length=50,
        widget = forms.widgets.Input(
            attrs={'class':'form-control','style':"width:60%"}
        )
    )

    email = forms.CharField(
        label='Email',
        max_length=50,
        widget=forms.widgets.Input(
            attrs={'class': 'form-control','style':"width:60%"}
        )
    )
    website = forms.CharField(
        label='网站',
        max_length=100,
        widget=forms.widgets.URLInput(
            attrs={'class': 'form-control','style':"width:60%"}
        )
    )


    content = forms.CharField(
        label="内容",
        max_length=500,
        widget=forms.widgets.Textarea(attrs={'row':6,'clos':60,'class':'form-control','style':"width:60%"})
    )
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) <10:
            raise  forms.ValidationError("长度太短。。。。")
        return content

    class Meta:
        model = Comment
        fields = ['target','nickname','email','website','content']