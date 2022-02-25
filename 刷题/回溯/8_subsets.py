class Solution:
    def __init__(self):
        self.path: List[int] = []
        self.paths: List[List[int]] = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.path.clear()
        self.paths.clear()
        self.backtracking(nums, 0)
        return self.paths
    
    def backtracking(self, nums: List[int], startIndex: int):
        self.paths.append(self.path[:])

        # 终止条件
        if startIndex == len(nums):  # 开始遍历的节点已经大于数组的长度了，就终止了，因为没有元素可取了
            return
        
        for i in range(startIndex, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()
