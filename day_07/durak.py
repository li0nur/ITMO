# coding: utf-8
"""
    Дурак версии 1.0
    ----------------

    Ограничения:
        - в игре участвуют только два игрока;
        - сходить можно только одной картой, возможность подкинуть не предусмотрена.

    Глюки:
        иногда может быть принято неверное решение о том, какой картой биться. Это происходит в те моменты,
        когда на руке присутствуют карты того же ранга, что и "правильная карта" (минильно возможный ранг для
        подброшенной масти)
"""

from cards import *


def _print():
    print "\n" + "-" * 50 + "\n"


def distribute_card():
    for i in range(6):
        for h in [h1, h2]:
            karta = d.moveCard()
            h.addCard(karta)
    return h1, h2


def choose_first_hand(k1, k2):
    if len(k1) > 0 and len(k2) > 0:
        if cmp(k1[0], k2[0]) == 1:
            hod_index = name2
            print "Ходит %s" % hod_index
        else:
            hod_index = name1
            print "Ходит %s" % hod_index
    elif len(k1) == 0 and len(k2) > 0:
        hod_index = name2
        print "Ходит %s" % hod_index
    else:
        hod_index = name1
        print "Ходит %s" % hod_index
    return hod_index


def hod(hod_index):
    while len(h1.cards) and len(h2.cards) > 0:
        if hod_index == name1:
            hod = h1.moveCard(0)
            print "Ход %s:" % name1, hod
            hod_index = boi(name2, h2, hod, hod_index)
            if hod_index == name1:
                try:
                    if len(h1.cards) < 6:
                        karta = d.moveCard()
                        h1.addCard(karta)
                        Person.sortCard(h1.cards)
                    yield hod_index
                except IndexError:
                    yield hod_index
            else:
                try:
                    if len(h1.cards) < 6:
                        karta = d.moveCard()
                        h1.addCard(karta)
                        Person.sortCard(h1.cards)
                    if len(h2.cards) < 6:
                        karta = d.moveCard()
                        h2.addCard(karta)
                        Person.sortCard(h2.cards)
                    yield hod_index
                except IndexError:
                    yield hod_index
        else:
            hod = h2.moveCard(0)
            print "Ход %s:" % name2, hod
            hod_index = boi(name1, h1, hod, hod_index)
            if hod_index == name2:
                try:
                    if len(h2.cards) < 6:
                        karta = d.moveCard()
                        h2.addCard(karta)
                        Person.sortCard(h2.cards)
                    yield hod_index
                except IndexError:
                    yield hod_index
            else:
                try:
                    if len(h2.cards) < 6:
                        karta = d.moveCard()
                        h2.addCard(karta)
                        Person.sortCard(h2.cards)
                    if len(h1.cards) < 6:
                        karta = d.moveCard()
                        h1.addCard(karta)
                        Person.sortCard(h1.cards)
                    yield hod_index
                except IndexError:
                    yield hod_index


def boi(name, h, hod, hod_index):
    k = [card for card in h.cards if card.trump is not None]
    var = [card for card in h.cards if card.suit == hod.suit]
    var.extend(k)
    if len(var) > 0:
        for i in var:
            if i > hod:
                otvet = h.moveCard(h.cards.index(i))
                print "Ответ %s:" % name, otvet, "на", hod
                return name
        try:
            print otvet  # костыль =)
        except NameError:
            print "Vse <. Beru!"
            h.addCard(hod)
            Person.sortCard(h.cards)
            return hod_index
    else:
        print "Ответ %s:" % name, "Beru!"
        h.addCard(hod)
        Person.sortCard(h.cards)
        return hod_index

#@staticmethod
#name1 = raw_input("Приветствую! Как Вас зовут?\n")
name1 = "Maks"
name2 = "Melamori"
Person.deanonimise(name1)

# создаем экземпляр класса колода
d = Deck()
_print()
print "Печатаем колоду:\n", d

# создаем экземпляр класса рука
h1 = Hand()
h2 = Hand()
print "Рука %s:\t\t" % name1, h1.cards, "\nРука %s:\t" % name2, h2.cards

# перемешиваем колоду
d.shuffle()
_print()
print "Перемешанная колода:\n", d

# сдаем 6 карт
distribute_card()
print "Рука %s:\n" % name1, h1, "\nРука %s:\n" % name2, h2, "\nОстаток колоды:\n", d

# выбираем козырь
k = d.chooseTrump()
_print()
print "Козырь:", k

# устанавливаем признак "козырь" всем картам с такой же мастью как и k
d.trump = k
for h in [h1, h2]:
    h.trump = k
    Person.sortCard(h.cards)
print "Рука %s:\n" % name1, h1
print "Рука %s:\n" % name2, h2
k1 = [card for card in h1.cards if card.trump is not None]
k2 = [card for card in h2.cards if card.trump is not None]
hod_index = choose_first_hand(k1, k2)

# делаем ход младшей картой на руке
_print()
for perehod in hod(hod_index):
    print "Количество карт в колоде:", len(d.cards)
    print "Ход переходит к %s" % perehod
    print "Рука %s:\n" % name1, h1
    print "Рука %s:\n" % name2, h2
    _print()
    hod_index = perehod

# решение о победителе
if len(h1.cards) > 0 and len(h2.cards) == 0:
    print "Победитель %s" % hod_index
elif len(h1.cards) == 0 and len(h2.cards) > 0:
    print "Победитель %s" % hod_index
else:
    print "Ничья!"