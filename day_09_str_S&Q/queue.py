# coding: utf-8

from datetime import datetime


class Queue(object):
    """
    Кольцевой буфер.
        одна ячейка из n всегда будет незанятой (так как очередь с n элементами невозможно отличить от пустой)
    """

    def enqueue(self, x):
        """Перед пополнением очереди выполняется проверка на заполненность очереди n-1 элементами."""
        if self.queue[2] - self.queue[1] == self.queue[0] - 1 or self.queue[2] - self.queue[1] == -1:
            return "overflow"
        if self.queue[2] == self.queue[0]:
            self.queue[2] = 1
            self.queue[self.queue[2]+2] = x
        else:
            self.queue[2] += 1
            self.queue[self.queue[2]+2] = x
        return self.queue

    def dequeue(self):
        """Перед уменьшением очереди выполняется проверка очереди на пустоту."""
        if self.queue[1] == self.queue[2]:
            return None
        if self.queue[1] == self.queue[0]:
            self.queue[1] = 1
            x = self.queue[self.queue[1]+2]
        else:
            x = self.queue[self.queue[1]+3]
            self.queue[1] += 1
        return x

    def __str__(self):
        return "Special = {0} \t Queue = {1}".format(self.queue[:3], self.queue[3:])

    def __init__(self, size):
        """В первом элементе списка хранится размер очереди, во 2-ом - "голова", в 3-ем - "хвост"."""
        self.queue = [size, 0, 0] + [None] * size


if __name__ == '__main__':

    def check_Queue(queue):
        out_data = []
        for i in in_data:
            if queue.enqueue(i) == "overflow":
                x = queue.dequeue()
                out_data.append(x)
                #print "OUT:", out_data
                queue.enqueue(i)
            #print "IN: %s \t %s" % (i, queue)
        while x:
            x = queue.dequeue()
            if x:
                out_data.append(x)
        return out_data

    t1 = datetime.now()
    q1 = Queue(5)
    in_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    print "Попытка чтения пустой очереди:", q1.dequeue()
    print "Объект очереди:\n", q1
    print "На входе: {0} \nНа выходе: {1}".format(in_data, check_Queue(q1))
    print "Объект очереди:\n", q1
    print "Попытка чтения пустой очереди:", q1.dequeue()
    print "На входе: {0} \nНа выходе: {1}".format(in_data, check_Queue(q1))
    t2 = datetime.now()
    print "-" * 50
    print "Время работы queue.py -", t2 - t1