class Solution {
public:
    int majorityElement(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        int majority = nums[0], count = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == majority) {
                count++;
            } else {
                count--;
                if (count < 0) {
                    majority = nums[i];
                    count = 0;
                }
            }
        }
        return majority;
    }
};
