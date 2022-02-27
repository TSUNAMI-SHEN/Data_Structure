class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])   # 两种情况，1：如果i偷，则i-1不偷，是从i-2的状态下继承；2.如果i不偷，则继承i-1的情况；取两者的最大值
        return dp[-1]
