class Solution(object):
    def compareVersion(self, version1, version2):
        ver1, ver2 = version1.split(.), version2.split(.)
        
        while len(ver1) < len(ver2):
            ver1.append(0)
        
        while len(ver2) < len(ver1):
            ver2.append(0)
            
        for i in range(len(ver1)):
            v1, v2 = int(ver1[i]), int(ver2[i])
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        
        return 0
