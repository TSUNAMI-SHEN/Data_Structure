class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 滑动窗口
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        start, end = 0, 0

        total = 0

        while end < n:
            total += nums[end]
            while total >= target:
                ans = min(ans, end-start+1)
                total -= nums[start]
                start += 1
            end += 1
        
        return 0 if ans == n + 1 else ans
