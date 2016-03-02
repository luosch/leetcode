class Solution {
public:
    bool containsDuplicate_slow(vector<int>& nums) {
        set<int> s;
        for (int i = 0; i < nums.size(); i++) {
            if (s.find(nums[i]) != s.end()) {
                return true;
            }
            s.insert(nums[i]);
        }
        return false;
    }
    
    bool containsDuplicate(vector<int>& nums) {
        int max = -0x7fffffff, min = 0x7fffffff;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > max) {
                max = nums[i];
            }
            if (nums[i] < min) {
                min = nums[i];
            }
        }
        vector<bool> hash(max - min + 1, false);
        for (int i = 0; i < nums.size(); i++) {
            if (hash[nums[i] - min] == true) {
                return true;
            }
            hash[nums[i] - min] = true;
        }
        
        return false;
    }
};
