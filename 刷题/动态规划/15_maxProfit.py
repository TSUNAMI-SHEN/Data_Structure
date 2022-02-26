class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        dp = [[0]*5 for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]   # 没有操作的情况
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])    # 第一次买入，可能是第i或i-1天买入
            dp[i][2] = max(dp[i-1][2], dp[i-1][1]+prices[i])    # 第一次卖出，可能是第i或i-1天卖出
            dp[i][3] = max(dp[i-1][3], dp[i-1][2]-prices[i])    # 第二次买入，可能是第i或i-1天买入
            dp[i][4] = max(dp[i-1][4], dp[i-1][3]+prices[i])    # 第二次卖出，可能是第i或i-1天卖出
        return dp[-1][4]

    
# 优化写法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        dp = [0] * 5
        dp[1] = -prices[0]
        dp[3] = -prices[0]

        for i in range(len(prices)):
            dp[1] = max(dp[1], dp[0]-prices[i])
            dp[2] = max(dp[2], dp[1]+prices[i])
            dp[3] = max(dp[3], dp[2]-prices[i])
            dp[4] = max(dp[4], dp[3]+prices[i])

        return dp[4] 
