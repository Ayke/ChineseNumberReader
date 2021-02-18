#include <string>
#include <iostream>
using namespace std;
class Solution {
public:
    int BILLION = 1000000000, MILLION = 1000000, THOUSAND = 1000;
    string readDigit[21] = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                            "Eighteen", "Nineteen", "Twenty"};
    string readTenDig[10] = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    string readNum(int num) {
        string answer;
        if (num >= BILLION) answer = readNum(num / BILLION) + " Billion " + readNum(num % BILLION);
        else if (num >= MILLION) answer = readNum(num / MILLION) + " Million " + readNum(num % MILLION);
        else if (num >= THOUSAND) answer = readNum(num / THOUSAND) + " Thousand " + readNum(num % THOUSAND);
        else if (num >= 100) answer = readDigit[num / 100] + " Hundred " + readNum(num % 100);
        else if (num >= 21) answer = readTenDig[num / 10] + " " + readDigit[num % 10];
        else answer = readDigit[num];
        while (answer.back() == ' ') answer.erase(answer.end()-1);
        // answer = answer.trim();
        return answer;
    }
    
    string numberToWords(int num) {
        if (num == 0) return "Zero";
        return readNum(num);
    }
};

int main() {
    Solution s1;
    cout << "***" << endl << s1.numberToWords(9);
    cout << "***" << endl << s1.numberToWords(10);
    cout << "***" << endl << s1.numberToWords(1313);
    cout << "***" << endl << s1.numberToWords(923214);
    cout << "***" << endl << s1.numberToWords(5000);
    cout << "***" << endl << s1.numberToWords(1003);
    cout << "***" << endl << s1.numberToWords(400);
    cout << "***" << endl << s1.numberToWords(0);
}
