# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        node, parent, right = root, None, None
        while node:
            left = node.left
            node.left = right
            right = node.right
            node.right = parent
            parent = node
            node = left
        return parent
        
    def upsideDownBinaryTree_slow(self, root):
        def rotate(root):
            if root:
                left = rotate(root.left)
                if left:
                    left.left = root.right
                    left.right = root
                root.left = root.right = None
            return root
        
        new_root = root
        while new_root and new_root.left:
            new_root = new_root.left
        
        rotate(root)
        
        return new_root
