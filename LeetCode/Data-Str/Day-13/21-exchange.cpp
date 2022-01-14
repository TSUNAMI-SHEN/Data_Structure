//调整数组顺序使奇数位于偶数前面
//双指针，分类问题，将奇数放在前面，偶数放在后面，可以设置头尾指针，交换实现
class Solution {
public:
    vector<int> exchange(vector<int>& nums) {
        int i = 0, j = nums.size() - 1;
        while(i < j)
        {
            while(i < j && nums[i] % 2 == 1) i++;
            while(i < j && nums[j] % 2 == 0) j--;
            swap(nums[i], nums[j]);
        }
        return nums;
    }
};
