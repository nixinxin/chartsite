from django.test import TestCase
import re
# Create your tests here.

a = "ss作物优异资源种uyti质数据库dfsasd"

parttern = "[A-Za-z]+"


print(re.findall(parttern, a))

