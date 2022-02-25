class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def partition(self, s: str) -> List[List[str]]:
        self.path.clear()
        self.paths.clear()
        self.backtracking(s, 0)
        return self.paths


    def backtracking(self, s: str, startIndex: int) -> None:
        # 确定终止条件：切割线切到了字符串最后面，说明找到了一种切割方法，此时就是本层递归的终止条件
        if startIndex >= len(s):
            self.paths.append(self.path[:])
            return
        
        # 单层逻辑
        for i in range(startIndex, len(s)):
            temp = s[startIndex:i+1]    # 判断被截取的这一段子串是否为回文串
            if temp == temp[::-1]:
                self.path.append(temp)
                self.backtracking(s, i+1)   # 递归，纵向遍历，从下一处进行切割，判断是否仍为回文串
                self.path.pop()
            else:
                continue
        
