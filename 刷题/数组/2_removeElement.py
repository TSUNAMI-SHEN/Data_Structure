class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = slow = 0

        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]     # 若不等于要删除的值（是需要保存的），先将值赋给slow，再将slow后移
                slow += 1
            fast += 1
        
        return slow
