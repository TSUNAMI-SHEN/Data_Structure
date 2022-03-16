class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      #利用哈希表
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
