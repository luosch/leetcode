# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        
        left_height = right_height = 1
        p, q = root.left, root.right
        while p:
            p = p.left
            left_height += 1
        while q:
            q = q.right
            right_height += 1
        
        if left_height == right_height:
            return (1 << left_height) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
