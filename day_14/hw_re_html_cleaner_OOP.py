# coding: utf-8

import re


class CleanerHTML(object):

    dictionary_tags = {"meta": 1, "link": 1, "style": 2, "script": 2}

    def make_pattern(self, verbose):
        try:
            p1 = [key for key in self.args if self.dictionary_tags[key] == 1]
            p2 = [key for key in self.args if self.dictionary_tags[key] == 2]
        except KeyError as detail:
            print "-" * 100
            class_name = str(self.__class__).split(".")[1].rstrip("'>")
            print "WARNING! Тег {0} в словаре тегов класса {1} не найден.\n" \
                  "Необходимо убедиться в том, что указанный тег существует в HTML и дополнить словарь."\
                .format(detail, class_name)
            self.args.remove(str(detail).strip("'"))
            self.make_pattern(verbose=False)
            p1 = [key for key in self.args if self.dictionary_tags[key] == 1]
            p2 = [key for key in self.args if self.dictionary_tags[key] == 2]
        part1 = r'(?:' + '|'.join(p1) + r').*?'
        part2 = r'(' + '|'.join(p2) + r').*?>(?:\s|\S)*?</\1'
        if p1 and p2:
            p = r'<(?:' + part1 + '|' + part2 + ')>'
        elif p1:
            p = r'<(?:' + part1 + ')>'
        elif p2:
            p = r'<(?:' + part2 + ')>'
        else:
            return
        if verbose:
            print "-" * 100 + "\nPATTERN --> \t %s" % p
        return re.compile(p)

    def read_html(self):
        line_number = 0
        data = ""
        f = open(self.f_name)
        for line in f.xreadlines():
            line_number += 1
            for j in tags:
                k = line.count("<" + j)
                self.tags_dict[j][0] = self.tags_dict[j][0] + k
                if k:
                    self.tags_dict[j].append(line_number)
            data += line
        f.close()
        return data

    def clean_html(self, data, verbose=False):
        pattern = self.make_pattern(verbose)
        if pattern:
            if verbose:
                mo = pattern.finditer(data)
                print "-" * 100
                print "Удалены следующие конструкции:\n"
                for j in mo:
                    print j.group()
            data = pattern.sub("", data)
            return data
        else:
            return "No matches was found"

    def __str__(self):
        strings = ["В файле {0} тег <{1}> найден {2} раз(а), в строках под номер(ом|ами): {3}"
                   .format(self.f_name, key, self.tags_dict[key][0], self.tags_dict[key][1:])
                   for key in self.tags_dict]
        return "\n".join(strings)

    def __init__(self, f_name, args):
        self.f_name = f_name
        self.args = args
        self.tags_dict = {}
        for i in tags:
            self.tags_dict[i] = [0]


if __name__ == '__main__':

    filename = "Django_1.6_tutorial02.html"
    #tags = ["title"]
    #tags = ["title", "meta", "style"]
    tags = ["meta", "link", "style", "script", "title", "TEST-TEST"]
    cl = CleanerHTML(filename, tags)
    f_out = open("clear.html", "w")
    in_data = cl.read_html()
    print cl
    #out_data = cl.clean_html(in_data)
    out_data = cl.clean_html(in_data, True)
    f_out.write(out_data)
    f_out.close()