class Solution {
public:
    int findMin(vector<int>& nums) {
        int low = 0, high = nums.size() - 1;
        // while (low < high) {
        //     int mid = low + (high - low) / 2;
        //     if (nums[mid] < nums[low]) {
        //         high = mid;
        //     } else if (nums[mid] > nums[high]) {
        //         low = mid + 1;
        //     } else {
        //         high = mid - 1;
        //     }
        // }
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] < nums[high]) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return nums[low];
    }
};
