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
    void deleteNode(ListNode* node) {
        ListNode *tmp = node;
        if (node->next != NULL) {
            node->val = node->next->val;
            node->next = node->next->next;
        } else {
            node = NULL;
        }
    }
};
