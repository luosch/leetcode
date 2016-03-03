class Solution {
public:
    int maxProduct(vector<string>& words) {
        int n = words.size(), answer = 0;
        vector<int> mask(n, 0);
        
        // sort(words.begin(), words.end(), helper);
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < words[i].length(); j++) {
                mask[i] |= 1 << (words[i][j] - 'a');
            }
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (!(mask[i] & mask[j])) {
                    int tmp = words[i].length() * words[j].length();
                    answer = max(tmp, answer);
                }
            }
        }
        return answer;
    }
    
    static bool helper(string a, string b) {
        return a.length() < b.length();
    }
};
