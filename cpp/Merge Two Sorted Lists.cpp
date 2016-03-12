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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *dummy = new ListNode(-1);
        ListNode *tmp = dummy;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                tmp->next = new ListNode(l1->val);
                l1 = l1->next;
                tmp = tmp->next;
            } else {
                tmp->next = new ListNode(l2->val);
                l2 = l2->next;
                tmp = tmp->next;
            }
        }
        
        while (l1) {
            tmp->next = new ListNode(l1->val);
            l1 = l1->next;
            tmp = tmp->next;
        }
        
        while (l2) {
            tmp->next = new ListNode(l2->val);
            l2 = l2->next;
            tmp = tmp->next;
        }
        
        return dummy->next;
    }
};
