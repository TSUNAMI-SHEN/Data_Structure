class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        def robrange(nums):
            n = len(nums)
            dp = [[0]*2 for _ in range(n)]

            dp[0][0] = 0
            dp[0][1] = nums[0]

            for i in range(1, n):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1])
                dp[i][1] = max(dp[i-1][0]+nums[i], dp[i-1][1])

            return max(dp[-1])
        
        # 比较分别不包含头尾的两种情况，取较大值
        ans1 = robrange(nums[1:])
        ans2 = robrange(nums[:-1])
        return max(ans1, ans2)
