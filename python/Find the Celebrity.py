# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        celebrity = 0
        for i in range(1, n):
            if knows(celebrity, i):
                celebrity = i
        
        for i in range(n):
            if i != celebrity:
                if not knows(i, celebrity) or knows(celebrity, i):
                    celebrity = -1
                    break
        
        return celebrity
        
    def findCelebrity_slow(self, n):
        answer = -1
        for celebrity in range(n):
            know = True
            for i in range(n):
                if i != celebrity:
                    if not knows(i, celebrity) or knows(celebrity, i):
                        know = False
                        break
            if know:
                answer = celebrity
                break
        return answer
