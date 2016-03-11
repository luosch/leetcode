class Solution {
public:
    bool used[1000];
    vector<int> num;
    int n;
    vector<vector<int>> answer;
    vector<vector<int>> permute(vector<int>& nums) {
        n = nums.size();
        num = nums;
        for (int i = 0; i < n; i++) {
            used[i] = false;
        }
        
        for (int i = 0; i < n; i++) {
            if (!used[i]) {
                vector<int> list;
                list.push_back(i);
                used[i] = true;
                helper(i, list);
                list.pop_back();
                used[i] = false;
            }
        }
        return answer;
    }
    
    void helper(int x, vector<int> &list) {
        if (list.size() == n) {
            vector<int> tmp;
            for (int i = 0; i < n; i++) {
                tmp.push_back(num[list[i]]);
            }
            answer.push_back(tmp);
            return;
        }
        for (int i = 0; i < n; i++) {
            if (!used[i]) {
                used[i] = true;
                list.push_back(i);
                helper(i, list);
                list.pop_back();
                used[i] = false;
            }
        }
    }
};
