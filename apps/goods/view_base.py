# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from django.views.generic.base import View
from goods.models import Goods
from django.http import HttpResponse,JsonResponse
import json

class GoodsListView(View):
    def get(self,request):

        json_list = []
        goods = Goods.objects.all()[:10]

        for good in goods:

            json_dict = {}

            json_dict['name'] = good.name
            json_dict['category'] = good.category.name
            json_dict['market_price'] = good.market_price
            json_list.append(json_dict)

        return HttpResponse(json.dumps(json_list),content_type='application/json')




