class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.path.clear()
        self.paths.clear()
        self.backtracking(nums, 0)
        return self.paths

    
    def backtracking(self, nums: List[int], startIndex: int) -> bool:
        if len(self.path) >= 2:
            self.paths.append(self.path[:])
        
        if startIndex == len(nums):
            return

        used_list = [False] * 201       # 利用哈希表进行去重
        for i in range(startIndex, len(nums)):

            if (self.path and nums[i] < self.path[-1]) or used_list[nums[i]+100] == True:  # 1.如果插入的数小于序列中最后一个数（不满足递增） or 2.同一层中这个数已经用过了
                continue
            used_list[nums[i]+100] = True
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()
