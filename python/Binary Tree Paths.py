# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        else:
            return [str(root.val) + '->' + path                 for leaf in (root.left, root.right) if leaf                 for path in self.binaryTreePaths(leaf)] or ['%d' % root.val]
