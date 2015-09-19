class Solution(object):
    def addBinary(self, a, b):
        len_a = len(a)
        len_b = len(b)
        length = max(len_a, len_b)
        c = [0] * (length + 1)
        if len_a < len_b:
            a, b = b, a
            len_a, len_b = len_b, len_a

        for i in range(0, length):
            if len_a - 1 - i >= 0 and len_b - 1 - i >= 0:
                num_a = int(a[len_a - 1 - i])
                num_b = int(b[len_b - 1 - i])
                c[i] += (num_a + num_b)
                c[i + 1] += c[i] / 2
                c[i] %= 2
            elif len_a - 1 - i >= 0 and len_b - 1 - i < 0:
                num_a = int(a[len_a - 1 - i])
                c[i] += num_a
                c[i + 1] += c[i] / 2
                c[i] %= 2
            else:
                break
        
        while len(c) > 1 and c[-1] == 0:
            c.pop()
        
        answer = 
        while c:
            answer += str(c.pop())
        
        return answer
