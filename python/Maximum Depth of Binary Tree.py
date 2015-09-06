# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    max_depth = 0
    def maxDepth(self, root):
        if root == None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        if (left_depth > right_depth):
            return left_depth + 1
        else:
            return right_depth + 1
        
