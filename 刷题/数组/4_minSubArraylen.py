# 采用滑动窗口
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        sum = 0
        index = 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                res = min(res, i-index+1)
                sum -= nums[index]
                index += 1
        return 0 if res == float('inf') else res
