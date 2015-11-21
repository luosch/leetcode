# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindromeNaive(self, head):
        values = []
        cursor = head
        while cursor:
            values.append(cursor.val)
            cursor = cursor.next
        n = len(values)
        for i in range(n // 2):
            if values[i] != values[n - 1 - i]:
                return False
        return True
    
    def isPalindrome(self, head):
        if head is None:
            return True
        # find mid node
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # reverse second half
        cursor, last = slow.next, None
        while cursor:
            next = cursor.next
            cursor.next = last
            last, cursor = cursor, next
        # check palindrome
        p1, p2 = last, head
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next
        # resume linked list(optional)
        p, last = last, None
        while p:
            next = p.next
            p.next = last
            last, p = p, next
        slow.next = last
        return p1 is None
