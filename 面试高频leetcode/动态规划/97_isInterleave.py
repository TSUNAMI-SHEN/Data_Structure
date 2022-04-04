class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp[i][j]表示s1的前i个字符和s2的前j个字符是否能构成s3的前i+j个字符
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len1 + len2 != len3:
            return False

        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
        dp[0][0] = True

        for i in range(1, len1+1):
            dp[i][0] = (dp[i-1][0] and s1[i-1]==s3[i-1])
        for j in range(1, len2+1):
            dp[0][j] = (dp[0][j-1] and s2[j-1]==s3[j-1])
        
        for m in range(1, len1+1):
            for n in range(1, len2+1):
                dp[m][n] = (dp[m-1][n] and s1[m-1]==s3[m+n-1]) or (dp[m][n-1] and s2[n-1]==s3[m+n-1])
        
        return dp[-1][-1]
