# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, start, end):
        if start == end:
            return None
        
        ret = []
        for i in range(start, end):
            for l in self.dfs(start, i) or [None]:
                for r in self.dfs(i + 1, end) or [None]:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    ret.append(node)
        
        return ret
        
    def generateTrees(self, n):
        if n == 0:
            return [[]]
        else:
            return self.dfs(1, n + 1)
