class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], -prices[i])     # i当天持有股票，考虑两种情况，1.i-1天已经持有股票，i天不买入;2.第i天买入，持有现金即为-prices[i]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i]) # i当天不持有股票，考虑两种情况，1.第i-1天就不持有股票，保持原状；2.第i天卖出
        return dp[n-1][1]
