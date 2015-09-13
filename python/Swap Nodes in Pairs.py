# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        answer = head.next
        cursor = head
        prev = None
        
        while cursor and cursor.next:
            tmp = cursor.next
            cursor.next = cursor.next.next
            tmp.next = cursor
            if prev: prev.next = tmp
            prev = cursor
            cursor = cursor.next
        
        return answer
