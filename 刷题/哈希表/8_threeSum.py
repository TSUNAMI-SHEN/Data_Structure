# 利用双执政的方法，提高去重的效率
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            left = i + 1
            right = n - 1
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    # 排除重复的三元组
                    while left != right and nums[left] == nums[left+1]: left += 1
                    while left != right and nums[right] == nums[right-1]: right -= 1
                    left += 1
                    right -= 1
        return ans
