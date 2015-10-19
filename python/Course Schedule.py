class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        ind = [[] for i in range(numCourses)]
        outd = [0] * numCourses
        for p in prerequisites:
            outd[p[0]] += 1
            ind[p[1]].append(p[0])
        dq = collections.deque()
        for i in range(numCourses):
            if outd[i] == 0:
                dq.append(i)
        
        selected = 0
        while dq:
            x = dq.popleft()
            selected += 1
            for i in ind[x]:
                outd[i] -= 1
                if outd[i] == 0:
                    dq.append(i)
        return selected == numCourses
