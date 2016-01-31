class Solution(object):
    def minArea(self, image, x, y):
        def binary_search(low, high, check):
            while low < high:
                mid = low + (high - low) / 2
                if check(mid):
                    high = mid
                else:
                    low = mid + 1
            
            return low
        
        top = binary_search(0, x, lambda x: '1' in image[x])
        bottom = binary_search(x, len(image), lambda x: '1' not in image[x])
        left = binary_search(0, y, lambda y: any(row[y] == '1' for row in image))
        right = binary_search(y, len(image[0]), lambda y: all(row[y] == '0' for row in image))
        
        return (bottom - top) * (right - left)
