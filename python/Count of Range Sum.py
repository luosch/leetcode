class SegmentTreeNode(object):
    def __init__(self, start, end, val):
        self.start, self.end, self.val = start, end, val
        self.children = []

class SegmentTree(object):
    def __init__(self, nums):
        self.nums = nums
        self.root = self.build(0, len(nums) - 1)
    
    def build(self, left, right):
        if left > right:
            return None
        
        root = SegmentTreeNode(self.nums[left], self.nums[right], 0)
        if left == right:
            return root
        
        root = SegmentTreeNode(self.nums[left], self.nums[right], 0)
        mid = (left + right) / 2
        root.children = filter(None, [self.build(left, mid), self.build(mid + 1, right)])
        return root
        
    def update(self, index, val, root=None):
        root = root or self.root
        if index < root.start or index > root.end:
            return root.val
        elif index == root.start and index == root.end:
            root.val += val
            return root.val
        else:
            root.val = sum([self.update(index, val, c) for c in root.children])
            return root.val
    
    def sum(self, start, end, root=None):
        root = root or self.root
        if end < root.start or start > root.end:
            return 0
        elif start <= root.start and end >= root.end:
            return root.val
        else:
            return sum([self.sum(start, end, c) for c in root.children])
            
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        n = len(nums)
        if n == 0:
            return 0

        num_sum, answer = nums[::], 0
        for i in range(1, n):
            num_sum[i] += num_sum[i - 1]
        
        tmp_sum, answer = num_sum[-1], 0
        num_sum = sorted(list(set(num_sum)))
        
        print num_sum
        tree = SegmentTree(num_sum)
        
        for num in nums[::-1]:
            tree.update(tmp_sum, 1)
            tmp_sum -= num
            answer += tree.sum(lower + tmp_sum, upper + tmp_sum)
        
        return answer
