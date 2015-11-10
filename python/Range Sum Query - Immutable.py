class NumArray(object):
    sum = None
    def __init__(self, nums):
        if len(nums) <= 0:
            return
        self.sum = [0] * len(nums)
        self.sum[0] = nums[0]
        for i in range(1, len(nums)):
            self.sum[i] = self.sum[i - 1] + nums[i]
        

    def sumRange(self, i, j):
        if i > 0:
            return self.sum[j] - self.sum[i - 1]
        else:
            return self.sum[j]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
