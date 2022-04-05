class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 使用二分法找到target在nums中第一次出现的位置
        def find_left_index(nums, target):
            low, high = 0, len(nums) - 1
            while low < high:
                mid = low + (high - low) // 2
                if nums[mid] > target or target == nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            return low if nums and nums[low] == target else -1

        # 使用二分法找到target在nums中最后一次出现的位置
        def find_right_index(nums, target):
            low, high = 0, len(nums) - 1
            while low < high:
                mid = low + (high - low) // 2 + 1
                if nums[mid] < target or target == nums[mid]:
                    low = mid
                else:
                    high = mid - 1
            return low if nums and nums[low] == target else -1

        return [find_left_index(nums, target), find_right_index(nums, target)]
