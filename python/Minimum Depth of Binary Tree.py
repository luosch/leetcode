# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0

        parents = [root]
        children = []
        answer = 1

        while parents + children:
            front = parents.pop()
            
            if front:
                if not front.left and not front.right:
                    break
                
                children.append(front.left)
                children.append(front.right)
    
            if not parents:
                parents = children
                children = []
                answer += 1
        
        return answer
