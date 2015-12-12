# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if k < 1 or not head:
            return head
        
        listLen, p = 1, head
        while p.next:
            p = p.next
            listLen += 1
        p.next = head
        
        k = listLen - k % listLen
        while k:
            p = p.next
            k -= 1
        
        head = p.next
        p.next = None
        
        return head
