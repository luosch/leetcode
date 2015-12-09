# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        if not head:
            return head
        cur, count = head, 0
        while cur:
            cur = cur.next
            count += 1
        return self.mergeSort(head, count)[0]

    def mergeSort(self, head, k):
        if k == 1:
            next = head.next
            head.next = None
            return head, next
        else:
            leftHead, next = self.mergeSort(head, k // 2)
            rightHead, next = self.mergeSort(next, k - (k // 2))
            return self.merge(leftHead, rightHead), next
    
    def merge(self, h1, h2):
        dummy = ListNode(0)
        cur = dummy
        while h1 and h2:
            if h1.val <= h2.val:
                cur.next = h1
                cur = cur.next
                h1 = h1.next
            else:
                cur.next = h2
                cur = cur.next
                h2 = h2.next
        if not h1 and h2:
            cur.next = h2
        elif not h2 and h1:
            cur.next = h1
        return dummy.next
