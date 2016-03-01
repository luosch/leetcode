class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int answer = 0, len = nums.size();
        for (int i = 0; i < len; i++) {
            answer ^= nums[i];
        }
        return answer;
    }
};
