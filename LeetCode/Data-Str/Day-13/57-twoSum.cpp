//和为s的两个数字
//双指针，利用nums递增的特点，指针往中间移动，若两个和大于target，则左指针往右移动，若两个和小于target，则右指针往左移动
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i = 0, j = nums.size() - 1;
        while (i < j)
        {
            if(nums[i] + nums[j] > target)   j--;
            else if (nums[i] + nums[j] < target)    i++;
            else return {nums[i], nums[j]};
        }
        return {};
    }
};
