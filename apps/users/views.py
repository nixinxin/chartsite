import os
from datetime import datetime, timedelta
from captcha.models import CaptchaStore
from django.contrib.auth import get_user_model, authenticate, login
from random import choice, Random
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q, QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from chartsite.settings import YUN_KEY
from apps.users.models import PhoneCode, EmailCode, ImageCode, UserProfile
from operation.models import UserMessage
from users.forms import RegisterForm, LoginForm, CaptchaForm
from users.serializers import PhoneSerialier, UserRegSerializer, UserDetailSerializer, EmailSerialier, \
    ImageCodeSerialier, ImageCodeVerifySerialier, EmailVerifySerialier, UserExitSerialier

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
from utils.code import send_email
User = get_user_model()


class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
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


class EmailCodeViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    发送邮箱验证码
    """

    def get_queryset(self):
        queryset = ''
        if self.action == 'retrieve':
            queryset = User.objects.all()
        elif self.action == 'create':
            queryset = EmailCode.objects.all()
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        return queryset

    def generate_code(self, ranglength=4):
        str = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(ranglength):
            str += chars[random.randint(0, length)]
        return str

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserExitSerialier
        elif self.action == 'create':
            return EmailSerialier
        elif self.action == 'list':
            return EmailVerifySerialier
        return EmailSerialier

    # 验证邮箱是否存在
    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        return Response(email, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # drf可以捕做捉异常返回400
        send_type = serializer.validated_data['send_type']
        email = serializer.validated_data['email']
        if send_type == 'activate':
            code = self.generate_code(16)
        else:
            code = self.generate_code(4)
        sms_status = send_email(code=code.lower(), email=email, send_type=send_type)
        if not sms_status:
            return Response({
                "msg": '邮件发送失败，请重新发送！'
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = EmailCode(code=code.lower(), email=email, send_type=send_type)
            code_record.save()
            return Response({
                'msg': '邮件发送成功，请注意查收！'
            }, status=status.HTTP_201_CREATED)

    # 验证邮箱验证码是否正确 get
    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        response = Response(email, status=status.HTTP_200_OK)
        if email:
            if serializer.validated_data['send_type'] == 'register':

                response = Response(True, status=status.HTTP_200_OK)

            elif serializer.validated_data['send_type'] == 'forget':

                user = User.objects.get(Q(username=email) | Q(email=email))
                payload = jwt_payload_handler(user)
                re_dict = serializer.data
                re_dict['token'] = jwt_encode_handler(payload)
                headers = self.get_success_headers(re_dict)
                headers['Authorization'] = "token " + re_dict['token']
                response = Response(True, status=status.HTTP_200_OK, headers=headers)
                expires = datetime.now() + timedelta(days=1)
                response.set_cookie('token', re_dict['token'], expires=expires)

        return response


class EmailCodeVereifyViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    发送邮箱验证码
    """
    serializer_class = EmailVerifySerialier

    queryset = EmailCode.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        code = serializer.validated_data['verify']
        send_type = serializer.validated_data['send_type']
        data = False
        statuscode = status.HTTP_200_OK
        exit = EmailCode.objects.filter(code=str(code).lower(), email=email, send_type=send_type)
        if exit:
            data = True
        return Response(data, status=statuscode)


class ImageCodeViewset(mixins.ListModelMixin,  mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    发送图片验证码
    """
    serializer_class = ImageCodeSerialier

    def get_queryset(self):
        code = self.generate_code()
        Image = ImgEmailCode(code=code)
        img_path, image = Image.made_code_img()
        image = os.path.join('chartsite', 'captcha', image)
        ImageCode.objects.create(code=code, image=image)
        with open(img_path, 'rb') as f:
            ret = f.read()
        return ret

    def list(self, request, *args, **kwargs):
        parses = request.query_params
        header = {
            "status": status.HTTP_200_OK,
            'content_type': "text/plain"
        }
        if parses:
            parses = dict(parses)
            result = ImageCode.objects.get(code=dict(parses.keys())[0]).exists()
            if result:
                data = "OK"
            else:
                data = "Not Found"
                header['status'] = status.HTTP_404_NOT_FOUND
        else:
            data = self.get_queryset()
            header['content_type'] = "image/png"
        return HttpResponse(content=data, **header)

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


class ImageCodeVerifyViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    验证图片验证码
    """
    serializer_class = ImageCodeVerifySerialier
    queryset = EmailCode.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = serializer.validated_data['response']
        hashkey = serializer.validated_data['hashkey']
        data = False
        statuscode = status.HTTP_200_OK
        exit = CaptchaStore.objects.filter(response=str(response).lower(), hashkey=hashkey)
        if exit:
            data = True
        return Response(data, status=statuscode)


class UserViewset(CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    # serializer_class = UserRegSerializer
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
        headers = self.get_success_headers(re_dict)
        headers['Authorization'] = "token " + re_dict['token']
        response = Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)
        return response



    # 重载获取用户model的实例
    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "user/register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "user/register.html", {"register_form": register_form, "msg": "用户已经存在"})
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            # 写入欢迎注册消息
            user_message = UserMessage()
            user_message.user = user_profile.id
            user_message.message = "欢迎注册农业统计数据可视化平台"
            user_message.save()

            send_email(user_name, "register")
            return render(request, "user/login.html")
        else:
            return render(request, "user/register.html", {"register_form": register_form})


class LoginView(View):
    def get(self, request):
        login_form = RegisterForm()
        return render(request, "user/login.html", {'register_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("email", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, "user/login.html", {"msg": "用户未激活！"})
            else:
                return render(request, "user/login.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request, "user/login.html", {"login_form": login_form})


class PersonalViewset(View):
    def get(self, request):
        return render(request, "user/personal.html")


class ForgetView(View):
    def get(self, request):
        return render(request, "user/forgetpwd.html")


class AccountView(View):
    def get(self, request):
        return render(request, "user/account.html")


class ServiceView(View):
    def get(self, request):
        return render(request, "service.html")


class ShareView(View):

    def get(self, request):
        return render(request, "share.html")


class FaviconView(View):

    def get(self, request):
        favicon = open(os.path.join('static', 'img', 'favicon.ico'), 'rb').read()
        header = {
            'content_type': "image/png"
        }
        data = favicon
        return HttpResponse(content=data, **header)


class InviteView(View):
    def get(self, request):
        return render(request, "invite.html")


class TemplateViews(View):
    def get(self, request):
        return render(request, "test.html")