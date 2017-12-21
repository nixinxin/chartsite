#!/usr/bin/python
# _*_ encoding:utf-8 _*_
from django.contrib.auth import get_user_model

__author__ = "xin nix"

from django import forms

User = get_user_model()

from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'gender', 'birthday', 'desc', 'mobile', 'work', 'city', 'unit']


class CaptchaForm(forms.Form):
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})
