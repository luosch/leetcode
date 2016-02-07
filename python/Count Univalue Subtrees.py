# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        self.res = 0
        self.dfs(root)
        return self.res
        
    def dfs(self, root):
        if root == None:
            return None
        
        left, right = self.dfs(root.left), self.dfs(root.right)
        if left == None and right == None:
            self.res += 1
            return root.val
        elif left == False or right == False:
            return False
        else:
            if (left == right and root.val == left) or                 (left == None and right == root.val) or (right == None and left == root.val):
                self.res += 1
                return root.val
            else:
                return False
