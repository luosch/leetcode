# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        if root is None:
            return []
        tree = []
        queue = []
        current = []
        queue.append(root)
        queue.append(None)

        while len(queue) > 1:
            front = queue[0]
            del queue[0]
            
            if front == None:
                tree.append(current)
                current = []
                queue.append(None)
                continue
                
            current.append(front.val)
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)
        
        tree.append(current)
        tree.reverse()
        return tree
