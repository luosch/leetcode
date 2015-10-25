# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, num):
        tmp = 0
        if root.left:
            tmp += self.dfs(root.left, num * 10 + root.val)
        if root.right:
            tmp += self.dfs(root.right, num * 10 + root.val)
        if not root.left and not root.right:
            tmp += 10 * num + root.val
        return tmp

    def sumNumbers(self, root):
        if not root:
            return 0
        return self.dfs(root, 0)
