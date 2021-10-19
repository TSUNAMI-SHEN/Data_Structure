//求最大子序和
//采用动态规划的方法，减而治之
//递推方程：f(i) = max{f(i-1)+nums[i], nums[i]}
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
    int maxV = nums[0];
    int pre = 0;
    for (const auto &x: nums)
    {
        pre = max(pre+x, x);
        maxV = max(pre, maxV);
    }
    return maxV;
    }
};
