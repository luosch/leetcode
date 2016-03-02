class Solution {
public:
    int maxProfit_slow(vector<int>& prices) {
        int answer = 0, n = prices.size();
        bool hold = false;
        for (int i = 0; i < n - 1; i++) {
            if (hold == false && prices[i] < prices[i + 1]) {
                answer -= prices[i];
                hold = true;
            } else if (hold == true && prices[i] > prices[i + 1]) {
                answer += prices[i];
                hold = false;
            }
        }
        if (hold == true) {
            answer += prices[n - 1];
            hold = false;
        }
        return answer;
    }
    
    int maxProfit(vector<int>& prices) {
        int answer = 0, n = prices.size();
        for (int i = 0; i < n - 1; i++) {
            if (prices[i] < prices[i + 1]) {
                answer += prices[i + 1] - prices[i];
            }
        }
        return answer;
    }
};
