from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import SmsSerializer,UserRegSerializer
from rest_framework import mixins
from rest_framework import viewsets

from rest_framework.response import Response

from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework import status

from utils.yunpian import YunPian
from MxShop.settings import API_KEY
from random import random,choice
from .models import VerifyCode

User = get_user_model()

class SmsCodeViewset(mixins.CreateModelMixin,viewsets.GenericViewSet):

    """
    发送短信验证码接口
    """
    serializer_class = SmsSerializer
    def generate_code(self):
        """
        生成四位数字的验证码
        :return: 
        """
        seeds = "123456789"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data['mobile']

        code = self.generate_code()

        yun_pian = YunPian(API_KEY)

        sms_status = yun_pian.send_sms(code=code,mobile=mobile)

        if sms_status["code"] != 0:

            return Response({"mobile":sms_status["msg"]}, status=status.HTTP_400_BAD_REQUEST)
        else:

            code_record = VerifyCode(code=code,mobile=mobile)
            code_record.save()

            return Response({"mobile":mobile},status=status.HTTP_201_CREATED)

        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class UserViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):

    """
    用户注册
    """

    serializer_class = UserRegSerializer
    queryset = User.objects.all()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()



