# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        list_len = 0
        cursor = head

        while cursor:
            cursor = cursor.next
            list_len += 1
        
        if list_len == 1:
            return None

        cursor = head
        for i in range(list_len - n - 1):
            cursor = cursor.next
        
        if list_len == n:
            return head.next
        else:
            cursor.next = cursor.next.next
        
        return head
