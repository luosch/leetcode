# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next

        # reverse the [m, n] nodes
        reverseHead = None
        cursor = pre.next
        for i in range(n - m + 1):
            next = cursor.next
            cursor.next = reverseHead
            reverseHead = cursor
            cursor = next

        pre.next.next = cursor
        pre.next = reverseHead

        return dummyNode.next
