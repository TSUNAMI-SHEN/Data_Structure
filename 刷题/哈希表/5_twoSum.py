class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = dict()

        for idx, val in enumerate(nums):
            if target - val not in record:
                record[val] = idx       # record字典中键是那个值，值是对应的下标，因为最后要求的是下标
            else:
                return [record[target-val], idx]    
