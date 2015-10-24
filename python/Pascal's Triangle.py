class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
    
        ans = [[1]]
        for i in range(1, numRows):
            tmp = [1]
            for j in range(i - 1):
                tmp.append(ans[i - 1][j] + ans[i - 1][j + 1])
            tmp.append(1)
            ans.append(tmp)
        
        return ans
