class Solution {
public:
    void sortColors_slow(vector<int>& nums) {
        vector<int> count(3, 0);
        for (int i = 0; i < nums.size(); i++) {
            count[nums[i]]++;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (count[0] > 0) {
                nums[i] = 0;
                count[0]--;
            } else if (count[1] > 0) {
                nums[i] = 1;
                count[1]--;
            } else if (count[2] > 0) {
                nums[i] = 2;
                count[2]--;
            }
        }
    }
    
    void sortColors(vector<int>& nums) {
        int left = 0, right = nums.size() - 1, zero = 0;
        while (left <= right) {
            if (nums[left] == 0) {
                nums[left] = nums[zero];
                nums[zero] = 0;
                zero++;
                left++;
            } else if (nums[left] == 1) {
                left++;
            } else if (nums[left] == 2) {
                nums[left] = nums[right];
                nums[right] = 2;
                right--;
            }
        }
    }
};
