class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ret1;
        if (n < 1)
            return ret1;

        vector<vector<int>> ret(n, vector<int>(n, 0));
        int total = n * n;
        int i = 0, j = 0, element = 1;
        int rightBound = n - 1;
        int downBound  = n - 1;
        int leftBound  = 0;
        int upBound    = 0;

        while(element <= total)
        {
            //toward right
            if (upBound != 0)
            {
                i++;
                j++;
            }
            for (; j <= rightBound && element <= total; j++)
                ret[i][j] = element++;
            upBound++;//update upBound

            //toward down
            j--;
            i++;
            for (; i <= downBound && element <= total; i++)
                ret[i][j] = element++;
            rightBound--;//update rightBound

            //toward left
            i--;
            j--;
            for (; j >= leftBound && element <= total; j--)
                ret[i][j] = element++;
            downBound--;//update downBound

            //toward up
            j++;
            i--;
            for (; i >= upBound && element <= total; i--)
                ret[i][j] = element++;
            leftBound++;//update leftBound
        }

        return ret;
    }
};
