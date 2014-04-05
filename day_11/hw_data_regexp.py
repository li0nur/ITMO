# coding: utf-8

import re

p = r'(?:0[1-9]|[12]\d|3[01])\.(?:0[1-9]|1[0-2])\.\d{4}(?!\d)'
string = '07.12.2014 jsggfsk 11.09.2014 11.13.2014 37.12.2013 07.12.91988 00.01.2014 113.13.2014 11.143.2014 10.01.1914'
number_re = re.compile(p)
print number_re.findall(string)
