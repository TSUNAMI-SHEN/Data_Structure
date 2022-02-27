class Solution:
    def __init__(self):
        self.path = []
        self.res = []


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.path.clear()
        self.res.clear()
        self.backtracking(candidates, target, 0, 0)
        return self.res
    
    # 确定参数，candidates-给定集合，target-求和目标值，sum_-记录当前求和的值，startIndex-每层循环开始的地方
    def backtracking(self, candidates: List[int], target: int, sum_: int, startIndex: int) -> None:
        # 确定终止条件，sum_等于目标值，则添加path，并返回，如果sum_大于目标值，则直接返回
        if sum_ == target:
            self.res.append(self.path[:])
            return
        if sum_ > target:
            return
        
        # 处理单层逻辑
        for i in range(startIndex, len(candidates)):
            sum_ += candidates[i]   # 处理
            self.path.append(candidates[i]) 
            self.backtracking(candidates, target, sum_, i)  # 使用i是因为可以无限制重复选取
            sum_ -= candidates[i]   # 回溯
            self.path.pop()
