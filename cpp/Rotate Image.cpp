class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        /**
         * clock rotate : rotate[j][n-1-i]=a[i][j]
         **/
        reverse(matrix.begin(), matrix.end());   /** a[n-1-i][j]=a[i][j] **/
        for(int i=0; i<matrix.size(); i++){   /** a[i][j]=a[j][i] **/
            for(int j=i+1; j<matrix[i].size(); j++)
                swap(matrix[i][j], matrix[j][i]);
        }
    }
};
