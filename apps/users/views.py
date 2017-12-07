from django.contrib.auth import get_user_model
from random import choice
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from chartsite.settings import YUN_KEY
from apps.users.models import PhoneCode, EmailCode, ImageCode
from users.serializers import PhoneSerialier, UserRegSerializer, UserDetailSerializer, EmailSerialier

from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import authentication

from utils.code import SmsEmailCode, ImgEmailCode
from utils.code import SmsPhoneCode
from rest_framework.mixins import CreateModelMixin


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
User = get_user_model()


class CustomBBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class PhoneCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送手机验证码
    """
    serializer_class = PhoneSerialier

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = '1234567890'
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # drf可以捕做捉异常返回400
        code = self.generate_code()

        mobile = serializer.validated_data['mobile']

        yun_pian = SmsPhoneCode(YUN_KEY)

        sms_status = yun_pian.send_msg(code=code, mobile=mobile)
        if sms_status['code'] != 0:
            return Response({
                "mobile": sms_status['msg']
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = PhoneCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                'mobile': mobile
            }, status=status.HTTP_201_CREATED)


class EmailCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送邮箱验证码
    """
    serializer_class = EmailSerialier

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = '1234567890'
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # drf可以捕做捉异常返回400
        code = self.generate_code()

        email = serializer.validated_data['email']

        sms_status = SmsEmailCode(code=code, email=email)
        if sms_status['code'] != 0:
            return Response({
                "email": sms_status['msg']
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = EmailCode(code=code, email=email)
            code_record.save()
            return Response({
                'email': email
            }, status=status.HTTP_201_CREATED)


class ImageCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送图片验证码
    """

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = '1234567890'
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # drf可以捕做捉异常返回400
        code = self.generate_code()
        print(request.data)
        index = request.data['index']

        img_code = ImgEmailCode(code=code)
        code, image_path, image = img_code.made_code_img()

        sms_status = ImageCode(code=code, index=index, image='/chartsite/captcha/{}'.format(image)).save()
        if sms_status:
            with open(image_path, 'rb') as f:
                ret = f.read()
            return Response(data=ret, content_type='',status=status.HTTP_201_CREATED)





class UserViewset(CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    # permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (authentication.SessionAuthentication, JSONWebTokenAuthentication)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated(), ]
        elif self.action == 'create':
            return []
        return []

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        elif self.action == 'create':
            return UserRegSerializer

        return UserDetailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(payload)
        re_dict['name'] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    # 重载获取用户model的实例
    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()






@api_view(['GET', 'POST'])
def UserAccess(request, type):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        rep = render(request, 'index.html')
        if type == 'login':
            rep = render(request, 'user/login.html')
        elif type == 'register':
            rep = render(request, 'user/register.html')
        return rep
