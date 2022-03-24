class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[False] * n for _ in range(n)]    # dp数组含义是指区间[i,j]的子字符串是否为回文串

        for i in range(n):
            dp[i][i] = True
        
        res = n

        for left in range(n-1, -1, -1):

            for right in range(left+1, n):
                
                if s[right] == s[left]:
                    # 如果是相邻的两个字母相同，则直接判定是回文串
                    if right - left == 1:
                        dp[left][right] = True
                        res += 1
                    # 否则需要看内部的子字符串是否为回文串
                    else:
                        if dp[left+1][right-1] == True:
                            dp[left][right] = True
                            res += 1
        
        return res
