class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
        
        res = n

        for left in range(n-1, -1, -1):

            for right in range(left+1, n):

                if s[right] == s[left]:
                    if right - left == 1:
                        dp[left][right] = True
                        res += 1
                    else:
                        if dp[left+1][right-1] == True:
                            dp[left][right] = True
                            res += 1
        
        return res
