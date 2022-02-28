class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = 0
        minPro = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < minPro:      # 相当于买入
                minPro = prices[i]
            elif prices[i] >= minPro and prices[i] <= minPro + fee: # 相当于不操作，因为买入没有利润
                continue
            else:
                result += prices[i] - minPro - fee  # 相当于卖出，有利润可赚
                minPro = prices[i] - fee
            
        return result
