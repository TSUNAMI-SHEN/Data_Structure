//53-在排序数组中查找数字-I
//普通遍历，计数
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int count = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == target)
            {
                count++;
            }
        }
        return count;
    }
};

//二分查找，寻找target-1和target的右边界，两者相减即target元素的数量
class Solution {
public:
    int search(vector<int>& nums, int target) {
        return helper(nums, target) - helper(nums, target-1);
    }
private:
    int helper(vector<int>& nums, int tar){
        int i = 0, j = nums.size() - 1;
        while(i <= j)
        {
            int m = (i + j) / 2;
            if (nums[m] <= tar)
            {
                i = m + 1;
            }
            else
            {
                j = m - 1;
            }
        }
        return j;
    }
};
