class Solution {
public:
    vector< vector<int> > answer;
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<int> tmp;
        for (int i = 1; i <= 9; i++) {
            tmp.push_back(i);
            helper(i, k - 1, n - i, tmp);
            tmp.pop_back();
        }
        return answer;
    }
    
    void helper(int cur, int count, int target, vector<int> &v) {
        if (count < 0) {
            return;
        }
        if (count == 0) {
            if (target == 0) {
                answer.push_back(v);
            }
            return;
        }
        for (int i = cur + 1; i <= 9; i++) {
            v.push_back(i);
            helper(i, count - 1, target - i, v);
            v.pop_back();
        }
    }
};
