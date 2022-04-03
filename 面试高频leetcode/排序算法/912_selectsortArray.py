class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 选择排序：每次选出最小的元素
        for i in range(len(nums)-1):
            minIndex = i
            # 找到最小值的下标
            for j in range(i+1, len(nums)):
                if nums[j] < nums[minIndex]:
                    minIndex = j
            # 交换最小元素
            nums[i], nums[minIndex] = nums[minIndex], nums[i]

        return nums
