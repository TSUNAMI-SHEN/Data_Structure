class Solution:
    def numTrees(self, n: int) -> int:
        # 状态方程： dp[i] += dp[以j为头结点左子树节点数量] * dp[以j为头结点右子树节点数量]
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]  # dp[j-1]：以j为头节点左子树节点数量；dp[i-j]：以j为头节点右子树节点数量
        return dp[-1]
