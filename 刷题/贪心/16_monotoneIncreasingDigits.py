class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # 局部最优：遇到strNum[i - 1] > strNum[i]的情况，让strNum[i - 1]--，然后strNum[i]给为9，可以保证这两位变成最大单调递增整数
        # 全局最优：得到小于等于N的最大单调递增的整数
        # 从后往前遍历
        a = list(str(n))
        for i in range(len(a)-1, 0, -1):
            if int(a[i]) < int(a[i-1]):
                a[i:] = '9' * (len(a)-i)
                a[i-1] = str(int(a[i-1])-1)
        return int(''.join(a))
