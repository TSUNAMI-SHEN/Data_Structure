class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp0 = cost[0]
        dp1 = cost[1]
        res = 0

        for i in range(2, len(cost)):
            res = min(dp0, dp1) + cost[i]   #状态方程
            dp0, dp1 = dp1, res
        return min(dp0, dp1)
        
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[len(cost)-1], dp[len(cost)-2])
