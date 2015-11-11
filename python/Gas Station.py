class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        
        keep = 0
        position = 0
        
        # don't need to travel through the circle
        # because it guarante a unique solution
        for i in range(len(gas)):
            keep += gas[i] - cost[i]
            if keep < 0:
                keep = 0
                position = i + 1
        
        return position
