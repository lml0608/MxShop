from rest_framework import serializers
from .models import Goods,GoodsCategory

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):

    #使用ModelSerializer

    category = CategorySerializer()

    class Meta:

        model = Goods
        #fields = ('name','click_num','market_price','add_time')

        fields = "__all__"

    # name = serializers.CharField(required=True,max_length=100)
    # click_num = serializers.IntegerField(default=0)
    # goods_front_image = serializers.ImageField()


