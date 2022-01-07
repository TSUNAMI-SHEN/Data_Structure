//去除重复的元素，返回去重后数组的长度
//采用双指针的方式
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int p1 = 1, p2 = 1;
        int n = nums.size();
        if (n == 0) return 0;
        while (p1 < n)
        {
            if (nums[p1] != nums[p1-1])
            {
                nums[p2] = nums[p1];
                ++p2;
            }
            ++p1;
        }
        return p2;
    }
};
