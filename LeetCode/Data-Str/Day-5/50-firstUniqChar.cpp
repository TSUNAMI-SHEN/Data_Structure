//第一个只出现一次的字符
//哈希表
class Solution {
public:
    char firstUniqChar(string s) {
        unordered_map<char, bool> dic;
        for (char c : s)
            dic[c] = dic.find(c) == dic.end();
        for (char c : s)
            if(dic[c]) return c;
        return ' ';
    }
};
