class Solution {
public:
    vector<string> answer;
    vector<string> generateParenthesis(int n) {
        helper(, n, n);
        return answer;
    }
    
    void helper(string str, int left, int right) {
        if (right < left) {
            return;
        }
        if (left == 0 && right == 0) {
            answer.push_back(str);
        }
        
        if (left > 0) {
            helper(str + '(', left - 1, right);
        }
        if (right > 0) {
            helper(str + ')', left, right - 1);
        }
    }
};
