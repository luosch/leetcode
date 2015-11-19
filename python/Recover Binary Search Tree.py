# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        self.w1 = self.w2 = self.pre = None
        self.inorder(root)
        self.w1.val, self.w2.val = self.w2.val, self.w1.val
    
    def inorder(self, root):
        if not root:
            return
        
        self.inorder(root.left)
        
        if not self.pre:
            self.pre = root
        else:
            if not self.w1 and root.val < self.pre.val:
                self.w1 = self.pre
            if self.w1 and root.val < self.pre.val:
                self.w2 = root
            else:
                self.pre = root
            
        self.inorder(root.right)
