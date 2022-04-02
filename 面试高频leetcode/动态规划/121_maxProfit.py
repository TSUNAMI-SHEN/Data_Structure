class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心算法
        # res = 0
        # low = float('inf')
        # for i in range(len(prices)):
        #     low = min(low, prices[i])
        #     res = max(res, prices[i]-low)
        # return res

        # 动态规划
        # dp二维数组，dp[i][0]表示第i天不持有股票的利润，dp[i][1]表示第i天持有股票的利润
        dp = [[0]*2 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            # 第i天不持有股票，1.可能第i-1天就不持有股票；2.可能第i-1天持有股票，然后第i天卖出了，两者取较大者
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            # 第i天持有股票，1.可能第i-1天就持有股票，第i天无动作；2.可能第i-1天不持有股票，然后第i天买入股票了（注意股票只能买卖一次），两者取较大者
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[-1][0]
