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
    vector<int> vals;
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        vals = nums;
        return helper(0, nums.size() - 1);
    }
    
    TreeNode* helper(int low, int high) {
        if (low > high) {
            return NULL;
        } else if (low == high) {
            TreeNode *node = new TreeNode(vals[low]);
            return node;
        }
        
        int mid = (low + high) / 2;
        TreeNode *root = new TreeNode(vals[mid]);
        root->left = helper(low, mid - 1);
        root->right = helper(mid + 1, high);
        
        return root;
    }
};
