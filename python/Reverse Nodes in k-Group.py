# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, pre, next):
        last = pre.next
        cur = last.next
        while cur != next:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        return last
        
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        count = 0
        pre = dummy
        
        while head != None:
            count += 1
            if count % k == 0:
                pre = self.reverse(pre, head.next)
                head = pre.next
            else:
                head = head.next
        
        return dummy.next
