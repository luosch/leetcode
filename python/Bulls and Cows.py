class Solution(object):
    def getHint(self, secret, guess):
        from collections import Counter
        secret_map = Counter(secret)

        n = len(secret)
        bulls = cows = 0
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
                secret_map[secret[i]] -= 1
        for i in range(n):
            if secret[i] != guess[i] and guess[i] in secret_map and secret_map[guess[i]] > 0:
                cows += 1
                secret_map[guess[i]] -= 1
        
        return '%dA%dB' % (bulls, cows)
