class Solution {
public:
    int singleNumber(vector<int>& nums) {
        vector<int> bits(32, 0);
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < 32; j++) {
                bits[j] += (nums[i] >> j) & 1;
            }
        }
        int answer = 0;
        for (int j = 0; j < 32; j++) {
            answer += (bits[j] % 3) << j;
        }
        return answer;
    }
};
