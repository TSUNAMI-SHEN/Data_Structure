class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)    # 表示到第i个台阶需要的最少成本
        
        dp[0] = 0   # 第0个台阶
        dp[1] = 0   # 第1个台阶

        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[n]
