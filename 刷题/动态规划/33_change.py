class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[j]数组表示凑成总金额j的货币组合数
        dp = [0] * (amount + 1)
        dp[0] = 1

        # 遍历物品（即不同面额的硬币）
        for i in range(len(coins)):
            # 遍历背包
            for j in range(coins[i], amount+1):
                dp[j] += dp[j - coins[i]]
        return dp[amount]
