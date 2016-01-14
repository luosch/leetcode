class SegmentTreeNode(object):
    def __init__(self, start, end, val):
        self.start, self.end, self.val = start, end, val
        self.children = []

class SegmentTree(object):
    def __init__(self, n):
        self.root = self.build(0, n - 1)
    
    def build(self, start, end):
        if start > end:
            return None
        
        root = SegmentTreeNode(start, end, 0)
        if start == end:
            return root
        
        mid = (start + end) / 2
        root.children = filter(None, [self.build(start, mid), self.build(mid + 1, end)])
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
    def countSmaller(self, nums):
        hash_table = {v:i for i, v in enumerate(sorted(set(nums)))}

        tree, ans = SegmentTree(len(hash_table)), []
        for num in nums[::-1]:
            ans.append(tree.sum(0, hash_table[num] - 1))
            tree.update(hash_table[num], 1)
        
        return ans[::-1]
