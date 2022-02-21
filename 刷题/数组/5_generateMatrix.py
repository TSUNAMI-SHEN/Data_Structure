# 坚持循环不变量原则，画每条边的时候坚持同一个原则，左闭右开
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        left, right, up, down = 0, n-1, 0, n-1
        number = 1
        while left < right and up < down:
            for x in range(left, right):
                matrix[up][x] = number
                number += 1
            
            for y in range(up, down):
                matrix[y][right] = number
                number += 1
            for x in range(right, left, -1):
                matrix[down][x] = number
                number += 1
            for y in range(down, up, -1):
                matrix[left][y] = number
                number += 1
            left += 1
            right -= 1
            up += 1
            down -= 1
        if n % 2:
            matrix[n//2][n//2] = number
        return matrix
