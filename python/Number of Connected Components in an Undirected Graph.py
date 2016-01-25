class Solution(object):
    def countComponents(self, n, edges):
        father = range(n)
        
        def find(a):
            if father[a] != a:
                father[a] = find(father[a])
            return father[a]

        def union(a, b):
            fa, fb = find(a), find(b)
            if fa == fb:
                return 0
            else:
                father[fb] = fa
                return 1
    
        return n - sum(union(a, b) for a, b in edges)
