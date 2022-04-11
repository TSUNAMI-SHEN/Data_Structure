class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # flag = False
        # for i in range(len(nums)-1, 0, -1):
        #     if nums[i] > nums[i-1]:
        #         nums[i], nums[i-1] = nums[i-1], nums[i]
        #         flag = True
        #         break
        # if flag:
        #     return nums
        # else:
        #     return nums[::-1]

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:  # 首先找到一个逆序的数
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:    # 找到上个循环中找到的逆序的第一个数，然后不断循环找到比该数大的最小数
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # 再进行交换
        left, right = i+1, len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
