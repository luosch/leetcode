# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if head is None:
            return head
        slow = head
        fast = head.next
        
        while slow and fast:
            if slow == fast:
                slow = slow.next
                while head != slow:
                    head = head.next
                    slow = slow.next
                return head
            else:
                slow = slow.next
                if fast.next:
                    fast = fast.next.next
                else:
                    return None
        
        return None
