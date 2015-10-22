# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        self.it = iterator
        if self.it.hasNext():
            self.tmp = self.it.next()
        else:
            self.tmp = None
        
    def peek(self):
        return self.tmp
        
    def next(self):
        pre_tmp = self.tmp
        if self.it.hasNext():
            self.tmp = self.it.next()
        else:
            self.tmp = None
        return pre_tmp

    def hasNext(self):
        return self.tmp is not None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
