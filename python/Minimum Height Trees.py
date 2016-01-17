class Solution(object):
    def findMinHeightTrees_1(self, n, edges):
        if n == 1:
            return [0]

        children = collections.defaultdict(set)
        for s, t in edges:
            children[s].add(t)
            children[t].add(s)
        
        vertices = set(children.keys())
        while len(vertices) > 2:
            leaves = [leaf for leaf in children if len(children[leaf]) == 1]
            for leaf in leaves:
                for child in children[leaf]:
                    children[child].remove(leaf)
                del children[leaf]
                vertices.remove(leaf)
        
        return list(vertices)

    def findMinHeightTrees(self, n, edges):
        children = [set() for x in range(n)]
        for s, t in edges:
            children[s].add(t)
            children[t].add(s)
        leaves = [x for x in range(n) if len(children[x]) <= 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for x in leaves:
                for y in children[x]:
                    children[y].remove(x)
                    if len(children[y]) == 1:
                        new_leaves.append(y)
            leaves = new_leaves
        return leaves
