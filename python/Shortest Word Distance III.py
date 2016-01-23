class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        pos_1 = pos_2 = -1
        pos = []
        ans = 0x7fffffff
        
        if word1 == word2:
            for i in range(len(words)):
                if words[i] == word1:
                    pos.append(i)
            return min([pos[i] - pos[i - 1] for i in range(1, len(pos))])
        else:
            for i in range(len(words)):
                if words[i] == word1:
                    pos_1 = i
                if words[i] == word2:
                    pos_2 = i
                if pos_1 != -1 and pos_2 != - 1:
                    ans = min(ans, abs(pos_1 - pos_2))
            return ans
