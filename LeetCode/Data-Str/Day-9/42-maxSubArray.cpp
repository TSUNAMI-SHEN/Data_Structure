//连续子数组的最大和
//动态规划解题，需要有两层比较，第一层是第n项如果大于0，则最大和累加上；第二层比较累加和跟当前项的大小（可能累加项是负的）
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int pre = 0;
        int maxV = nums[0];
        for (const auto &x : nums)
        {
            pre = max(x, pre+x);
            maxV = max(pre, maxV);
        }
        return maxV;
    }
};
