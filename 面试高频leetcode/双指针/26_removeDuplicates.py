class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 快慢指针
        if not nums:
            return 0
        fast = slow = 1
        while fast < len(nums):
            # 当遇到不同元素，慢指针接收快指针的元素
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
