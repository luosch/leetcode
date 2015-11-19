class Solution(object):
    def groupAnagrams(self, strs):
        used, result = {}, []
        for item in strs:
            key = tuple(sorted(item))
            if key not in used:
                used[key] = [item]
            else:
                used[key].append(item)
        
        for key in used:
            result.append(sorted(used[key]))
        
        return result
