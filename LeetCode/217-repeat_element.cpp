//217-存在重复元素
//解题思路：先对向量进行排序，再逐一进行比对
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    for (int i = 0; i < nums.size() - 1; i++)
    {
        if (nums[i] == nums[i+1])
        {
            return true;
        }
    }
    return false;
    }
};
