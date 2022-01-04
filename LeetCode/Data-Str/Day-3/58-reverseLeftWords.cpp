//三次翻转实现左转操作
class Solution {
public:
    string reverseLeftWords(string s, int n) {
        // return s.substr(n, s.size()) + s.substr(0, n);
        reverseString(s, 0, n-1);
        reverseString(s, n, s.size()-1);
        reverseString(s, 0, s.size()-1);
        return s;
    }
private:
    void reverseString(string& s, int i, int j){
        while(i < j){
            swap(s[i++], s[j--]);
        }
    }
};
