class Solution {
public:
    int maxProfit_1(vector<int>& prices) {
        if (prices.size() <= 1) {
            return 0;
        }
        vector<int> sell(prices.size(), 0);
        vector<int> buy(prices.size(), 0);
        buy[0] = -prices[0];
        buy[1] = -prices[1];
        sell[1] = prices[1] + buy[0];
        
        int answer = max(answer, sell[1]);
        for (int i = 2; i < prices.size(); i++) {
            int delta = prices[i] - prices[i - 1];
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1] + delta);
            buy[i] = max(sell[i - 2] - prices[i], buy[i - 1] - delta);
            answer = max(answer, sell[i]);
        }
        return answer;
    }
    
    int maxProfit(vector<int>& prices) {
        if (prices.size() <= 1) {
            return 0;
        }
        vector<int> sell(prices.size(), 0);
        vector<int> buy(prices.size(), 0);
        buy[0] = -prices[0];
        buy[1] = max(-prices[0], -prices[1]);
        sell[1] = max(buy[0] + prices[1], 0);
        
        for (int i = 2; i < prices.size(); i++) {
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1]);
            buy[i] = max(sell[i - 2] - prices[i], buy[i - 1]);
        }
        return sell[prices.size() - 1];
    }
};
