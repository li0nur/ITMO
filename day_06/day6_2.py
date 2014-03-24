class Auto(object):
    _col = None
    cost = 300000
    def setcolor(self, col):
        self._col = col
        self.cost -= 10000
    def getcolor(self):
        return self._col
    def delcolor(self):
        del self._col
    color = property(getcolor, setcolor, delcolor, "I'm color")

a = Auto()
a.color = "green"
print help(Auto.color)
print "color: ", a.color, "cost: ", a.cost