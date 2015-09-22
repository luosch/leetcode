# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    # using bfs
    def connect(self, root):
        queue = []
        queue.append(root)
        
        while queue:
            root = queue.pop()
            if root is None:
                continue
            if root.left:
                isFound = False
                tmp = root
                while isFound == False and tmp:
                    if tmp.right:
                        root.left.next = tmp.right
                        isFound = True
                    else:
                        tmp = tmp.next
                        if tmp and tmp.left:
                            root.left.next = tmp.left
                            isFound = True
    
            if root.right:
                isFound = False
                tmp = root.next
                while isFound == False and tmp:
                    if tmp.left:
                        root.right.next = tmp.left
                        isFound = True
                    elif tmp.right:
                        root.right.next = tmp.right
                        isFound = True
                    else:
                        tmp = tmp.next

            queue.append(root.left)
            queue.append(root.right)
