class Solution(object):
    def getPermutation(self, n, k):
        answer, nums = '', [str(i) for i in xrange(1, n + 1)]
        for i in xrange(n - 1, -1, -1):
            index, k = (k - 1) // math.factorial(i), k % math.factorial(i)
            answer += nums[index]
            del nums[index]
        return answer
