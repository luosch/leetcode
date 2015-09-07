# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        stack, answer = [root], []
        while stack:
            top = stack.pop()
            if top:
                answer.append(top.val)
                stack.append(top.right)
                stack.append(top.left)
        return answer
        
