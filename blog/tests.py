# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.db import  connection
from  django.test import TestCase

from  .models import Category

class  TestCategory(TestCase):
    def setUp(self):
        user = User.objects.create_user("zhan",'25164276@qq.com','123456')
        for i in range(10):
            category_name = "cate_%s" %i
            category = Category()
            category.name = category_name
            category.owner = user
            category.save()

            Category.objects.create(name= category_name,owner = user)

    def test_filter(self):
        categories = Category.objects.all()
        print(categories.query)
        categories = categories.filter(status=1)
        print('-----------------')
        print(categories.query)
        print('-----------------')
        print(connection.queries)
        print('-----------------')
        print(categories)

