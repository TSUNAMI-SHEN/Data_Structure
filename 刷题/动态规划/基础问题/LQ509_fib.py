class Solution:
    def fib(self, n: int) -> int:
        # 0,1的情况单独考虑
        if n < 2:
            return n
        
        # 初始化，a=F(0), b=F(1)
        a, b = 0, 1
        res = 0
        for i in range(1, n):
            res = a + b     # dp方程，dp[i] = dp[i-1] + dp[i-2]
            a, b = b, res
        return res
