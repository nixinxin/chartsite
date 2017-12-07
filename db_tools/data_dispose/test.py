#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "xin nix"
import re
from pypinyin import pinyin, lazy_pinyin
import pypinyin
a = 0
one = " = models."

with open('one.py', 'w+', encoding='utf-8') as ff:
    with open('G:\pycharm\chartsite\models.py', 'r') as f:
        for i in f.readlines():
            a += 1
            if one in i and "id" not in i:
                row = ""
                ziduan = i.strip(" ").split(" = ")[0]
                left = ziduan.strip().strip("_field")
                if "db_column=" not in i:
                    verbose = ", verbose_name='{}')".format(ziduan)
                    dbcolumn = ", db_column='{}'".format(ziduan)
                    row = i[:-2] + dbcolumn + verbose
                elif "db_column=" in i:
                    ziduans = re.findall("db_column=(.+?)[\"']", i)[0][1:]
                    verbose = ", verbose_name='{}')".format(ziduans)
                    i = re.findall(".+, null=True?", i)[0]
                    row = i + verbose
                if ziduan.strip() == "支链淀粉":
                    left = "次链淀粉"
                temp = lazy_pinyin(left)
                temps = []
                for j in temp:
                    temps.append(j[:2])
                hanzi_pinyin = "".join(temps)
                i = "    " + row.replace(ziduan, hanzi_pinyin, 1).strip() + "\n"

            ff.write(i)
