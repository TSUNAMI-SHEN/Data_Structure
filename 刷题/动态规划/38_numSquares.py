class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i**2 for i in range(1, n+1) if i**2 <= n]
        dp = [10**4] * (n+1)
        dp[0] = 0

        # # 先遍历物品
        # for num in nums:
        #     # 再遍历背包
        #     for j in range(num, n+1):
        #         dp[j] = min(dp[j], dp[j-num]+1)
        # return dp[n]


        # 先遍历背包
        for j in range(1, n+1):
            # 再遍历物品
            for num in nums:
                if num <= j:
                    dp[j] = min(dp[j], dp[j-num]+1)
        return dp[n]
