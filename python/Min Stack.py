class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
        else:
            minNumber = self.stack[-1][1]
            if x < minNumber:
                minNumber = x
            self.stack.append((x, minNumber))
        

    def pop(self):
        if self.stack:
            self.stack.pop()
        

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        else:
            return None
