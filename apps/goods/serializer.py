from rest_framework import serializers
from .models import Goods,GoodsCategory,GoodsImage

class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ["image",]

class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):

    #使用ModelSerializer

    category = CategorySerializer()
    images = GoodsImageSerializer(many=True)

    class Meta:

        model = Goods
        #fields = ('name','click_num','market_price','add_time')

        fields = "__all__"

    # name = serializers.CharField(required=True,max_length=100)
    # click_num = serializers.IntegerField(default=0)
    # goods_front_image = serializers.ImageField()

#
# class GoodCategorySerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = GoodsCategory
#         fields = "__all__"





