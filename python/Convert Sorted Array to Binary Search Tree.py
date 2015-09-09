# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildBSTNode(self, nums):
        if (len(nums) == 1):
            return TreeNode(nums[0])
        elif (len(nums) == 0):
            return None
        else:
            mid = (0 + len(nums)) / 2
            root = TreeNode(nums[mid])
            root.left = self.buildBSTNode(nums[0:mid])
            root.right = self.buildBSTNode(nums[mid + 1:len(nums)])
        return root

    def sortedArrayToBST(self, nums):
        return self.buildBSTNode(nums)
