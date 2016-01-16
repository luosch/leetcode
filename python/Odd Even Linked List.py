# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if not head:
            return head
        
        odd, even, tmp = head, head.next, head.next
        while odd.next and even.next:
            odd.next = even.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        
        odd.next = tmp
        return head
