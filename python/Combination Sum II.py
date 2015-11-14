class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)
        stack = [([], -1, target)]
        length = len(candidates)
        ans = []

        while stack:
            tmp, index, t = stack.pop()
            for i in range(index + 1, length):
                num = candidates[i]
                if t == num:
                    if tmp + [num] not in ans:
                        ans.append(tmp + [num])
                elif t > num:
                    stack.append((tmp + [num], i, t - num))

        return ans
