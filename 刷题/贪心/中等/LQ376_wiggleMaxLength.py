class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 保持区间波动，只需要把单调区间上的元素移除即可
        preC, curC, res = 0, 0, 1
        for i in range(len(nums)-1):
            curC = nums[i+1] - nums[i]
            if curC * preC <= 0 and curC != 0:   # 差值为0，不算摆动
                res += 1
                preC = curC
        return res
