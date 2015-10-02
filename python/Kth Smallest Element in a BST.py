# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, answer):
        if root:
            self.dfs(root.left, answer)
            answer.append(root.val)
            self.dfs(root.right, answer)

    def kthSmallest_rec(self, root, k):
        answer = []
        self.dfs(root, answer)
        return answer[k - 1]
    
    def kthSmallest(self, root, k):
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if k > 1:
                    k -= 1
                else:
                    return node.val
                
                node = node.right
