class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
        n = (numRows - 1) * 2
        rows = [] * numRows
        
        for i, c in enumerate(s):
            index = i % n
            if index < numRows:
                rows[index] += c
            else:
                rows[n - index] += c
        
        return .join(rows)
