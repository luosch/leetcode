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
    vector<int> inorderTraversal(TreeNode* root) {
        res.clear();
        helper(root);
        return res;
    }
    
    void helper(TreeNode *root) {
        if (root == NULL) {
            return;
        }
        helper(root->left);
        res.push_back(root->val);
        helper(root->right);
    }
};
