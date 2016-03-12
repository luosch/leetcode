class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int dp[500+10][500+10] = {0};
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        
        for (int len = 2; len < nums.size(); len++) {
            for (int left = 0; left + len < nums.size(); left++) {
                int right = left + len;
                for (int k = left + 1; k < right; k++) {
                    int tmp = nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right];
                    dp[left][right] = max(dp[left][right], tmp);
                }
            }
        }
        
        return dp[0][nums.size() - 1];
    }
};
