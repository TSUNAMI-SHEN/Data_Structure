class Solution:
    # 贪心：只要收集每天的正利润即可
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)-1):
            d = prices[i+1] - prices[i]
            if d > 0:
                result += d
        return result
