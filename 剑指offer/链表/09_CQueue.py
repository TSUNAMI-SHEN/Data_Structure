class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        # 如果stack2非空，则直接弹出stack2的头元素
        if self.stack2: return self.stack2.pop()

        # 如果stack1为空，stack2为空则整个队列为空，直接返回-1
        if not self.stack1: return -1

        # 当stack1非空时，先将元素放入stack2中再弹出头元素
        while self.stack1:
            val = self.stack1.pop()
            self.stack2.append(val)
        return self.stack2.pop()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
