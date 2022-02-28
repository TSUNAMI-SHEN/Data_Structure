class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        ans = 0
        curDistance = 0     # 当前覆盖最远距离的下标
        nextDistance = 0    # 下一步覆盖最远距离的下标
        for i in range(len(nums)):
            nextDistance = max(i+nums[i], nextDistance)     # 更新下一步覆盖最远距离的下标
            if i == curDistance:    # 遇到当前覆盖最远距离下标
                if curDistance != len(nums) - 1:    # 如果当前覆盖最远距离下标不是终点
                    ans += 1                        # 需要走下一步
                    curDistance = nextDistance      # 更新当前覆盖的最远距离下标
                    if nextDistance >= len(nums) - 1:   # 下一步的覆盖范围已经达到终点，结束循环
                        break
        return ans
      
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n-1):
            if maxPos >= i:
                maxPos = max(i+nums[i], maxPos)
                if i == end:
                    end = maxPos  # end是当前下标能覆盖的最远距离
                    step += 1
        return step
