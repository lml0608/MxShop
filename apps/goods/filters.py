# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import django_filters
from .models import Goods,GoodsCategory
from django.db.models import Q

class GoodsFilter(django_filters.rest_framework.FilterSet):

    pricemin = django_filters.NumberFilter(name='shop_price',lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
    #contains 包含 i 忽略大小写
    #name = django_filters.CharFilter(name='name',lookup_expr='icontains')

    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self,queryset, name, value):

        return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))

    class Meta:

        model = Goods
        fields = ['pricemin','pricemax','is_hot']
