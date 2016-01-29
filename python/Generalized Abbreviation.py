class Solution(object):
    def generateAbbreviations(self, word):
        result = []
        def dfs(word, item=''):
            if not word:
                result.append(item)
            for i in range(1, len(word) + 1):
                if not item or item[-1].isalpha():
                    dfs(word[i:], item + str(i))
                if not item or item[-1] in '0123456789':
                    dfs(word[i:], item + word[:i])
        
        dfs(word)
        return result
