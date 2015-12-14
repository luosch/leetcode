# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        fast, slow = head.next, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        
        tmp, cur = None, slow.next
        slow.next = None
        while cur:
            next = cur.next
            cur.next = tmp
            tmp = cur
            cur = next
        
        p = head
        while tmp:
            next1, next2 = p.next, tmp.next
            p.next = tmp
            tmp.next = next1
            p, tmp = next1, next2
