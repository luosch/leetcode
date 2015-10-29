# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def helper_slow(self, head, tail):
    #     if head == tail:
    #         return None

    #     slow = fast = head

    #     while fast != tail and fast.next != tail:
    #         fast = fast.next.next
    #         slow = slow.next

    #     root = TreeNode(slow.val)
    #     root.left = self.helper(head, slow)
    #     root.right = self.helper(slow.next, tail)
        
    #     return root
    _list = []
    def helper(self, left, right):
        if left == right:
            root = TreeNode(self._list[left])
            return root
        elif left > right:
            return None

        mid = left + (right - left) // 2
        
        root = TreeNode(self._list[mid])
        root.left = self.helper(left, mid - 1)
        root.right = self.helper(mid + 1, right)
        
        return root
        
    def sortedListToBST(self, head):
        self._list, cursor = [], head
        while cursor:
            self._list.append(cursor.val)
            cursor = cursor.next

        return self.helper(0, len(self._list) - 1)
