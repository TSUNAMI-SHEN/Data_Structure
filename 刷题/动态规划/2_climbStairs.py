class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
         
        # 初始状态
        dp1, dp2 = 1, 2
        res = 0

        for i in range(2, n): 
            res = dp1 + dp2     # 动态方程 dp[i] = dp[i-1] + dp[i-2]
            dp1, dp2 = dp2, res
        return res
