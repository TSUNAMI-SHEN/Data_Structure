class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 冒泡排序：每次找出一个最大的元素，因此需要遍历n-1次

        for i in range(len(nums)-1):
            flag = False
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]
                    flag = True
            # 如果这一轮没有发生交换说明已经达到有序，可以提前终止排序
            if flag == False:
                break
        return nums
