//C++原地修改，由于替换空格会导致字符串长度改变，所以需要先对空格进行统计，然后修改长度，再倒序遍历进行替换
class Solution {
public:
    string replaceSpace(string s) {
        int count = 0, len = s.size();
        for (int i = 0; i < len; i++){
            if (s[i] == ' '){
                count++;
            }
        }
        s.resize(len + 2 * count);
        for (int i = len - 1, j = s.size() - 1; i < j; i--, j--){
            if(s[i] != ' '){
                s[j] = s[i];
            }
            else{
                s[j] = '0';
                s[j-1] = '2';
                s[j-2] = '%';
                j = j - 2;
            }
        }
        return s;
    }
};
