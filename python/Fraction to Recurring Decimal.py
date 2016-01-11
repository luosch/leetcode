class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        negative = numerator * denominator < 0
        n, d = abs(numerator), abs(denominator)
        
        if n == 0:
            return '0'
        if d == 0:
            return '-2147483648' if negative else '2147483648'
        if n % d == 0:
            return '-' + str(n / d) if negative else str(n / d)

        answer, num_dict = str(n / d) + '.', collections.defaultdict(int)
        pos = len(answer)
        n %= d

        while n:
            if num_dict[n]: 
                answer = '%s(%s)' % (answer[:num_dict[n]], answer[num_dict[n]:])
                break
            num_dict[n] = pos
            pos += 1
            answer += str(n * 10 / d)
            n = n * 10 % d

        return '-' + answer if negative else answer
