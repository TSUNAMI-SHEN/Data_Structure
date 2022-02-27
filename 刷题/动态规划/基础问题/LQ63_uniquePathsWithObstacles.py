class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        dp = [[0 for _ in range(col)] for _ in range(row)]
        
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
        else:
            dp[0][0] = 0
        
        if dp[0][0] == 0:   # 如果第一个格子就是障碍，则返回0
            return 0        
        
        # 第一行
        for i in range(1, col):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i-1]       # 遇到一个不为0时，后面的数都为0，因为无法通过了
        
        # 第一列
        for j in range(1, row):
            if obstacleGrid[j][0] != 1:
                dp[j][0] = dp[j-1][0]
        
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] != 1: # 动态方程，多加一个判断
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]  
        
        return dp[-1][-1]
        
