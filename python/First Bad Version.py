# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left, right = 1, n
        while left < right:
            mid = (left + right) >> 1
            if isBadVersion(mid) and not isBadVersion(mid + 1):
                return mid
            elif isBadVersion(mid):
                right = mid
            elif not isBadVersion(mid):
                left = mid + 1
        
        return (left + right) >> 1
