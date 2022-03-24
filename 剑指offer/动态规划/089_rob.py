class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        dp = [[0]*2 for _ in range(n)]  # 二维数组，分别表示第i个房间偷与不偷时的最大偷窃金额

        dp[0][0] = 0
        dp[0][1] = nums[0]

        for i in range(1, n):
            # 分两种情况考虑，即第i个房间偷不偷
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])  # 不偷，则比较前i-1个房间两种情况的最大偷窃金额
            dp[i][1] = max(dp[i-1][0]+nums[i], dp[i-1][1])  # 偷，则比较加上第i个房间的金额与前i-1个房间偷窃金额
        return max(dp[n-1])
