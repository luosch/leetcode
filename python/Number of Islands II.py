class Solution(object):
    def numIslands2(self, m, n, positions):
        answer, father = [], [-1] * (m * n)
        num = 0
        
        def find(x):
            if x != father[x]:
                father[x] = find(father[x])
            return father[x]
        
        def union(x, y):
            root1, root2 = find(x), find(y)
            if root1 == root2:
                return True
            else:
                father[root1] = root2
                return False
        
        for pos in positions:
            num += 1
            idx = pos[0] * n + pos[1]
            father[idx] = idx
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = pos[0] + d[0]
                y = pos[1] + d[1]
                new_idx = x * n + y
                if x < 0 or x >= m or y < 0 or y >= n or father[new_idx] == -1:
                    continue
                if not union(idx, new_idx):
                    num -= 1
            answer.append(num)
        
        return answer
