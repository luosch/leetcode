class Solution(object):
    def largestNumber(self, nums):
        str_list = [str(num) for num in nums]
        str_list.sort(cmp = lambda a, b: cmp(a + b, b + a), reverse=True)
        return str(int(''.join(str_list)))
