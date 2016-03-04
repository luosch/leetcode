/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == NULL || head->next == NULL) {
            return head;
        }
        ListNode *dummy = new ListNode(-1);
        ListNode *p = head, *q = head, *r = head->next;
        
        while (r) {
            q = r;
            r = r->next;
            q->next = p;
            p = q;
        }
        head->next = NULL;
        return p;
    }
};
