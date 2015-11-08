class Solution(object):
    def removeInvalidParentheses(self, s):
        def calc(s):
            a = b = 0
            for c in s:
                a += {'(' : 1, ')' : -1}.get(c, 0)
                b += a < 0
                a = max(a, 0)
            return a + b

        visited = set([s])
        ans = []
        queue = collections.deque([s])
        done = False
        while queue:
            t = queue.popleft()
            mi = calc(t)
            if mi == 0:
                done = True
                ans.append(t)
            if done:
                continue
            for x in range(len(t)):
                if t[x] not in ('(', ')'):
                    continue
                ns = t[:x] + t[x+1:]
                if ns not in visited and calc(ns) < mi:
                    visited.add(ns)
                    queue.append(ns)

        return ans
