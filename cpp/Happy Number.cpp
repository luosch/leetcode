class Solution {
public:
    bool isHappy(int n) {
        do {
            int sum = 0;
            while (n > 0) {
                sum += (n%10) * (n%10);
                n /= 10;
            }
            n = sum;
        } while (n > 9);
        return n == 1;
    }
};
