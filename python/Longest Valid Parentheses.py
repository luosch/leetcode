class Solution(object):
    def longestValidParentheses_dp(self, s):
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            j = i - 2 - dp[i - 1]
            if s[i - 1] == '(' or j < 0 or s[j] == ')':
                dp[i] = 0
            else:
                dp[i] = dp[i - 1] + 2 + dp[j]
        return max(dp)
    
    def longestValidParentheses(self, s):
        answer = 0
        stack = []

        for i, c in enumerate(s):
            if c == ')' and stack and s[stack[-1]] == '(':
                stack.pop()
                if not stack:
                    answer = i + 1
                else:
                    answer = max(answer, i - stack[-1])
            else:
                stack.append(i)
        
        return answer
