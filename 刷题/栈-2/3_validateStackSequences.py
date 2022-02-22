# 模拟栈的操作。利用辅助栈stack来模拟push和pop的操作，stack栈放入push的元素与popped栈的元素比较（从popped栈中从左往右比较）
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0
        for item in pushed:
            stack.append(item)
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1
        if stack:
            return False
        return True
