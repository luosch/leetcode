# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        if head is None:
            return None
        current = head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        if head.val == val:
            return head.next
        else:
            return head
