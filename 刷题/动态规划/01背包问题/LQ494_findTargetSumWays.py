class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumV = sum(nums)
        if abs(target) > sumV or (sumV+target) % 2 == 1:
            return 0
        
        bagSize = (sumV + target) // 2
        dp = [0] * (bagSize + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bagSize, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[bagSize]
