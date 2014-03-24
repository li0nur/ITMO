# coding: utf-8

"""
translate(word, [amount], [params])

Ф-ия-словарик для перевода слов с англ.яз.
    - слова, например: sun, like...
    - у каждого слова:
        - транскрипция (русск.буквы)
        - несколько значений
        - значения делятся по типам - гл., сущ., прил.
    - по умолчанию выводить все данные
    - д.б. возможность получить только значение по типу (гл., прил. и т.п.)
    - или только транскрипцию
    - или любые сочетания
    - возможность задать максимальное кол-во выводимых значений по типу

При выборе максимального кол-ва выводимых значений в конце строки может появиться "...". Это означает,
что в словаре есть еще варианты перевода этого слова. Все варианты можно получить, указав в качестве
параметра [amount] 0 или опустить его.

[params]
    t   -   транскрипция
    n   -   существительное
    v   -   глагол
    a   -   прилагательное
    ad  -   наречие

Пример использования ф-ии:
>>>translate("warm", 0, "t", "n", "v")
warm
t -> [ворм]
n -> тепло
v -> греть, нагревать
>>>
"""

dictonary = {'sun': {'t': '[сан]', 'n': 'солнце', 'a': None, 'ad': None, 'v': None},
             'like': {'t': '[лайк]', 'v': ('нравиться', 'любить', 'обожать'), 'n': 'любовь', 'ad': ('подобно', 'как'),
                      'a': None},
             'warm': {'t': '[ворм]', 'n': 'тепло', 'a': ('теплый', 'горячий'),
                      'v': ('греть', 'нагревать'), 'ad': None},
             'rest': {'t': '[рест]', 'n': ('отдых', 'отпуск', 'остаток'), 'v': ('отдыхать', 'расслабляться'), 'a': None,
                      'ad': None}}


def translate(word, *args):
    result = word + "\n" + "-" * 10 + "\n"
    if args:
        k, args = check_params(*args)
        if args:
            result += form_result(word, k, *args)
        else:
            result += form_result(word, k, *dictonary[word].keys())
        return result
    else:
        k = 0
        result += form_result(word, k, *dictonary[word].keys())
        return result


def form_result(word, k, *params):
    data = dictonary[word]
    t_str, result = "", ""
    for key in params:
        try:
            if type(data[key]) == tuple:
                if k == 0:
                    k = len(data[key])
                for i in data[key][:k]:
                    t_str += i + ", "
                if 0 < k < len(data[key]):
                    t_str = t_str[:-2] + "..."
                result += "%s -> %s \n" % (key, t_str.rstrip(", "))
            elif data[key] is None:
                continue
            else:
                result += "%s -> %s \n" % (key, data[key])
            t_str = ""
        except KeyError as detail:
            print "WARNING!\nНедопустимый аргумент:", detail, "\nМожет быть любой из: 't', 'a', 'n', 'ad', 'v'"
    return result


def check_params(*args):
    if type(args[0]) == int:
        k = args[0]
        args = args[1:]
    else:
        k = 0
    return k, args