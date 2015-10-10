class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        answer1 = 999999
        answer2 = -999999
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                delta = tmp - target
                if delta > 0:
                    right -= 1
                    answer1 = min(answer1, delta)
                elif delta < 0:
                    left += 1
                    answer2 = max(answer2, delta)
                elif delta == 0:
                    return target
        
        if answer1 < abs(answer2):
            return target + answer1
        else:
            return target + answer2
