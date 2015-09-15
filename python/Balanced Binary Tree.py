# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root):
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            return max(self.dfs(root.left), self.dfs(root.right)) + 1
        
    def isBalanced(self, root):
        if not root:
            return True
        elif abs(self.dfs(root.left) - self.dfs(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
