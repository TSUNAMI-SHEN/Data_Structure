# 用栈实现队列，输入栈和输出栈辅助

class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        if self.stack_out == []:
            while self.stack_in != []:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        else:
            return self.stack_out.pop()

    def peek(self) -> int:
        ans = self.pop()    # 直接利用pop函数获取队列的首元素
        self.stack_out.append(ans)  # 因为pop是取出了首元素，需要把它放回队列中，放在out栈中
        return ans

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)        # 只要in和out中有元素就非空


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
