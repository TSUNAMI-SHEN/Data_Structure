class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used_list = [False] * len(nums)
        self.path.clear()
        self.paths.clear()
        nums.sort()     # 需要排序
        self.backtracking(nums, used_list)
        return self.paths


    def backtracking(self, nums: List[int], used_list: List[bool]) -> None:
        if len(self.path) == len(nums):
            self.paths.append(self.path[:])
            return
        
        for i in range(0, len(nums)):
            if not used_list[i]:
                if i > 0 and nums[i] == nums[i-1] and not used_list[i-1]:   # not used_list[i-1]表明同一树层中前一个元素已经使用过，需要去重
                    continue
                used_list[i] = True
                self.path.append(nums[i])
                self.backtracking(nums, used_list)
                self.path.pop()
                used_list[i] = False
