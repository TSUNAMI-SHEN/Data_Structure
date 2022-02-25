class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.paths.clear()
        self.path.clear()
        nums.sort() # 需要先对元素进行排序
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums: List[int], startIndex: int) -> None:
        # 确定终止条件
        self.paths.append(self.path[:])

        if startIndex == len(nums):
            return
        
        for i in range(startIndex, len(nums)):

            if i > startIndex and nums[i] == nums[i-1]:
                continue
            
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()
