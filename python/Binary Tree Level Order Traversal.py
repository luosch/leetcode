# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        
        tree, level = [], [root]
        
        while level:
            tree.append([node.val for node in level])
            tmp = []
            for node in level:
                tmp.extend([node.left, node.right])
            level = [node for node in tmp if node]
        
        return tree
