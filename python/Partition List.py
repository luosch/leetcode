# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        new_start = h1 = ListNode(0)
        new_mid = h2 = ListNode(0)
        
        while head:
            if head.val < x:
                h1.next = head
                h1 = h1.next
            else:
                h2.next = head
                h2 = h2.next
            head = head.next
        
        h2.next = None
        h1.next = new_mid.next
        
        return new_start.next
