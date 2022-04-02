class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        start = 0
        end = 0
        total = 0
        
        # 滑动窗口，end是滑动窗口的右边界，start是滑动窗口的左边界
        while end < n:
            # 先加入右边界元素，然后进行总和的判断，若大于则不断缩小窗口大小，最后窗口再往右移动
            total += nums[end]
            while total >= target:
                ans = min(ans, end-start+1)
                total -= nums[start]
                start += 1
            end += 1
        return 0 if ans == n + 1 else ans
