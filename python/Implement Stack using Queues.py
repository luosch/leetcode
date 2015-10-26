class Stack(object):
    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.size = 0
        

    def push(self, x):
        if len(self.q2) == 0:
            self.q1.append(x)
        else:
            self.q2.append(x)
        self.size += 1
        

    def pop(self):
        if not self.q2:
            for _ in xrange(self.size - 1):
                self.q2.append(self.q1.pop(0))
            self.q1.pop(0)
        else:
            for _ in xrange(self.size - 1):
                self.q1.append(self.q2.pop(0))
            self.q2.pop(0)
        self.size -= 1
        

    def top(self):
        if not self.q2:
            for _ in xrange(self.size - 1):
                self.q2.append(self.q1.pop(0))
            tmp = self.q1.pop(0)
            self.q2.append(tmp)
            return tmp
        else:
            for _ in xrange(self.size - 1):
                self.q1.append(self.q2.pop(0))
            tmp = self.q2.pop(0)
            self.q1.append(tmp)
            return tmp

    def empty(self):
        return self.size == 0
