# coding: utf-8

a = 'a', 1, 17, -9
b = 'b', 7, 38, 16
c = 'c', 12, 7, 8
lst = [a, b, c]
y = []
for i in lst:
    y.append(i[2])
for i in lst:
    if i[2] == max(y):
        print "%s : %2d %2d %2d <-- UPPER" % i
    else:
        print "%s : %2d %2d %2d" % i

