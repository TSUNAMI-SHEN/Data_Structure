//最长不含重复字符的子字符串
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> dic;
        int res = 0, tmp = 0, len = s.size(), i;
        for (int j = 0; j < len; j++)
        {
            if(dic.find(s[j]) == dic.end()) i = -1;
            else i = dic.find(s[j])->second;
            dic[s[j]] = j;
            tmp = tmp < j-i ? tmp+1:j-i;
            res = max(res, tmp);
        }
        return res;
    }
};
