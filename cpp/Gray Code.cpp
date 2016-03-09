class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result(1, 0);
        /** level-by-level expand the result **/
        /** add 1 to prefix of each int the previous layer ***/
        for (int i = 0; i < n; i++) {
            int cur = result.size();
            while (cur) {
                cur--;
                int temp = result[cur];
                temp += (1<<i);
                result.push_back(temp);
            }
        }
        return result;
    }
};
