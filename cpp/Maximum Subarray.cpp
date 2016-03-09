class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        vector<int> dp(nums.size(), 0);
        dp[0] = nums[0];
        int answer = dp[0];
        for (int i = 1; i < nums.size(); i++) {
            dp[i] = max(nums[i], dp[i - 1] + nums[i]);
            answer = max(answer, dp[i]);
        }
        return answer;
    }
};
