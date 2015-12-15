# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        p, carry = dummy, 0
        while l1 or l2 or carry > 0:
            tmp = carry
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            carry = tmp / 10
            tmp = tmp % 10
            p.next = ListNode(tmp)
            p = p.next

        return dummy.next
