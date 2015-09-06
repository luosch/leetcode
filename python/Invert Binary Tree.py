# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        # dfs
        stack = [root]
        while stack:
            top = stack.pop()
            if top:
                top.left, top.right = top.right, top.left
                stack.extend([top.left, top.right])
        return root
        
