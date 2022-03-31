class MyStack:

    def __init__(self):
        self.que1 = deque()     # 辅助栈
        self.que2 = deque()     # 主栈

    def push(self, x: int) -> None:
        self.que1.append(x)
        while self.que2:
            self.que1.append(self.que2.popleft())
        self.que1, self.que2 = self.que2, self.que1

    def pop(self) -> int:
        return self.que2.popleft()

    def top(self) -> int:
        return self.que2[0]


    def empty(self) -> bool:
        return not self.que2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
