class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1

        # 遍历背包
        for i in range(1, target+1):
            # 遍历物品
            for j in nums:
                if i >= j:      # 如果物品小于背包容量时才可以加入
                    dp[i] += dp[i-j]
        return dp[target]
