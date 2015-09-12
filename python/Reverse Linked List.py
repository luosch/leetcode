# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        if not head:
            return None

        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        values.reverse()
        
        new_list_head = ListNode(values[0])
        cursor = new_list_head

        for i in range(1, len(values)):
            cursor.next = ListNode(values[i])
            cursor = cursor.next
            
        return new_list_head
