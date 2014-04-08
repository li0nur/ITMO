# coding: utf-8

from fractions import Fraction
from optparse import OptionParser


def sum_fraction(ch_a, zn_a, ch_b, zn_b):
    return Fraction(ch_a, zn_a) + Fraction(ch_b, zn_b)


def subtract_fraction(ch_a, zn_a, ch_b, zn_b):
    return Fraction(ch_a, zn_a) - Fraction(ch_b, zn_b)


def multiple_fraction(ch_a, zn_a, ch_b, zn_b):
    return Fraction(ch_a, zn_a) * Fraction(ch_b, zn_b)


def devide_fraction(ch_a, zn_a, ch_b, zn_b):
    return Fraction(ch_a, zn_a) / Fraction(ch_b, zn_b)


def verbose_mode(o, ch_a, zn_a, ch_b, zn_b):
    return "%d/%d %s %d/%d" % (ch_a, zn_a, o, ch_b, zn_b)


def main():
    parser = OptionParser(description=u"Простейший калькулятор дробей.")
    parser.add_option("-v", "--verbose", help=u"многословный вывод", action="store_true", dest="verbose", default=False)
    parser.add_option("-a", "--fraction_a", help=u"значение первой дроби, например: 3/4", action="store", dest="a")
    parser.add_option("-b", "--fraction_b", help=u"значение второй дроби, например: 1/2", action="store", dest="b")
    parser.add_option("-o", "--operation", help=u"операция +, -, * или : \
                                                для операции умножения возможно \
                                                необходим экранирующий символ: '\*' \
                                                (default = '%default')", action="store", dest="o", default="+")
    (options, args) = parser.parse_args()
    try:
        args = int(options.a.split("/")[0]), int(options.a.split("/")[1]), \
               int(options.b.split("/")[0]), int(options.b.split("/")[1])
        if options.o == "+":
            if options.verbose:
                print verbose_mode(options.o, *args)
            print "=", sum_fraction(*args)
        elif options.o == "-":
            if options.verbose:
                print verbose_mode(options.o, *args)
            print "=", subtract_fraction(*args)
        elif options.o == "*":
            if options.verbose:
                print verbose_mode(options.o, *args)
            print "=", multiple_fraction(*args)
        elif options.o == ":":
            if options.verbose:
                print verbose_mode(options.o, *args)
            print "=", devide_fraction(*args)
        else:
            print "Invalid operation -o: '%s'. Type -h for help." % options.o
            opt = parser.option_list[-1]
            help_str = opt.help.replace(u"  ", u"")
            start, end = help_str.find(u"для"), help_str.find(u" (")
            print help_str[start:end]
    except AttributeError:
        print "Необходимо задать дроби!"
        parser.print_help()


if __name__ == '__main__':
    main()
