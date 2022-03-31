class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ss in s:
            if ss == '(':
                stack.append(')')
            elif ss == '{':
                stack.append('}')
            elif ss == '[':
                stack.append(']')
            
            # 中途stack不能为空,若遇到ss=}\]\)则判断是否与栈顶元素相等,相等则pop掉,不相等直接判为False
            elif stack and stack[-1] == ss:
                stack.pop()
            else:
                return False

        # 遍历完时stack应该是空的,否则为False
        if not stack:
            return True
        else:
            return False 
