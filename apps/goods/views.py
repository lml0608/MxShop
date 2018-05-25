from .models import Goods,GoodsCategory
from .serializer import GoodsSerializer,CategorySerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend

from .filters import GoodsFilter
from rest_framework import filters

# Create your views here.
# class GoodsListView(APIView):
#class GoodsListView(mixins.ListModelMixin,generics.GenericAPIView):

#http://127.0.0.1:8000/goods/?p=2&page_size=20
class StandarResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100

class GoodsListViewset(mixins.ListModelMixin,viewsets.GenericViewSet):


    """
    商品列表页  分页，搜索，。过滤，排序
    """


    queryset = Goods.objects.all()

    serializer_class = GoodsSerializer

    pagination_class = StandarResultsSetPagination
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)

    filter_class = GoodsFilter
    search_fields = ('name','goods_brief','goods_desc')

    ordering_fields = ('sold_num','shop_price')
    #search_fields = ('@name','goods_brief','goods_desc')
    #  =,^,@,$

    #filter_fields = ('name','shop_price')


class CategoryViewset(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    list:
        商品分类列表
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer



