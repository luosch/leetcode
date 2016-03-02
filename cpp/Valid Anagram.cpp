class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        int len = s.length();
        vector<int> countS(26, 0), countT(26, 0);
        for (int i = 0; i < len; i++) {
            countS[s[i] - 'a'] += 1;
            countT[t[i] - 'a'] += 1;
        }
        
        for (int i = 0; i < 26; i++) {
            if (countS[i] != countT[i]) {
                return false;
            }
        }
        
        return true;
    }
};
