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
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL || head->next == NULL) {
            return head;
        }
        ListNode *cur = head, *prev = NULL;
        ListNode *answer = head->next;
        while (cur && cur->next) {
            ListNode *curNext = cur->next;
            cur->next = cur->next->next;
            curNext->next = cur;
            if (prev) {
                prev->next = curNext;    
            }
            prev = cur;
            cur = cur->next;
        }
        return answer;
    }
};
