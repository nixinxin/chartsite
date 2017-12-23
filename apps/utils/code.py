#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "xin nix"
import re
from random import Random
from urllib import request
import requests
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import json
from django.shortcuts import render, HttpResponse
import os
from django.core.mail import send_mail

from chartsite import settings
from chartsite.settings import BASE_DIR, EMAIL_FROM, HOST
from apps.users.models import EmailCode
import smtplib
import random
from email.mime.text import MIMEText
from email.utils import formataddr



# Create your views here.
_letter_cases = "abcdefghjkmnpqrstuvwxy"  # 小写字母，去除可能干扰的i，l，o，z
_upper_cases = _letter_cases.upper()  # 大写字母
_numbers = ''.join(map(str, range(3, 10)))  # 数字
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))
TFF_PATH = os.path.join(BASE_DIR, 'static', 'fonts', 'Monaco.TTF')


class ImgEmailCode(object):
    """
    @todo: 生成验证码图片
    @param size: 图片的大小，格式（宽，高），默认为(120, 30)
    @param chars: 允许的字符集合，格式字符串
    @param img_type: 图片保存的格式，默认为GIF，可选的为GIF，JPEG，TIFF，PNG
    @param mode: 图片模式，默认为RGB
    @param bg_color: 背景颜色，默认为白色
    @param fg_color: 前景色，验证码字符颜色，默认为蓝色#0000FF
    @param font_size: 验证码字体大小
    @param font_type: 验证码字体，默认为 ae_AlArabiya.ttf
    @param length: 验证码字符个数
    @param draw_lines: 是否划干扰线
    @param n_lines: 干扰线的条数范围，格式元组，默认为(data, 2)，只有draw_lines为True时有效
    @param draw_points: 是否画干扰点
    @param point_chance: 干扰点出现的概率，大小范围[0, 100]
    @return: [0]: PIL Image实例
    @return: [data]: 验证码图片中的字符串
    """
    def __init__(self,
                 size=(120, 38),
                 chars=init_chars,
                 img_type="GIF",
                 mode="RGB",
                 bg_color=(255, 255, 255),
                 fg_color=(0, 0, 255),
                 font_size=18,
                 font_type=TFF_PATH,
                 length=4,
                 draw_lines=True,
                 n_line=(1, 2),
                 draw_points=True,
                 point_chance=2,
                 code='1234'):
        self.size = size,
        self.chars = chars,
        self.img_type = img_type,
        self.mode = mode,
        self.bg_color = bg_color,
        self.fg_color = fg_color,
        self.font_size = font_size,
        self.font_type = font_type,
        self.length = length,
        self.draw_lines = draw_lines,
        self.n_line = n_line,
        self.draw_points = draw_points,
        self.point_chance = point_chance
        self.width, self.height = size  # 宽， 高
        self.img = Image.new(mode, size, bg_color)  # 创建图形
        self.draw = ImageDraw.Draw(self.img)  # 创建画笔
        self.code = code

    def code_to_img(self, code):
        font = ImageFont.truetype(self.font_type[0], self.font_size[0])
        font_width, font_height = font.getsize(code)
        xy = ((self.width - font_width) / 3, (self.height - font_height) / 3)
        self.draw.text(xy, code, font=font, fill=self.fg_color[0])

    def create_lines(self):
        """绘制干扰线"""
        line_long = random.randint(*self.n_line[0])  # 干扰线条数

        for i in range(line_long):
            # 起始点
            begin = (random.randint(0, self.width), random.randint(0, self.height))
            # 结束点
            end = (random.randint(0, self.width), random.randint(0, self.height))
            self.draw.line([begin, end], fill=(0, 0, 0))

    def create_points(self):
        """绘制干扰点"""
        chance = min(100, max(0, int(self.point_chance)))  # 大小限制在[0, 100]

        for w in range(self.width):
            for h in range(self.height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    self.draw.point((w, h), fill=(0, 0, 0))

    def lines_points(self):
        if self.draw_lines:
            self.create_lines()
        if self.draw_points:
            self.create_points()

    def distort(self):
        # 图形扭曲参数
        params = [1 - float(random.randint(1, 2)) / 100,
                  0,
                  0,
                  0,
                  1 - float(random.randint(1, 10)) / 100,
                  float(random.randint(1, 2)) / 500,
                  0.001,
                  float(random.randint(1, 2)) / 500
                  ]
        self.img = self.img.transform(self.size[0], Image.PERSPECTIVE, params)  # 创建扭曲
        self.img = self.img.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强（阈值更大）
        return self.img

    def made_code_img(self):
        self.code_to_img(self.code)
        self.lines_points()
        self.distort()
        image = self.code + '.png'
        img_path = os.path.join(BASE_DIR, 'media', 'chartsite', 'captcha', image)
        self.img.save(img_path)
        return img_path, image


def str_tool(length):
    """生成给定长度的字符串，返回列表格式"""
    # 定义一个空字符串
    code = ""
    # 构建循环，每循环一次，往temp中加一个字符,循环次数相当于随机码位数
    for i in range(length):
        # 随机码由数字和字符构成，定义随机数字和字符,数字范围：0,9
        a = random.randrange(65, 91)
        b = random.randrange(10)
        # 随机构建数字和字符出现的位数,定义一个随机数字范围，如果这个数在0-5以内，则temp添加数字，否则添加字符
        c = random.randrange(length * 2)
        if c in range(length):
            code += str(b)
        else:
            code += str(chr(a))
    return code


def SmsEmailCode(code, email):
    # 第三方 SMTP 服务
    data = {'code': 1, 'msg': ''}
    my_sender = '1025464043@qq.com'  # 发件人邮箱账号
    my_pass = 'ehtcmrqluckmbgab'  # 发件人邮箱密码
    receivers = [email, ]  # 收件人邮箱账号，我这边发送给自己
    code = "【农业统计数据】您的验证码是：{}".format(code)
    try:
        msg = MIMEText(code, 'html', 'utf-8')
        msg['From'] = formataddr(["何言", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["", receivers[0]])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "验证码"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, receivers, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        data['code'] = 0
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        data['code'] = 1
        data['msg'] = e
    return data


def get_email_code(request):
    data = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        ip = request.META['REMOTE_ADDR']
        try:
            code = SmsEmailCode(code=str_tool(4), email=email)
            result = EmailCode.objects.filter(code=code, ip=ip, code_type=1).exists()
            if not result:
                EmailCode.objects.create(code=code, ip=ip, code_type=1)
        except:
            code = None
        if code:
            data['status'] = 0
            data['msg'] = '请输入验证码'
    return HttpResponse(json.dumps(data))


def check_email_code(request):
    data = {"status": 1, "msg": "验证码错误"}
    if request.method == 'POST':
        code = request.POST.get('code')
        code = code.upper()
        ip = request.META['REMOTE_ADDR']
        store_code = False
        try:
            store_code = EmailCode.objects.filter(code=code, ip=ip, code_type=1).exists()
        except Exception as e:
            print(e)
        if store_code:
            data['status'] = 0
            data['msg'] = ''
    print(data)
    return HttpResponse(json.dumps(data))


def get_code_img(request):
    img_code = ImgEmailCode()
    code, img_path = img_code.made_code_img()
    ip = request.META['REMOTE_ADDR']
    EmailCode.objects.create(code=code, ip=ip, code_type=2)
    data = {}
    if request.method == 'POST':
        img_path = '/'.join((settings.STATIC_URL[:-1], 'captcha', 'imgs', code + '.png'))
        data['status'] = 0
        data['url'] = img_path
        return HttpResponse(json.dumps(data))
    if request.method == 'GET':
        with open(img_path, 'rb') as f:
            ret = f.read()
        return HttpResponse(ret)


def check_img_code(request):
    data = {'status': 1, 'msg': ""}
    if request.method == 'GET':
        code = request.GET.get('code')
        code = code.upper()
        ip = request.META['REMOTE_ADDR']
        try:
            exit = EmailCode.objects.filter(ip=ip, code=code, code_type=2).exists()
            if exit:
                result = EmailCode.objects.filter(ip=ip, code=code, code_type=2).order_by('-time').values().first()['code']
                if code == result:
                    data['msg'] = 'ok'
                    data['status'] = 0
        except Exception as e:
            print(e)
    return HttpResponse(json.dumps(data))


def sendactemail(host, username, emailaddr):
    data = {'status': False, 'msg': ''}
    # 第三方 SMTP 服务
    my_sender = '1025464043@qq.com'  # 发件人邮箱账号
    my_pass = 'ehtcmrqluckmbgab'  # 发件人邮箱密码
    receivers = [emailaddr, ]  # 收件人邮箱账号，我这边发送给自己
    mail_msg = """<table width="500" cellspacing="0" cellpadding="0" border="0" bgcolor="#ffffff" align="center"><tbody>
    <td><table width="500" height="40" cellspacing="0" cellpadding="0" border="0" align="center"></table></td> <tr> <td> 
    <table width="500" height="48" cellspacing="0" cellpadding="0" border="0" bgcolor="#10A64F" backgroud-color='transparent' 
    align="center"> <tbody> <tr> <td border="0" style="padding-left:20px;" width="74" valign="middle" height="26" 
    align="center"> <a href="http://127.0.0.data:8000/user/login" target="_blank">
    <img src="http://www.easyicon.net/api/resizeApi.php?id=1207445&size=48" width="44" height="44" border="0"> </a> </td> 
    <td colspan="2" style="color:#ffffff; padding-right:20px;"width="500" valign="middle" height="48" align="right"> 
    <a href="http://127.0.0.data:8000/user/login" target="_blank" style="color:#ffffff;text-decoration:none;font-size:16px">
    首页</a> </td> </tr> </tbody> 
    </table> </td> </tr> <tr> <td> <table style="border:1px solid #edecec;border-top:none;border-bottom:none;padding:0 
    20px;font-size:14px;color:#333333;" width="500" cellspacing="0" cellpadding="0" border="0" align="left"> <tbody> <tr> 
    <td border="0" colspan="2" style=" font-size:16px;vertical-align:bottom;" width="500" height="56" align="left">尊敬的
    </a>：</td> </tr> <tr> <td border="0" style="padding-left:40px;font-size:12px;"width="360" height="32">欢迎加入农业
    统计数据，请妥善保管您的登录信息：</td> </tr> <tr> <td colspan="2" style="padding-left:40px;font-size:12px;" 
    width="360" height="32">点击进入激活链接，以激活您的账号：<a href="http://127.0.0.data:8000/user/check-active-email" 
    style="text-decoration:none" target="_blank">点此进入</a> </td> </tr><tr><td colspan="2" style="line-height:30px;
    border-bottom:1px  dashed #e5e5e5;font-size:12px;text-align: left;padding-left: 320px;" width="360" height="14">
    农业统计数据</td></tr><tr><td colspan="2" style="padding:8px0 28px;color:#999999; font-size:12px;text-align: right;
    padding-right: 40px;" width="360" height="14">此为系统邮件请勿回复</td></tr></tbody></table></td></tr><td><table 
    width="500" height="40" cellspacing="0" cellpadding="0" border="0" align="center"></table></td></tbody></table>"""
    username = request.quote(username)
    url = "active-email?username={}&email={}".format(username, emailaddr)
    mail_msg = re.sub("active-email", url, mail_msg)
    username = request.unquote(username)
    mail_msg = re.sub("尊敬的", "尊敬的" + username, mail_msg)
    mail_msg = re.sub("127.0.0.data:8000", host, mail_msg)
    try:
        msg = MIMEText(mail_msg, 'html')
        msg['From'] = formataddr(["何言", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["大神", receivers[0]])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "农业统计数据—邮箱激活链接"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, receivers, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        data['status'] = True
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        data['msg'] = e
    return data


class SmsPhoneCode(object):

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





def send_email(email, code, send_type="register"):
    email_record = EmailCode()

    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    data = False
    title = "【农业统计数据】"
    email_body = """<table width="500" cellspacing="0" cellpadding="0" border="0" bgcolor="#ffffff" 
    align="center"><tbody> <td><table width="500" height="40" cellspacing="0" cellpadding="0" border="0" 
    align="center"></table></td> <tr> <td> <table width="500" height="48" cellspacing="0" cellpadding="0" border="0" 
    bgcolor="#10A64F" backgroud-color='transparent' align="center"> <tbody> <tr> <td border="0" 
    style="padding-left:20px;" width="74" valign="middle" height="26" align="center"> <a href="{host}/index" 
    target="_blank"><img src="{host}/static/index/img/chartsite.png" width="176" height="36" border="0"> </a> </td> 
    <td colspan="2" style="color:#ffffff; padding-right:20px;"width="500" valign="middle" height="48" align="right"> 
    <a href="{host}/index" target="_blank" style="color:#ffffff;text-decoration:none;font-size:16px"> 首页</a> </td> 
    </tr> </tbody></table> </td> </tr> <tr> <td> <table style="border:1px solid 
    #edecec;border-top:none;border-bottom:none;padding:0 20px;font-size:14px;color:#333333;" width="500" 
    cellspacing="0" cellpadding="0" border="0" align="left"> <tbody> <tr> <td border="0" colspan="2" style=" 
    font-size:16px;vertical-align:bottom;" width="500" height="56" align="left">尊敬的用户：</a></td> </tr> <tr> <td 
    border="0" style="padding-left:40px;font-size:12px;"width="360" height="32">{email}, 您好</td></tr> <tr> <td 
    border="0" style="padding-left:40px;font-size:12px;"width="360" height="32">欢迎加入农业统计数据，请妥善保管您的验证信息：</td> </tr> 
    <tr> <td colspan="2" style="padding-left:40px;font-size:12px;" width="360" height="32">{notice}<br><a href="{url}" 
    style="text-decoration:none" target="_blank">{url}</a> </td> </tr><tr><td colspan="2" style="line-height:30px; 
    border-bottom:1px  dashed #e5e5e5;font-size:12px;text-align: left;padding-left: 320px;" width="360" height="14"> 
    农业统计数据</td></tr><tr><td colspan="2" style="padding:8px0 28px;color:#999999; font-size:12px;text-align: right; 
    padding-right: 40px;" width="360" height="14">此为系统邮件请勿回复</td></tr></tbody></table></td></tr><td><table 
    width="500" height="40" cellspacing="0" cellpadding="0" border="0" align="center"></table></td></tbody></table> """

    if send_type == "register":
        email_title = "邮箱验证码"
        email_body = title + "你的邮箱验证码为: {0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            data = True
        return data

    elif send_type == "activate":
        email_title = title + "账号激活链接"
        url = '{host}//user/active/{code}'.format(host=HOST, code=code)

        email_body = email_body.format(host=HOST, notice="请点击下面的链接激活你的账号(此链接有效期为24小时):", url=url, email=email)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email], html_message=email_body)
        if send_status:
            data = True
        return data

    elif send_type == "forget":
        email_title = title + "密码重置链接"
        url = '{host}/user/forget/{code}'.format(host=HOST, code=code)
        email_body = email_body.format(host=HOST, notice="请点击下面的链接重置密码(此链接有效期为24小时):", url=url, email=email)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email], html_message=email_body)
        if send_status:
            data = True
        return data

    elif send_type == "update_email":
        email_title = title + "邮箱验证码"
        email_body = email_title + "你的邮箱验证码为: {0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            data = True
        return data

