class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 贪心思路：把绝对值大的负数先翻转，如果翻转次数不到k，则将绝对值最小的正数数次翻转知道达到k
        nums = sorted(nums, key=abs, reverse=True)
        for i in range(len(nums)):
            if k>0 and nums[i]<0:
                nums[i] *= -1
                k -= 1
        if k>0:
            nums[-1] *= (-1) ** k
        return sum(nums)
