# coding: utf-8

from cards import *


def _print():
    print "\n" + "-" * 50 + "\n"

# создаем экземпляр класса колода
d = Deck()
_print()
print "Печатаем колоду:\n", d

# создаем экземпляр класса рука
h = Hand()
print "Пустая рука:\n", h.cards

# перемешиваем колоду
d.shuffle()
_print()
print "Перемешанная колода:\n", d

# сдаем 6 карт
for i in range(6):
    karta = d.moveCard()
    h.addCard(karta)
print "На руке:\n", h, "\nОстаток колоды:\n", d

# выбираем козырь
k = d.chooseTrump()
_print()
print "Козырь:", k

# устанавливаем признак "козырь" всем картам с такой же мастью как и k
d.setIndexTrump(k)
h.setIndexTrump(k)

# делаем ход младшей картой на руке
hod = h.moveCard(0)
_print()
print "Ход:", hod, "\n", "Осталось на руке:\n", h

# добор карты из колоды
karta = d.moveCard()
h.addCard(karta)
_print()
print "На руке после добора:\n", h, "\nОстаток колоды:\n", d
_print()
