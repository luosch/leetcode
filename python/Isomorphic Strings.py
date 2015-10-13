class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        ds, dt = {}, {}
        
        # for i in xrange(len(s)):
        #     c, d = s[i], t[i]
        #     if c not in ds:
        #         ds[c] = [i]
        #     else:
        #         ds[c].append(i)
                
        #     if d not in dt:
        #         dt[d] = [i]
        #     else:
        #         dt[d].append(i)
        
        for i, c in enumerate(s):
            if c not in ds:
                ds[c] = [i]
            else:
                ds[c].append(i)
        
        for i, c in enumerate(t):
            if c not in dt:
                dt[c] = [i]
            else:
                dt[c].append(i)

        return sorted(ds.values()) == sorted(dt.values())
