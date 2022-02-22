# 逆波兰表达式，利用栈解决，类似删除字符串中，做运算而不是对对碰除去
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item not in {'+', '-', '*', '/'}:
                stack.append(item)
            else:
                first_num = stack.pop()
                seconde_num = stack.pop()
                stack.append(int(eval(f'{seconde_num} {item} {first_num}')))    # 第一个出来的在运算符后面
        return int(stack.pop())     # 如果一开始只有一个数，那么会是字符串形式的
