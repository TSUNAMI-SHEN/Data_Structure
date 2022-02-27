class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 动态规划——编辑距离
        # dp[i][j] 表示以下标i-1为结尾的字符串s，和以下标j-1为结尾的字符串t，相同子序列的长度为dp[i][j]
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
        if dp[-1][-1] == len(s):
            return True
        return False
