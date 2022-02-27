class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(n, k, startIndex):
            # 确定终止条件
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(startIndex, n-(k-len(path))+2):  # 加上了剪枝操作
                path.append(i)  # 处理节点
                backtrack(n, k, i+1)    # 递归
                path.pop()  # 撤销处理
        backtrack(n, k, 1)
        return res
