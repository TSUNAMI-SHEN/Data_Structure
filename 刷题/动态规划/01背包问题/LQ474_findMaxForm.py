class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j]：最多有i个0和j个1的strs的最大子集的大小为dp[i][j]
        # 背包有两个维度
        dp = [[0]* (n+1) for _ in range(m+1)]
        for str in strs:
            onesNum = str.count('1')
            zerosNum = str.count('0')

            for i in range(m, zerosNum-1, -1):
                for j in range(n, onesNum-1, -1):
                    dp[i][j] = max(dp[i-zerosNum][j-onesNum] + 1, dp[i][j])
        return dp[m][n]
