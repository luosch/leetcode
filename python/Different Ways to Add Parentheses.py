class Solution(object):
    def diffWaysToCompute(self, input):
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }
        def helper(left, right):
            ans = []
            for i in range(left, right):
                if input[i] not in ops:
                    continue
                ans.extend([ops[input[i]](l, r) for l in helper(left, i) for r in helper(i + 1, right)])

            print(left, right, ans)
            if len(ans) == 0:
                return [int(input[left:right])]
            else:
                return ans

        return helper(0, len(input))
