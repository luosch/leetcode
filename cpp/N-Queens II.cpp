class Solution {
public:
    vector<bool> column;
    vector<bool> rightTop;
    vector<bool> leftTop1;
    vector<bool> leftTop2;
    int size, answer;
    
    int totalNQueens(int n) {
        if (n == 1) {
            return 1;
        }
        size = n;
        answer = 0;
        for (int i = 0; i < n + 1; i++) {
            column.push_back(false);
            leftTop1.push_back(false);
            leftTop2.push_back(false);
        }
        for (int i = 0; i < (n-1) * 2 + 1; i++) {
            rightTop.push_back(false);
        }
        helper(-1, 0);
        return answer;
    }
    
    void helper(int x, int y) {
        if (x >= size - 1) {
            answer++;
            return;
        }
        
        for (int i = 0; i < size; i++) {
            if (column[i] || rightTop[x+1+i]) {
                continue;
            }
            if (i > x+1 && leftTop1[i-(x+1)]) {
                continue;
            }
            if (x+1 >= i && leftTop2[x+1-i]) {
                continue;
            }
        
            column[i] = true;
            rightTop[x+1+i] = true;
            if (i > x+1) {
                leftTop1[i-(x+1)] = true;
            } else {
                leftTop2[x+1-i] = true;
            }
            
            helper(x + 1, i);
            
            column[i] = false;
            rightTop[x+1+i] = false;
            if (i > x+1) {
                leftTop1[i-(x+1)] = false;
            } else {
                leftTop2[x+1-i] = false;
            }
        }
    }
};
