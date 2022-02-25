class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.path.clear()
        self.paths.clear()
        used_list = [False] * len(nums)
        self.backtracking(nums, used_list)
        return self.paths
    
    def backtracking(self, nums: List[int], used_list: List[bool]) -> None:
        if len(self.path) == len(nums):
            self.paths.append(self.path[:])
            return
        
        for i in range(0, len(nums)):
            if used_list[i] == True:
                continue
            used_list[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, used_list)      # 纵向传递元素的使用信息，去重
            self.path.pop()
            used_list[i] = False
