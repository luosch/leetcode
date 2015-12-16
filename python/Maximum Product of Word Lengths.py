class Solution(object):
    def maxProductBS(self, words):
        def findLeft(left, right, val):
            while left < right:
                mid = left + (right - left) // 2
                if mask[mid][0] < val:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def findRight(left, right, val):
            while left < right:
                mid = left + (right - left + 1) // 2
                if mask[mid][0] > val:
                    right = mid - 1
                else:
                    left = mid
            return left

        n, answer, mask = len(words), 0, []
        for i, s in enumerate(words):
            tmp = 0
            for c in s:
                tmp |= 1 << (ord(c) - ord('a'))
            mask.append((tmp, len(s)))

        mask.sort(key=lambda x:x[0])

        for i in range(n - 1, -1, -1):
            val, l = mask[i]
            target = 1
            while target <= val:
                target <<= 1
            target >>= 1
            
            while target:
                while target & val:
                    target >>= 1
                indexRight = findRight(0, i - 1, (target << 1) - 1)
                
                while target and not (target & val):
                    target >>= 1
                indexLeft = findLeft(0, i - 1, target << 1)
                
                for j in range(indexLeft, indexRight + 1):
                    if not val & mask[j][0]:
                        answer = max(answer, l * mask[j][1])

        return answer

    def maxProduct(self, words):
        n, answer = len(words), 0
        mask = [0] * n
        words.sort(key=lambda s: -len(s))

        for i in range(n):
            tmp = 0
            for c in words[i]:
                tmp |= 1 << (ord(c) - ord('a'))
            mask[i] = (tmp, len(words[i]))
        
        for i in xrange(n):
            for j in xrange(i + 1, n):
                if not (mask[i][0] & mask[j][0]):
                    product = mask[i][1] * mask[j][1]
                    if product > answer:
                        answer = product
                    else:
                        break

        return answer
