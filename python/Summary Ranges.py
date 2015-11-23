class Solution(object):
    def summaryRanges(self, nums):
        start, end, n = 0, 0, len(nums)
        answer = []
        while start < n and end < n:
            if end < n - 1 and nums[end + 1] == nums[end] + 1:
                end += 1
            else:
                if start == end:
                    answer.append('%d' % nums[start])
                else:
                    answer.append('%d->%d' % (nums[start], nums[end]))
                start = end = end + 1
        return answer
