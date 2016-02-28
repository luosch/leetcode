# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        small, large = [], []
        self.inorder(root, target, small)
        self.inorder_reverse(root, target, large)
        answer = []
        
        while len(answer) < k:
            if len(small) == 0:
                answer.append(large.pop())
            elif len(large) == 0:
                answer.append(small.pop())
            elif abs(small[-1] - target) < abs(large[-1] - target):
                answer.append(small.pop())
            else:
                answer.append(large.pop())
        
        return answer
        
    def inorder(self, root, target, stack):
        if not root:
            return
        self.inorder(root.left, target, stack)
        if root.val > target:
            return
        else:
            stack.append(root.val)
        self.inorder(root.right, target, stack)
        
    
    def inorder_reverse(self, root, target, stack):
        if not root:
            return
        self.inorder_reverse(root.right, target, stack)
        if root.val <= target:
            return
        else:
            stack.append(root.val)
        self.inorder_reverse(root.left, target, stack)
    
