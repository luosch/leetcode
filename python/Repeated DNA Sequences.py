class Solution(object):
    def findRepeatedDnaSequences(self, s):
        n = len(s)
        if n <= 10:
            return []
        
        answer, dic = [], {}
        
        for start in xrange(10):
            for i in xrange(start, n - 10 + 1, 10):
                word = s[i:i + 10]
                if word in dic and dic[word] == 1:
                    dic[word] += 1
                    answer.append(word)
                elif word not in dic:
                    dic[word] = 1

        return answer
