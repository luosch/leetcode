class Solution(object):
    def solve(self, board):
        queue = collections.deque([])
        if board == []:
            return
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                if (r in [0, m - 1] or c in [0, n - 1]) and board[r][c] == "O":
                    queue.append((r, c))
    
        while queue:
            r, c = queue.popleft()
            if 0 <= r < m and 0 <= c< n and board[r][c] == "O":
                board[r][c] = "K"
                queue.append((r - 1, c))
                queue.append((r + 1, c))
                queue.append((r, c - 1))
                queue.append((r, c + 1))
    
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "K":
                    board[r][c] = "O"
