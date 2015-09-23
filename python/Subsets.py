class Solution(object):
    numbers = []
    answers = []
    def dfs(self, level, subset):
        selected = subset[:]
        unselected = subset[:]
        selected.append(self.numbers[level])

        if level == len(self.numbers) - 1:
            self.answers.append(unselected)
            self.answers.append(selected)
        else:
            self.dfs(level + 1, unselected)
            self.dfs(level + 1, selected)


    def subsets(self, nums):
        self.answers = []
        self.numbers = sorted(nums)
        self.dfs(0, [])
        return self.answers
