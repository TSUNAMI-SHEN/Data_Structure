class Solution:
    def __init__(self):
        self.res = []
        self.sum_now = 0
        self.path = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backstrack(k, n, 1)
        return self.res


    # 确定参数
    # 1.目标和-n；2.要求k个数；3.sum-当前path的和；4.startindex-下一层for循环开始的位置
    def backstrack(self, k: int, n: int, startindex: int):
        # 终止条件，如果路径长度=k，且sum等于目标值，则添加path
        if len(self.path) == k:
            if self.sum_now == n:    # 
                self.res.append(self.path[:])
            return
        
        # 如果当前和大于n，则直接返回
        if self.sum_now > n:
            return

        for i in range(startindex, 10-(k-len(self.path))+1):
            self.path.append(i)
            self.sum_now += i
            self.backstrack(k, n, i+1)
            self.path.pop()
            self.sum_now -= i
