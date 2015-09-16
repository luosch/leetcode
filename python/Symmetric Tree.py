# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rec(self, leftNode, rightNode):
        if leftNode is None and rightNode is None:
            return True
        elif leftNode is None or rightNode is None:
            return False
        elif leftNode.val != rightNode.val:
            return False

        return self.rec(leftNode.left, rightNode.right) and self.rec(leftNode.right, rightNode.left)
        
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.rec(root.left, root.right)
