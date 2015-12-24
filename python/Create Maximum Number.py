class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        def getMax(nums, t):
            max_nums, size = [], len(nums)
            for x in range(size):
                while max_nums and len(max_nums) + size - x > t and max_nums[-1] < nums[x]:
                    max_nums.pop()
                if len(max_nums) < t:
                    max_nums.append(nums[x])
            return max_nums
        
        def merge(nums1, nums2):
            ans = []
            while nums1 or nums2:
                if nums1 > nums2:
                    ans.append(nums1[0])
                    nums1.pop(0)
                else:
                    ans.append(nums2[0])
                    nums2.pop(0)
            return ans
        
        len1, len2 = len(nums1), len(nums2)
        answer = []
        for x in range(max(0, k - len2), min(k, len1) + 1):
            tmp = merge(getMax(nums1, x), getMax(nums2, k - x))
            answer = max(tmp, answer)
        return answer
