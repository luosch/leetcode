# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        self.maxSum = float('-inf')
        self.helper(root)
        return self.maxSum
        
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if left < 0:
            left = 0
        if right < 0:
            right = 0
        
        self.maxSum = max(self.maxSum, left + right + root.val)
        return max(left, right) + root.val
