# 针对各种符号具体考虑，' ', '+', '-', '(', ')'以及数字（可能是多位数）的情况考虑清楚
class Solution:
    def calculate(self, s: str) -> int:
        ops = [1]
        length = len(s)
        sign = 1
        i = 0
        res = 0

        while i < length:
            
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < length and s[i].isdigit():
                    num = 10 * num + ord(s[i]) - ord('0')
                    i += 1
                res += num * sign
        return res
