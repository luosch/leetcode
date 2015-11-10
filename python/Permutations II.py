class Solution(object):
    answer = None
    used = None
    n = None
    nums = None
    def dfs(self, x, tmp):
        if len(tmp) == self.n:
            self.answer.append(tmp[::])
            return
        
        for i in range(self.n):
            if i > 0 and not self.used[i - 1] and self.nums[i] == self.nums[i - 1]:
                continue
            else:
                if not self.used[i]:
                    self.used[i] = True
                    tmp.append(self.nums[i])
                    self.dfs(self.nums, tmp)
                    tmp.pop()
                    self.used[i] = False
        
        
    def permuteUnique(self, nums):
        self.used = [False] * len(nums)
        self.nums = sorted(nums)

        self.n = len(nums)
        self.answer = []

        self.dfs(nums, [])
        return self.answer
