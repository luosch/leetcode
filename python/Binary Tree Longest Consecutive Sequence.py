# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        if not root:
            return 0
        else:
            self.answer = 0
            self.dfs(root, 1)
            return self.answer
    
    def dfs(self, root, seq_len):
        self.answer = max(self.answer, seq_len)
        if root.left:
            if root.left.val == root.val + 1:
                self.dfs(root.left, seq_len + 1)
            else:
                self.dfs(root.left, 1)
        if root.right:
            if root.right.val == root.val + 1:
                self.dfs(root.right, seq_len + 1)
            else:
                self.dfs(root.right, 1)
