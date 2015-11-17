# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cursor = head
        
        while cursor != None:
            while cursor.next != None and pre.next.val == cursor.next.val:
                cursor = cursor.next
            if pre.next == cursor:
                pre = pre.next
            else:
                pre.next = cursor.next
            cursor = cursor.next
        
        return dummy.next
