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
    ListNode* sortList(ListNode* head) {
        if (head == NULL) {
            return head;
        }
        int count = 0;
        ListNode *tmp = head;
        while (tmp) {
            tmp = tmp->next;
            count++;
        }
        return mergeSort(head, count);
    }
    
    ListNode* mergeSort(ListNode *head, int len) {
        if (len == 1) {
            head->next = NULL;
            return head;
        }
        ListNode *mid = head;
        for (int i = 0; i < len / 2; i++) {
            mid = mid->next;
        }
        ListNode *left = mergeSort(head, len / 2);
        ListNode *right = mergeSort(mid, len - (len / 2));
        return merge(left, right);
    }
    
    ListNode* merge(ListNode *leftHead, ListNode *rightHead) {
        ListNode *cursor, *head;
        if (leftHead && rightHead) {
            if (leftHead->val < rightHead->val) {
                cursor = leftHead;
                head = cursor;
                leftHead = leftHead->next;
            } else {
                cursor = rightHead;
                head = cursor;
                rightHead = rightHead->next;
            }
        } else if (leftHead == NULL) {
            return rightHead;
        } else if (rightHead == NULL) {
            return leftHead;
        }
        
        while (leftHead && rightHead) {
            if (leftHead->val < rightHead->val) {
                cursor->next = leftHead;
                cursor = cursor->next;
                leftHead = leftHead->next;
            } else {
                cursor->next = rightHead;
                cursor = cursor->next;
                rightHead = rightHead->next;
            }
        }
        if (leftHead == NULL) {
            cursor->next = rightHead;
        } else if (rightHead == NULL) {
            cursor->next = leftHead;
        }

        return head;
    }
};
