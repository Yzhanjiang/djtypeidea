# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
# Create your tests here.
from django.contrib.auth.models import User
from django.db import  connection
from  django.test import TestCase

from django.test.utils import override_settings

from  .models import Category

class  TestCategory(TestCase):
    @override_settings(DEBUG=True)
    def setUp(self):
        user = User.objects.create_user("zhan",'25164276@qq.com','123456')
        Category.objects.bulk_create([
            Category(name='cate_bulk_%s' %i,owner=user)
            for i in range(10)
        ])


    # @override_settings(DEBUG=True)
    # def test_filter(self):
    #     queryset = Category.objects.filter(status=1)
    #
    #     print(type(queryset))
    #     categories = queryset
    #     print(categories)
    #     for cate in categories:
    #         print(cate.created_time)
    #         print(cate.name)
    #     print(connection.queries)
        # categories = categories.filter(status=1)
        # print(list(categories))
        # print('-----------------')
        # print(categories.query)
        # print('-----------------')
        # print(connection.queries)
        # print('-----------------')
        # print(categories)

    def test_values(self):
        categories = Category.objects.values('name')
        print(categories)
        categories = Category.objects.values_list('id','name')
        print(categories)

