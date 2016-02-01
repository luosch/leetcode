class Solution(object):
    def threeSumSmaller(self, nums, target):
        nums.sort()
        answer = 0
        for i in range(0, len(nums) - 2):
            if 3 * nums[i] >= target:
                return answer
            
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[i] + nums[start] + nums[end] < target:
                    answer += end - start
                    start += 1
                else:
                    end -= 1
        
        return answer
