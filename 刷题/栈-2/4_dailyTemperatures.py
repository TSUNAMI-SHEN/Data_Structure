# https://www.algomooc.com/620.html
# 当前数字需要不断跟栈顶元素进行比较，当前数字一定是第一个大于栈顶元素的数，直接求出下标差就是二者的距离
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        res = [0]*length
        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                preIndex = stack.pop()
                res[preIndex] = i - preIndex
            stack.append(i)
        return res
