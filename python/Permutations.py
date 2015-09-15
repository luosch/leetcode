class Solution(object):
    answer = None
    used = None
    n = None
    nums = None
    def dfs(self, x, _tmp):
        tmp = copy.copy(_tmp)
        tmp.append(x)
        if len(tmp) == self.n:
            self.answer.append(tmp)
            return
        for num in self.nums:
            if not self.used[num]:
                self.used[num] = True
                self.dfs(num, tmp)
                self.used[num] = False
        
    def permute(self, nums):
        self.used = dict()
        self.nums = nums
        for num in nums:
            self.used[num] = False

        self.n = len(nums)
        self.answer = []
        for num in nums:
            self.used[num] = True
            self.dfs(num, [])
            self.used[num] = False
        return self.answer
