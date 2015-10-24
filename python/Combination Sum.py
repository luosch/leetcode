class Solution(object):
    def combinationSum(self, candidates, target):
        candidates = sorted(set(candidates))
        stack = [([], 0, target)]
        length = len(candidates)
        ans = []

        while stack:
            tmp, index, t = stack.pop()
            for i in range(index, length):
                num = candidates[i]
                if t == num:
                    ans.append(tmp + [num])
                elif t > num:
                    stack.append((tmp + [num], i, t - num))

        return ans
