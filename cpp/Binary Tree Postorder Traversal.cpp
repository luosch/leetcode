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
    vector<int> postorderTraversal(TreeNode* root) {
        if (root == NULL) {
            return vector<int>();
        }
        vector<int> answer;
        stack<TreeNode*> st;
        
        while (!st.empty() || root != NULL) {
            if (root) {
                st.push(root);
                answer.push_back(root->val);
                root = root->right;
                continue;
            } else {
                root = st.top()->left;
                st.pop();
            }
        }
        
        reverse(answer.begin(), answer.end());
        return answer;
    }
    
    
    vector<int> answer;
    vector<int> postorderTraversal_rec(TreeNode* root) {
        helper(root);
        return answer;
    }
    
    void helper(TreeNode *root) {
        if (root == NULL) {
            return;
        }
        helper(root->left);
        helper(root->right);
        answer.push_back(root->val);
    }
};
