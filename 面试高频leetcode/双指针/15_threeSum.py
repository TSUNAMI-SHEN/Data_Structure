class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()     # 只需要找出元素的，不关心索引，因此可以排序，方便剔除相同的元素

        for i in range(len(nums)):
            # 如果num[i]>=0，因为排过序，所以以此为开头的数一定不符合
            if nums[i] > 0:
                break
            
            # 如果前后两个元素相同，则跳过，因为答案不含重复的三元组
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1


            # 利用前后指针对三个数求和，作比较
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # 排除相同的元素
                    while left < right and nums[left+1] == nums[left]: left += 1
                    while left < right and nums[right-1] == nums[right]: right -= 1
                    # 缩小范围
                    left += 1
                    right -= 1
                
        return res
