import collections
import itertools
class Solution(object):
    def fourSum(self, nums, target):
        two_sum = collections.defaultdict(list)
        result = set()
        
        for (id1, val1), (id2, val2) in itertools.combinations(enumerate(nums), 2):
            two_sum[val1 + val2].append({id1, id2})
        
        for key in two_sum.keys():
            if two_sum[key] and two_sum[target - key]:
                for pair1 in two_sum[key]:
                    for pair2 in two_sum[target - key]:
                        if pair1.isdisjoint(pair2):
                            result.add(tuple(sorted([nums[i] for i in (pair1 | pair2)])))
                
                del two_sum[key]
                if key != target - key:
                    del two_sum[target - key]
        
        return [list(item) for item in result]
