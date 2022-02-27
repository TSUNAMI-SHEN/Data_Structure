class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        dp = [1] * n
        result = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:   # 当j的元素大于i的元素时，dp[j]+1，然后取dp[i]和dp[j+1]中的较大者
                    dp[i] = max(dp[i], dp[j]+1)
            result = max(result, dp[i])
        return result
