# 先计算空格数，然后预留新字符串的长度，从后往前填充
class Solution:
    def replaceSpace(self, s: str) -> str:
        
        count = 0
        for i in range(len(s)):
            if s[i] == ' ':
                count += 1
        
        res = list(s)
        res.extend([' '] * count * 2)

        left, right = len(s) - 1, len(res) - 1

        while left >= 0:
            if s[left] != " ":
                res[right] = s[left]
                right -= 1
                left -= 1
            else:
                res[right] = "0"
                res[right-1] = "2"
                res[right-2] = "%"
                right -= 3
                left -= 1
        return ''.join(res)
