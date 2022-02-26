class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        res1 = self.robRange(nums, 0, n-2)
        res2 = self.robRange(nums, 1, n-1)
        return max(res1, res2)

    # 考虑只包含首元素和只包含尾元素的两种情况
    def robRange(self, nums: List[int], start: int, end: int) -> int:
        if end == start:
            return nums[start]  # 如果只有一个数字，直接返回该数字
        dp = [0] * len(nums)
        dp[start] = nums[start]
        dp[start+1] = max(nums[start], nums[start+1])

        for i in range(start+2, end+1):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        return dp[end]
