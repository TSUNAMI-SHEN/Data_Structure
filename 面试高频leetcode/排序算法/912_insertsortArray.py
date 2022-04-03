class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 插入排序
        for i in range(len(nums)-1):
            curNum, preIndex = nums[i+1], i
            # 当前的数curNum和nums[preIndex+1]进行交换，找到应该插入的位置
            while preIndex >= 0 and curNum < nums[preIndex]:
                nums[preIndex+1] = nums[preIndex]
                preIndex -= 1
            nums[preIndex+1] = curNum
        
        return nums
