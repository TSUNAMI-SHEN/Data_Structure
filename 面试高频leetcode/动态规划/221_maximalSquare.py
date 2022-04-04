class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp数字含义：dp[i][j]表示坐标(i,j)处最大正方形的边长
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0]*cols for _ in range(rows)]
        maxSide = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    # 如果是左上角元素，则dp[0][0]=1
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    # 当前点的正方形边长由左上、正上、左方三个点的最小值决定
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        return maxSide ** 2
