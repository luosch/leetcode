from collections import defaultdict
class WordDistance(object):
    def __init__(self, words):
        self.m = defaultdict(list)
        self.n = len(words)
        for i, word in enumerate(words):
            self.m[word].append(i)
        

    def shortest(self, word1, word2):
        ans = self.n
        a, b = self.m[word1], self.m[word2]
        na, nb = len(a), len(b)
        i = j = 0
        while i < na and j < nb:
            if a[i] < b[j]:
                ans = min(ans, b[j] - a[i])
                i += 1
            else:
                ans = min(ans, a[i] - b[j])
                j += 1
        
        return ans
        


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest(word1, word2)
# wordDistance.shortest(anotherWord1, anotherWord2)
