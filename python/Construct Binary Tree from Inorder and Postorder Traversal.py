# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        
        root_val = postorder.pop()
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        root.right = self.buildTree(inorder[root_index + 1:], postorder)
        root.left = self.buildTree(inorder[:root_index], postorder)
        
        return root
