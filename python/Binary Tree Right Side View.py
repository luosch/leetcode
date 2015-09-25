# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        
        old = [root]
        current = []
        answer = []
        
        while old + current:
            front = old.pop(0)

            if front.left:
                current.append(front.left)
            if front.right:
                current.append(front.right)
            
            if not old:
                answer.append(front.val)
                old, current = current, []
        
        return answer
