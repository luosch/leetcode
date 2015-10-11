class Solution(object):
    def shortestDistance(self, words, word1, word2):
        pos_1 = pos_2 = -1
        ans = 0xffffff
        for i in range(len(words)):
            if words[i] == word1:
                pos_1 = i
            if words[i] == word2:
                pos_2 = i
            if pos_1 != -1 and pos_2 != - 1:
                ans = min(ans, abs(pos_1 - pos_2))

        return ans
