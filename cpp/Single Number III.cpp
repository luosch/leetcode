class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum ^= nums[i];
        }
        int n = sum & (~(sum - 1)), a = 0, b =0;
        for (int i = 0; i < nums.size(); i++) {
            if (n & nums[i]) {
                a ^= nums[i];
            } else {
                b ^= nums[i];
            }
        }
        vector<int> result = {a, b};
        return result;
    }
};
