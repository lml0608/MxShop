from .models import Goods
from .serializer import GoodsSerializer

# from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

from rest_framework.pagination import PageNumberPagination


from rest_framework import viewsets


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
    商品列表页
    """

    queryset = Goods.objects.all()

    serializer_class = GoodsSerializer

    pagination_class = StandarResultsSetPagination

    #
    #
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    # #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    # def get(self,request,format=None):
    #     goods = Goods.objects.all()[0:10]
    #
    #     goods_serializer = GoodsSerializer(goods,many=True)
    #
    #     return Response(goods_serializer.data)
    #
    # def post(self,request,format=None):
    #
    #     serializer = GoodsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

