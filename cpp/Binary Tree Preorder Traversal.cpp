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
    vector<int> res;
    vector<int> preorderTraversal(TreeNode* root) {
        helper(root);
        return res;
    }
    void helper(TreeNode* root) {
        if (root == NULL) {
            return;
        }
        res.push_back(root->val);
        helper(root->left);
        helper(root->right);
    }
};
