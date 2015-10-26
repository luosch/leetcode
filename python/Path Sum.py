# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        elif not root.left and not root.right:
            return root.val == sum
        else:
            b_l, b_r = False, False
            if root.left:
                b_l = self.hasPathSum(root.left, sum - root.val)
            if root.right:
                b_r = self.hasPathSum(root.right, sum - root.val)
            return b_l or b_r
