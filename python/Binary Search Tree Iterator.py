# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.current = root
        self.stack = []

    def hasNext(self):
        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left
        
        if len(self.stack) == 0:
            return False
        else:
            return True

    def next(self):
        node = self.stack.pop()
        self.current = node.right
        return node.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
