class Solution:
    def climbStairs(self, n: int) -> int:
        # 是排列问题
        dp = [0] * (n+1)
        dp[0] = 1
        m = 2

        # 遍历背包
        for i in range(1, n+1):
            # 遍历物品，能走的台阶数
            for j in range(1, m+1):
                if i >= j:  # 如果向上走j步还未到i台阶才可以，即背包容量要大于物品
                    dp[i] += dp[i-j]
        return dp[n]
