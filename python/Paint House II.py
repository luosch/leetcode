class Solution(object):
    def minCostII_slow(self, costs):
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        
        for i in range(1, n):
            for j in range(k):
                costs[i][j] = min(costs[i - 1][:j] + costs[i - 1][j + 1:]) + costs[i][j]
        
        return min(costs[n - 1])
    
    def minCostII(self, costs):
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        
        cost_min = cost_second = 0
        idx = -1
        
        for i in range(0, n):
            tmp_min = tmp_second = float('inf')
            tmp_idx = -1
            
            for j in range(k):
                if idx == j:
                    costs[i][j] += cost_second
                else:
                    costs[i][j] += cost_min
                
                if costs[i][j] < tmp_min:
                    tmp_second = tmp_min
                    tmp_min = costs[i][j]
                    tmp_idx = j
                elif costs[i][j] < tmp_second:
                    tmp_second = costs[i][j]
            
            cost_min, cost_second, idx = tmp_min, tmp_second, tmp_idx
        
        return cost_min
