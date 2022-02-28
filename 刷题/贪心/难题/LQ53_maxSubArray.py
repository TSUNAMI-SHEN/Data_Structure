class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 贪心：负数会拉低总和
        # 局部最优：因此当当前连续和为负数的时候，立刻放弃，从下一个元素重新计算
        result = -float("inf")
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count
            if count <= 0:  # 如果当前连续和小于0，则count归为0重新开始计算
                count = 0
        return result
