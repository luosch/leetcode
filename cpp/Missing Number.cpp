class Solution {
public:
    int missingNumber_slow(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        if (nums[0] != 0) {
            return 0;
        } else {
            for (int i = 1; i < nums.size(); i++) {
                if (nums[i] != nums[i-1] + 1) {
                    return nums[i-1] + 1;
                }
            }
            return nums[nums.size()-1] + 1;
        }
    }
    
    int missingNumber(vector<int>& nums) {
        int sum = 0, n = nums.size();
        for (int i = 0; i < n; i++) {
            sum += nums[i];
        }
        return n * (n+1) / 2 - sum;
    }
};
