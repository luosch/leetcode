class Solution {
public:
    int romanToInt(string s) {
        std::map<char, int> translate {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
        int lastValue = 0;
        int total = 0;
        for (auto digit : s) {
            auto currentValue = translate[digit];
            if (lastValue < translate[digit]) {
                total += currentValue - 2*lastValue;
            } else {
                total += currentValue;
            }

            lastValue = currentValue;
        }

        return total;
    }
};
