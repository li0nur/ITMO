# coding: utf-8

import os

dir_path = os.getcwd() + "/h1"
word = "Python"
count = 0
try:
    os.chdir(dir_path)
    for f_name in os.listdir(dir_path):
        if f_name.split('.')[-1] == "txt":
            f = open(f_name, 'r')
            for line in f.xreadlines():
                count += line.count(word)
                count += line.count(word.lower())
            f.close()
            print "В файле", f_name, count, "вхождений слова Python."
except OSError:
    print "Каталог ", dir_path, " не найден."
