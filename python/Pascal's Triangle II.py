class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
    
        ans = [[1]]
        for i in range(1, rowIndex + 1):
            tmp = [1]
            for j in range(i - 1):
                tmp.append(ans[i - 1][j] + ans[i - 1][j + 1])
            tmp.append(1)
            ans.append(tmp)
        
        return ans[-1]
