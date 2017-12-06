#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "xin nix"
import requests
import json


class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_msg(self, code, mobile):
        parmas = {
            'apikey': self.api_key,
            "mobile": mobile,
            "text": "【农业统计数据】您的验证码是{}".format(code)
        }
        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict



