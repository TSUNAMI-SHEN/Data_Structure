class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [[0]*(2*k+1) for _ in range(len(prices))]

        for j in range(1, 2*k, 2):
            dp[0][j] = -prices[0]   # 买入的初始化状态
        for i in range(1, len(prices)):
            for j in range(0, 2*k-1, 2):
                dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j]-prices[i])    # 奇数天买入
                dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1]+prices[i])  # 偶数天卖出
        return dp[-1][2*k]
