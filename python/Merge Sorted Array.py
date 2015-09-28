class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i, j = 0, 0
        for j in range(n):
            while i < m + j and nums2[j] > nums1[i]:
                i += 1
            nums1.insert(i, nums2[j])
            if i == m + j:
                break
        nums1[m+j+1:] = nums2[j+1:]
