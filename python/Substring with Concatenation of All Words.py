class Solution(object):
    def findSubstring(self, s, words):
        word_dict = collections.defaultdict(int)
        for word in words:
            word_dict[word] += 1
        
        word_len, word_count, ans = len(words[0]), len(words), list()
        
        for i in range(len(s) + 1 - word_len * word_count):
            tmp = word_dict.copy()
            j = 0
            
            while j < word_count:
                word = s[i + j * word_len:i + j * word_len + word_len]
                if word not in tmp:
                    break
                tmp[word] -= 1
                if tmp[word] < 0:
                    break
                j += 1
                
            if j == word_count:
                ans.append(i)
        
        return ans
