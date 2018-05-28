"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
# from django.contrib import admin
import xadmin

from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls


from goods.views import GoodsListViewset,CategoryViewset
from users.views import SmsCodeViewset,UserViewSet
from user_operation.views import UserFavViewset
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token


router = DefaultRouter()

#配置goods的URL
router.register(r'goods',GoodsListViewset,base_name="goods")
router.register(r'categorys',CategoryViewset,base_name="categorys")
router.register(r'codes',SmsCodeViewset,base_name="codes")
router.register(r'users',UserViewSet,base_name="users")
router.register(r'userfavs',UserFavViewset,base_name="userfavs")

# goods_list = GoodsListViewset.as_view(
#     {
#         'get':'list',
#         #'post': 'create'
#     }
# )

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),


    #商品列表页

    #url(r'goods/$',goods_list,name='goods-list'),
    url(r'^',include(router.urls)),

    url(r'docs/',include_docs_urls(title='暮学生鲜')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api-token-auth/',views.obtain_auth_token),
    url(r'^jwt-auth/', obtain_jwt_token),
    #url(r'^api-token-auth/', obtain_jwt_token),
]

#云片网key
#c2f1d12148612fdd17ba394a007b01bc