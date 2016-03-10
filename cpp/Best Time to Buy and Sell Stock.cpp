class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() <= 1) {
            return 0;
        }
        int minBuy = prices[0];
        int answer = 0;
        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] < minBuy) {
                minBuy = prices[i];
            }
            if (prices[i] - minBuy > answer) {
                answer = prices[i] - minBuy;
            }
        }
        return answer;
    }
};
