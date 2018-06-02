import os
import sys
import time

import django
import json

import requests

from chartsite.settings import BASE_DIR

sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chartsite.settings")

django.setup()

from resource.models import ZgtsNcp

# url = "http://api.map.baidu.com/geocoder/v2/?address={}&output=json&ak=XbKB5htKalcYGbal6DbWlEY8pKzeXG8F"
url = "http://restapi.amap.com/v3/geocode/geo?address={}&key=9aff25df14c2842eccf896847c871141"
datas = ZgtsNcp.objects.all()

from fake_useragent import UserAgent

# for i in datas:
#     if not i.lng:
#         urls = url.format(i.location)
#         user = getattr(UserAgent(), 'random')
#         results = requests.get(urls, headers={"User-Agent": user})
#         # result = '{"status":0,"result":{"location":{"lng":113.42206002079804,"lat":22.545177514512998},"precise":0,"confidence":14,"level":"城市"}}'
#         if results.status_code == 200:
#             result = json.loads(results.text)['result']['location']
#
#             rec = ZgtsNcp.objects.filter(location=i.location)
#             for j in rec:
#                 j.lng = result['lng']
#                 j.lat = result['lat']
#                 j.save()
#             print(result, i.location)

for i in datas:
    if not i.lng:
        urls = url.format(i.location)
        user = getattr(UserAgent(), 'random')
        results = requests.get(urls, headers={"User-Agent": user})
        # result = '{"status":0,"result":{"location":{"lng":113.42206002079804,"lat":22.545177514512998},"precise":0,"confidence":14,"level":"城市"}}'
        if results.status_code == 200:
            result = json.loads(results.text)['result']['location']

            rec = ZgtsNcp.objects.filter(location=i.location)
            for j in rec:
                j.lng = result['lng']
                j.lat = result['lat']
                j.save()
            print(result, i.location)
