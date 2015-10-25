class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        second_height, area = 0, 0
        while left < right:
            if height[left] > height[right]:
                second_height = max(height[right], second_height)
                area += second_height - height[right]
                right -= 1
            else:
                second_height = max(height[left], second_height)
                area += second_height - height[left]
                left += 1
        return area
