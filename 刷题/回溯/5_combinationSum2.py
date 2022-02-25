class Solution:
    def __init__(self):
        self.path = []
        self.res = []
        self.used = []  # 用来去重

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.path.clear()
        self.res.clear()
        self.used = [False] * len(candidates)
        candidates.sort()
        self.backstrcking(candidates, target, 0, 0)
        return self.res

    def backstrcking(self, candidates: List[int], target: int, sum_: int, startIndex: int) -> None:
        # 确定终止条件
        if sum_ == target:
            self.res.append(self.path[:])
            return
        
        # 单层逻辑
        for i in range(startIndex, len(candidates)):

            if sum_ + candidates[i] > target:
                return

            # 检查同一树层是否出现曾经使用过的相同元素
            # 若数组中前后元素值相同，但前者却未被使用，说明是for loop中的同一树层的相同元素情况
            if i > 0 and candidates[i] == candidates[i-1] and self.used[i-1] == False:
                continue
            
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.used[i] = True
            self.backstrcking(candidates, target, sum_, i+1)    # 递归
            self.used[i] = False    # 回溯
            sum_ -= candidates[i]
            self.path.pop()
            
