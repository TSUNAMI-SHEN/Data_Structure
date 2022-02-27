class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 将一堆石头尽可能分成重量相同的两堆，相撞之后剩下的石头最小
        sumweight = sum(stones)
        target = sumweight // 2
        dp = [0] * 15001
        for i in range(len(stones)):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
        return sumweight - 2 * dp[target]
