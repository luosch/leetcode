class Solution(object):
    def longestConsecutive(self, nums):
        num_set, ans = set(nums), 0
    
        for num in nums:
            if num not in num_set:
                continue
            
            left, right, tmp = num - 1, num + 1, 1
            
            while left in num_set:
                num_set.remove(left)
                left -= 1
                tmp += 1
            
            while right in num_set:
                num_set.remove(right)
                right += 1
                tmp += 1
            
            ans = max(ans, tmp)
        
        return ans
