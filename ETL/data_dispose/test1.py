#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "xin nix"
import re
from pypinyin import pinyin, lazy_pinyin
import pypinyin

pattern = ".*class \(models.Model\):.+?unique_together = \(\('id', '统一编号'\),\).*"
with open('two.py', 'w+', encoding='utf-8') as ff:
    with open("one.py", 'r', encoding='utf-8') as f:
        data = f.read()
        # print(data)
        result = re.findall("""class \(models.Model\):.+?= verbose_name""", data, re.S)
        for i in result:
            db_name = re.findall("数据库_(.+)'", i)[0]
            db_name = "".join(lazy_pinyin(db_name))
            left, right = i.split("(models.Model):")
            ii = left + db_name + "(models.Model):" + right + "\n\n"
            ff.write(ii)

