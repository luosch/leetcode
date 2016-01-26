class Solution(object):
    def minCost(self, costs):
        n = len(costs)
        if n == 0:
            return 0
            
        paint_red, paint_blue, paint_green = tuple(costs[0])
        
        for i in range(1, n):
            tmp_red = min(paint_blue, paint_green) + costs[i][0]
            tmp_blue = min(paint_red, paint_green) + costs[i][1]
            tmp_green = min(paint_blue, paint_red) + costs[i][2]
            paint_red, paint_blue, paint_green = tmp_red, tmp_blue, tmp_green
        
        return min(paint_red, paint_blue, paint_green)
