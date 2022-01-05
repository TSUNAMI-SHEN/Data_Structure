// 0~n-1中缺失的数字
//利用二分查找，左子数组中必然有nums[m]=m
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int i = 0, j = nums.size() - 1;
        while(i<=j)
        {
            int m = i + (j - i) / 2;
            if(nums[m] == m)
            {
                i = m + 1;
            }
            else
            {
                j = m - 1;
            }
        }
        return i;
    }
};
