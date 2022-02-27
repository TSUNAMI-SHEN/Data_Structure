class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        res = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]: # 如果当前的数大于前一个数，那么dp[i] = dp[i-1]+1，否则dp[i]变为1（这个放在初始化里）
                dp[i] = dp[i-1]+1
            res = max(res, dp[i])
        return res
