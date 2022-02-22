# 先分析三种不匹配的情况，再写代码
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '{':
                stack.append('}')
            elif item == '[':
                stack.append(']')
            elif not stack or stack[-1] != item:    # not stack对应遍历过程中栈变空，stack[-1]对应出现不匹配的情况
                return False
            else:
                stack.pop()
        return True if not stack else False
