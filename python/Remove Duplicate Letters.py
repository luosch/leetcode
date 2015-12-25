class Solution(object):
    def removeDuplicateLetters(self, s):
        counter = collections.Counter(s)
        used, stack = set(), []
        for c in s:
            counter[c] -= 1
            if c in used:
                continue
            while stack and stack[-1] > c and counter[stack[-1]]:
                used.remove(stack.pop())
            used.add(c)
            stack.append(c)
        return ''.join(stack)
