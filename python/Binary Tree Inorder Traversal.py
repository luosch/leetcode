# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, answer):
        if root:
            self.dfs(root.left, answer)
            answer.append(root.val)
            self.dfs(root.right, answer)
    
    def inorderTraversal(self, root):
        answer = []
        self.dfs(root, answer)
        return answer
        
