class Solution(object):
    def getNextOne(self, s):
        current = s[0]
        count = 0
        res = 
        for c in s:
            if current == c:
                count += 1
            elif current != c:
                res += %d%c % (count, current)
                count = 1
                current = c

        res += %d%c % (count, current)
        return res

    def countAndSay(self, n):
        ans = 1
        for i in range(n - 1):
            ans = self.getNextOne(ans)
        return ans
