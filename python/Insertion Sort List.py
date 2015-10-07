# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            while head and head.next and head.val <= head.next.val:
                head = head.next
            node = head.next
            if not node:
                break
            head.next = node.next  # delete "node"
            pre = dummy 
            while node.val > pre.next.val:
                pre = pre.next 
            node.next = pre.next  # insert "node" in the right position
            pre.next = node
        return dummy.next
