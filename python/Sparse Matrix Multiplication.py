class Solution(object):
    def multiply(self, A, B):
        M, N, P = len(A), len(A[0]), len(B[0])
        C = [[0] * P for _ in range(M)]
        
        for i in range(M):
            for k in range(N):
                if A[i][k]:
                    for j in range(P):
                        C[i][j] += A[i][k] * B[k][j]
        
        return C
