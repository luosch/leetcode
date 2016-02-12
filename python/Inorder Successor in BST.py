# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        answer = None
        while root:
            if root.val > p.val:
                answer = root
                root = root.left
            else:
                root = root.right
        
        return answer
