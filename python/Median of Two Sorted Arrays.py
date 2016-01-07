class Solution(object):
    def findMedianSortedArrays_funny(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        n = len(nums)
        return (nums[n / 2] + nums[(n - 1) / 2]) / 2.0
    
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.findKth(nums1, nums2, n / 2)
        else:
            return (self.findKth(nums1, nums2, n / 2 - 1) + self.findKth(nums1, nums2, n / 2)) / 2.0

    def findKth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        if not nums1:
            return nums2[k]

        if k == len(nums1) + len(nums2) - 1:
            return max(nums1[-1], nums2[-1])

        i = len(nums1) / 2
        j = k - i

        if nums1[i] > nums2[j]:
            return self.findKth(nums1[:i], nums2[j:], i)
        else:
            return self.findKth(nums1[i:], nums2[:j], j)
