class Solution(object):
    answer = []
    def dfs(self, s, lastList):
        if len(lastList) == 4:
            if len(s) == 0:
                self.answer.append(..join(lastList))
        elif len(lastList) > 4:
            return

        if len(s) >= 1:
            tmp = lastList[:]
            tmp.append(s[:1])
            self.dfs(s[1:], tmp)

        if len(s) >= 2 and s[0] != 0:
            tmp = lastList[:]
            tmp.append(s[:2])
            self.dfs(s[2:], tmp)

        if len(s) >= 3 and s[0] != 0 and s[:3] <= 255:
            tmp = lastList[:]
            tmp.append(s[:3])
            self.dfs(s[3:], tmp)

    def restoreIpAddresses(self, s):
        self.answer = []
        if len(s) > 12:
            return []
        self.dfs(s, [])
        return self.answer
