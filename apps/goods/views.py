from .models import Goods
from .serializer import GoodsSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class GoodsListView(APIView):

    def get(self,request,format=None):
        goods = Goods.objects.all()[0:10]

        goods_serializer = GoodsSerializer(goods,many=True)

        return Response(goods_serializer.data)
