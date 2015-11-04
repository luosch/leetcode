# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ans = []
    def pathSum(self, root, sum):
        self.ans = []
        self.dfs(root, sum, [])
        return self.ans
    
    def dfs(self, root, sum, tmp):
        if not root:
            return
    
        if root.left == None and root.right == None and sum == root.val:
            self.ans.append(tmp + [root.val])
            return
    
        self.dfs(root.left, sum - root.val, tmp + [root.val])
        self.dfs(root.right, sum - root.val, tmp + [root.val])
