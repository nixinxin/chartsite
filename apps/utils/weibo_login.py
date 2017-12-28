#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "xin nix"
from chartsite.settings import SOCIAL_AUTH_WEIBO_KEY, SOCIAL_AUTH_WEIBO_SECRET
redirect_url = "http://127.0.0.1/complete/weibo/"
client_id = SOCIAL_AUTH_WEIBO_KEY
client_secret = SOCIAL_AUTH_WEIBO_SECRET
import requests


def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    auth_url = weibo_auth_url + "?client_id={client_id}&redirect_uri={re_url}".format(client_id=client_id,
                                                                                      re_url=redirect_url)
    print(auth_url)


def get_access_token(code):
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    redict = requests.post(url=access_token_url, data={
        "client_id": client_id,
        "client_secret": client_secret,
        'grant_type': "authorization_code",
        "code": code,
        "redirect_uri": redirect_url
    })
    print(redict)


def get_user_info(access_token, uid):
    user_url = "https://api.weibo.com/2/users/show.json" + "?access_token={token}&uid={uid}".format(token=access_token,
                                                                                                    uid=uid)
    print(user_url)
    result = requests.get(user_url)
    print(result)


if __name__ == "__main__":
    get_auth_url()
    get_access_token(code="b4977fde99c44a245daf6ffd47ca1c02")
    get_user_info(access_token="2.00rP55yFKXjhICa07adbfc2cioI6mB", uid="5473057431")
