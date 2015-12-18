class Solution(object):
    def largestRectangleArea(self, height):
        height.append(0)
        stack, answer = [-1], 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                answer = max(answer, h * w)
            stack.append(i)
        return answer
