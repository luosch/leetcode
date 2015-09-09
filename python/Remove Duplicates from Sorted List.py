# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return None
        
        current = head
        cursor = head.next
        while cursor:
            if cursor.val == current.val:
                current.next = None
                current.next = cursor.next
                cursor = current
            else:
                current = cursor
            cursor = cursor.next
                
        return head
