class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.cursor = -1
        if len(vec2d) > 0:
            self.data = reduce(lambda a,b:a+b, vec2d)
        else:
            self.data = []
        self.data_len = len(self.data)
        

    def next(self):
        self.cursor += 1
        return self.data[self.cursor]
        
        

    def hasNext(self):
        return self.cursor < self.data_len - 1
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
