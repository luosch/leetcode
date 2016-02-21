# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        delta = abs(root.val - target)
        res = root.val
        
        if root.left and target < root.val:
            left_value = self.closestValue(root.left, target)
            if abs(left_value - target) < delta:
                res = left_value
            
        if root.right and target > root.val:
            right_value = self.closestValue(root.right, target)
            if abs(right_value - target) < delta:
                res = right_value
        
        return res
