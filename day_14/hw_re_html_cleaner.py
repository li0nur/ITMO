# coding: utf-8

import re

f_name = "Django_1.6_tutorial02.html"
tags = ("meta", "link", "style")
dict_tags = {}
line_number = 0
in_data = ""
p = r'<(?:(?:{0}|{1}).*?|({2})>(?:\s|\S)*</\1)>'.format(*tags)
pattern = re.compile(p)
f = open(f_name)
f_out = open("clear.html", "w")
for i in tags:
    dict_tags[i] = [0]
for line in f.xreadlines():
    line_number += 1
    for i in tags:
        k = line.count("<" + i)
        dict_tags[i][0] = dict_tags[i][0] + k
        if k:
            dict_tags[i].append(line_number)
    in_data += line
for key in dict_tags:
    print "В файле {0} тег <{1}> найден и удален {2} раз(а)," \
          " в строках под номер(ом|ами): {3}".format(f_name, key, dict_tags[key][0], dict_tags[key][1:])
f.close()
print "-" * 100
print "Удалены следующие конструкции:\n"
mo = pattern.finditer(in_data)
for i in mo:
    print i.group()
out_data = pattern.sub("", in_data)
f_out.write(out_data)
f_out.close()
