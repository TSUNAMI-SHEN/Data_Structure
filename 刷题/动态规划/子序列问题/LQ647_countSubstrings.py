class Solution:
    def countSubstrings(self, s: str) -> int:
        # 布尔类型的dp[i][j]：表示区间范围[i,j] （注意是左闭右闭）的子串是否是回文子串，如果是dp[i][j]为true，否则为false
        dp = [[False]*(len(s)) for _ in range(len(s))]
        res = 0

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j-i <= 1:
                        res += 1
                        dp[i][j] = True
                    elif dp[i+1][j-1]:
                        res += 1
                        dp[i][j] = True
        return res
