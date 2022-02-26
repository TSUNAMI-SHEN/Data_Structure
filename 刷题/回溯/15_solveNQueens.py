class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 矩阵的高度就是树的高度，矩阵的宽度就是树层的宽度

        if not n: return []
        board = [['.']*n for _ in range(n)]
        res = []

        # 判断是否合理
        def isValid(board, row, col):
            # 判断同一列是否冲突
            for i in range(len(board)):
                if board[i][col] == 'Q':
                    return False
            
            # 判断左上角是否冲突
            i = row - 1
            j = col - 1
            while i>=0 and j>=0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # 判断右上角是否冲突
            i = row - 1
            j = col + 1
            while i>=0 and j<len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True
        
        def backtracking(board, n, row):        # 确定参数，board——棋盘，记录结果；n——棋盘大小；row——进行到第几行
            # 确定终止条件
            # 如果走到最后一行，说明已经找到一个解
            if row == n:
                temp_res = []
                for temp in board:
                    temp_str = "".join(temp)
                    temp_res.append(temp_str)
                res.append(temp_res)
            for col in range(n):
                if not isValid(board, row, col):        # 每一列进行判断，如果不冲突，则在该列添加Q
                    continue
                board[row][col] = 'Q'
                backtracking(board, n, row+1)           # 递归到下一行
                board[row][col] = '.'                   # 回溯
        backtracking(board, n, 0)
        return res
        
