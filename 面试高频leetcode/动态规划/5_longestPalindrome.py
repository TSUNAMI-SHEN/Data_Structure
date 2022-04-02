class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        # dp数组表示s[i:j]子串是否为回文串
        dp = [[False]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
        
        max_length = 1  # 记录最长子串的长度
        begin = 0       # 记录最长子串的起始位置

        # 对子串长度进行遍历
        for L in range(2, n+1):
            # 长度为L的子串所有子串进行遍历
            for i in range(n):
                # 子串的右边界j
                j = i + L - 1

                if j >= n:
                    break
                
                if s[j] != s[i]:
                    dp[i][j] = False
                else:
                    # 若i-j区间长度小于3，则只要两个相等即可判定dp[i][j]是回文子串
                    if j - i < 3:
                        dp[i][j] = True
                    # 否则需要看内部的子串是否为回文串
                    else:
                        dp[i][j] = dp[i+1][j-1]
                
                if dp[i][j] and j - i + 1 > max_length:
                    max_length = j - i + 1
                    begin = i
        
        return s[begin:begin+max_length]
