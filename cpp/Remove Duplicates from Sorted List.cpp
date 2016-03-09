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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *cursor = head;
        while (cursor && cursor->next) {
            if (cursor->val == cursor->next->val) {
                ListNode *tmp = cursor->next;
                cursor->next = cursor->next->next;
                delete tmp;
            } else {
                cursor = cursor->next;
            }
        }
        return head;
    }
};
