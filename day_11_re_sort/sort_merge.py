# coding: utf-8


def merge(l_lst, r_lst, verbose):
    res = []
    if verbose:
        print "left -> %s \t right -> %s" % (l_lst, r_lst)
    while l_lst and r_lst:
        res.append((l_lst if l_lst[0] < r_lst[0] else r_lst).pop(0))
    return res + l_lst + r_lst


def msort(sp, verbose=False):
    lenght = len(sp)
    if lenght > 1:
        sp = merge(msort(sp[:lenght/2], verbose), msort(sp[lenght/2:], verbose), verbose)
    return sp

if __name__ == '__main__':
    s = [10, 27, 2, -12, 6, -5, 0, 13, 11, 7, -1, 11, -3, 45, -123, 89]
    print msort(s, True)
