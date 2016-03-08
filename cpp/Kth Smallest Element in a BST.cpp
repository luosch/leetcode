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
    int count;

    int kthSmallest(TreeNode* root, int k) {
        res.clear();
        count = k;
        helper(root);
        return res[k - 1];
    }
    
    void helper(TreeNode* root) {
        if (root == NULL) {
            return;
        }
        if (res.size() < count) {
            helper(root->left);
            res.push_back(root->val);
            helper(root->right);
        }
    }
};
