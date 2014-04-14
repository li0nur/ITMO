# coding: utf-8


class Stack(object):

    def push(self, x):
        if self.stack[1] == self.stack[0]:
            print "stack overflow"
            return self.stack
        self.stack[1] += 1
        self.stack += [x]
        return self.stack

    def pop(self):
        if self.stack[1] == 0:
            print "stack empty"
            return self.stack
        self.stack[1] -= 1
        x = self.stack[-1]
        self.stack = self.stack[:-1]
        return x

    def top(self):
        if self.stack[1] == self.stack[0]:
            return self.stack[self.stack[1]+1], "stack overflow"
        elif self.stack[1] == 0:
            return None, "stack empty"
        else:
            return self.stack[self.stack[1]+1], ""

    def __str__(self):
        return "Stack: {0} \t top: {1} \t {2}".format(self.stack, self.top()[0], self.top()[1])

    def __init__(self, size):
        """В первом элементе списка хранится размер стека, во втором - кол-во элементов в стеке"""
        self.stack = [size, 0]

if __name__ == '__main__':
    s1 = Stack(5)
    n = 6
    print s1
    print "-" * 30
    for i in range(n):
        s1.push(i)
        print s1
        print "-" * 30
    for i in range(n):
        s1.pop()
        print s1
        print "-" * 30
