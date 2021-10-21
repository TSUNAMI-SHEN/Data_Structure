//求两数和
//Method-1，暴力枚举
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    for (int i = 0; i < nums.size(); i++)
    {
        for (int j = i + 1; j < nums.size(); j++)
        {
            if (nums[i] + nums[j] == target)
            {
                return {i, j};
            }
        }
    }
    return {};
    }
};


//Method-2，哈希表
