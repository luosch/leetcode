class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n <= 0) {
            return false;
        }
        return (int)(pow(3, 19)) % n == 0;
    }
};
