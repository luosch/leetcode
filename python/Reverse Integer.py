class Solution(object):
    def reverse(self, x):
        if -10 < x < 10:
            return x
        
        n = list(str(x))
        negative = False
        if n[0] == '-':
            negative = True
            n = n[1:]
        
        n.reverse()
        
        if negative:
            n = - + .join(n)
        else:
            n = .join(n)
        n = int(n)
        
        if n > 2147483647 or n < -2147483647:
            return 0

        return n
