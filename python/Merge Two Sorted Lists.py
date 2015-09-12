# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        
        answer = ListNode(0)
        if l1.val < l2.val:
            answer.val = l1.val
            l1 = l1.next
        else:
            answer.val = l2.val
            l2 = l2.next

        head = answer

        while l1 or l2:
            head.next = ListNode(0)
            head = head.next
            if l1 and l2:
                if l1.val < l2.val:
                    head.val = l1.val
                    l1 = l1.next
                else:
                    head.val = l2.val
                    l2 = l2.next
            elif l1 and not l2:
                head.val = l1.val
                l1 = l1.next
            elif l2 and not l1:
                head.val = l2.val
                l2 = l2.next

        return answer
