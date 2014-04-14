# coding: utf-8

from stack import Stack
from datetime import datetime


class Queue(object):

    def enqueue(self, x):
        if self.stack_in.stack[1] + self.stack_out.stack[1] == self.stack_in.stack[0]:
            return "overflow"
        self.stack_in.push(x)

    def dequeue(self):
        if self.stack_out.stack[1] == 0:
            if self.stack_in.stack[1] == 0:
                #print "Queue empty"
                return
            while self.stack_in.stack[1] > 0:
                self.stack_out.push(self.stack_in.pop())
            #print "\t\t in -> %s \t out -> %s" % (self.stack_in, self.stack_out)
        return self.stack_out.pop()

    def __str__(self):
        return "in -> %s \t out -> %s" % (self.stack_in, self.stack_out)

    def __init__(self, size):
        self.stack_in = Stack(size)
        self.stack_out = Stack(size)


if __name__ == '__main__':

    def check_queue(queue):
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
    q = Queue(5)
    in_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    print "Попытка чтения пустой очереди:", q.dequeue()
    print "Объект очереди:\n", q
    print "На входе: {0} \nНа выходе: {1}".format(in_data, check_queue(q))
    print "Объект очереди:\n", q
    print "Попытка чтения пустой очереди:", q.dequeue()
    print "На входе: {0} \nНа выходе: {1}".format(in_data, check_queue(q))
    t2 = datetime.now()
    print "-" * 50
    print "Время работы queue2.py -", t2 - t1