# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    answer = []
    def rec(self, root):
        if not root:
            return
        else:
            self.rec(root.left)
            self.rec(root.right)
            self.answer.append(root.val)
    
    def postorderTraversal(self, root):
        self.answer = []
        self.rec(root)
        return self.answer
