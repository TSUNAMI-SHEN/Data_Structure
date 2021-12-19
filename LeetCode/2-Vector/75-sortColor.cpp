//颜色分类
//方法1-单指针
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int ptr = 0;
        for (int i = 0; i < n; i++)
        {
            if (nums[i] == 0)
            {
                swap(nums[i], nums[ptr]);
                ++ptr;
            }
        }
        for (int i = ptr; i < n; i++)
        {
            if (nums[i] == 1)
            {
                swap(nums[i], nums[ptr]);
                ++ptr;
            }
        }
    }
};

//方法2-双指针
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int p0 = 0;
        int p1 = 0;
        for (int i = 0; i < n; ++i)
        {
            if (nums[i] == 1)
            {
                swap(nums[i], nums[p1]);
                ++p1;
            }
            else if (nums[i] == 0)
            {
                swap(nums[i], nums[p0]);
                if (p0 < p1)
                {
                    swap(nums[i], nums[p1]);
                }
                ++p0;
                ++p1;
            }
        }
    }
};
