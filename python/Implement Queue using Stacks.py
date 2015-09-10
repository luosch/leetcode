class Queue(object):
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x):
        helper = []
        for _ in xrange(self.size):
            helper.append(self.stack.pop())
        self.stack.append(x)
        for _ in xrange(self.size):
            self.stack.append(helper.pop())
        self.size += 1

    def pop(self):
        self.stack.pop()
        self.size -= 1

    def peek(self):
        return self.stack[-1]

    def empty(self):
        return self.size == 0
