#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "xin nix"
redirect_url = "http://127.0.0.1:8000/complete/weibo"
client_id = "3084778121"
client_secret = "6ddb49464400f59872169e2c917ddc33"
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
    result = requests.get(user_url)
    print(result)


if __name__ == "__main__":
    # get_auth_url()
    # get_access_token(code="aa04fbf1a2b1d8150d3cb5492a040879")
    get_user_info(access_token="2.00rP55yFph6l3De79e5958c20vv2jt", uid="5473057431")
