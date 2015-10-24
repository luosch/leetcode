class Solution(object):
    def combinationSum3(self, k, n):
        stack, ans = [([], 0, n)], []
        
        while stack:
            tmp, index, target = stack.pop()
            if len(tmp) >= k:
                continue
            for i in range(index + 1, 10):
                if target == i and len(tmp) == k - 1:
                    ans.append(tmp + [i])
                elif target > i:
                    stack.append((tmp + [i], i, target - i))
        
        return ans
