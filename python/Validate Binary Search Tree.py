# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        
        if root.left:
            tmp = root.left
            while tmp:
                if tmp.val >= root.val:
                    return False
                tmp = tmp.right

        if root.right:
            tmp = root.right
            while tmp:
                if tmp.val <= root.val:
                    return False
                tmp = tmp.left

        return self.isValidBST(root.left) and self.isValidBST(root.right)
