from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from .serializers import UserFavSerializer
from .models import UserFav

# Create your views here.



class UserFavViewset(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):

    """
    用户收藏功能接口
    """
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer


