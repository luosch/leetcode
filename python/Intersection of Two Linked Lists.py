# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        len_A, len_B = 0, 0
        cursor_A, cursor_B = headA, headB
        # find len_a and len_b
        cursor = headA
        while cursor:
            len_A += 1
            cursor = cursor.next
        
        cursor = headB
        while cursor:
            len_B += 1
            cursor = cursor.next
        
        if len_A > len_B:
            delta = len_A - len_B
            while delta > 0:
                cursor_A = cursor_A.next
                delta -= 1
        elif len_B > len_A:
            delta = len_B - len_A
            while delta > 0:
                cursor_B = cursor_B.next
                delta -= 1
        
        while cursor_A and cursor_B:
            if cursor_A == cursor_B:
                return cursor_A
            else:
                cursor_A = cursor_A.next
                cursor_B = cursor_B.next
        
        return None
