class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        ans = max_num = min_num = nums[0]

        for num in nums[1:]:
            if num > 0:
                max_num = max(max_num * num, num)
                min_num = min(min_num * num, num)
            else:
                tmp = max_num
                max_num = max(min_num * num, num)
                min_num = min(tmp * num, num)
            ans = max(max_num, ans)
        
        return ans
