class Solution(object):
    def isValidSudoku(self, board):
        rows = [None] * 9
        cols = [None] * 9
        blocks = [None] * 9
        
        for i in range(9):
            rows[i] = set()
            cols[i] = set()
            blocks[i] = set()
        
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == '.':
                    continue
                b = (i // 3) * 3 + j // 3
                if x in rows[i] or x in cols[j] or x in blocks[b]:
                    return False
                else:
                    rows[i].add(x)
                    cols[j].add(x)
                    blocks[b].add(x)
        
        return True
