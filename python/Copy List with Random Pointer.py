# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        # use DFS to visit the graph
        # DFS info must be stored within visited
        self.visited = {}
        return self.DFS(head)

    def DFS(self, node):
        if not node:
            return None
        if node not in self.visited: # visited
            self.visited[node] = RandomListNode(node.label)
            self.visited[node].next = self.DFS(node.next)
            self.visited[node].random = self.DFS(node.random)
        return self.visited[node]
