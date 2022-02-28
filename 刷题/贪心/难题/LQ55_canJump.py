class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 只要考虑跳跃覆盖的范围大于整个数组的长度即可
        # 局部最优解：每次取最大跳跃步数
        # 整体最优解：最后得到整体最大覆盖范围，看是否能到终点
        cover = 0
        if len(nums) == 1:
            return True
        i = 0
        while i <= cover:
            cover = max(i+nums[i], cover)
            if cover > len(nums) -1 :
                return True
            i += 1
        return False
