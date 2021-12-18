// 利用异或运算
// 异或运算：两个值相同时返回0，两个值不同时返回1
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ret = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            ret = ret ^ nums[i];
        }
        return ret;
    }
};
