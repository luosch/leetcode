class Solution {
public:
    string intToRoman(int num) {
        vector<int> numbers(13);
        vector<string> strings(13);

        numbers[0] = 1;
        strings[0] = "I";

        numbers[1] = 4;
        strings[1] = "IV";

        numbers[2] = 5;
        strings[2] = "V";

        numbers[3] = 9;
        strings[3] = "IX";

        numbers[4] = 10;
        strings[4] = "X";

        numbers[5] = 40;
        strings[5] = "XL";

        numbers[6] = 50;
        strings[6] = "L";

        numbers[7] = 90;
        strings[7] = "XC";

        numbers[8] = 100;
        strings[8] = "C";

        numbers[9] = 400;
        strings[9] = "CD";

        numbers[10] = 500;
        strings[10] = "D";

        numbers[11] = 900;
        strings[11] = "CM";

        numbers[12] = 1000;
        strings[12] = "M";

        int number = num;
        string result;
        int i;
        for(i=12; i>=0; i--)
        {
            while(number>=numbers[i])
            {
                result = result + strings[i];
                number = number - numbers[i];
            }
        }

        return result;
    }
};
