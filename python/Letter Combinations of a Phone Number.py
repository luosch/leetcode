class Solution(object):
    def letterCombinations(self, digits):
        dl = {
            2: [a, b, c],
            3: [d, e, f],
            4: [g, h, i],
            5: [j, k, l],
            6: [m, n, o],
            7: [p, q, r, s],
            8: [t, u, v],
            9: [w, x, y, z],
            0: [ ],
        }
        if not digits:
            return []
        n = len(digits)
        # from collections import deque
        ans = list()
        queue = collections.deque([])
        while queue:
            front = queue.popleft()
            l = len(front)
            if l == n:
                ans.append(front)
            else:
                next_d = digits[l]
                for item in dl[next_d]:
                    queue.append(front + item)
        
        return ans
