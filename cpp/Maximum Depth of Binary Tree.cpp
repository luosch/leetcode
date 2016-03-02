/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == NULL) {
            return 0;
        } else {
            int leftCount = maxDepth(root->left);
            int rightCount = maxDepth(root->right);
            if (leftCount > rightCount) {
                return leftCount + 1;
            } else {
                return rightCount + 1;
            }
        }
    }
};
