class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paths = []
        path = []

        def backtracking(left, right):
            # left,right记录左右括号个数进行判断，有效括号必须左括号先放并且个数不小于右括号个数

            if left < 0 or right < 0 or right < left:
                return
            
            if left == 0 and right == 0:
                paths.append(''.join(path))
                return
            
            # 先放左括号
            path.append('(')
            backtracking(left-1, right)
            path.pop()

            # 再放右括号
            path.append(')')
            backtracking(left, right-1)
            path.pop()

        backtracking(n, n)
        return paths
