class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 有重叠的部分将气球射了
        # 气球重叠时，右边边界的最小值之前的区间一定需要一个弓箭
        if len(points) == 0:
            return 0
        points.sort(key=lambda x:x[0])
        result = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i-1][1]:
                result += 1
            else:
                points[i][1] = min(points[i-1][1], points[i][1])    # 更新重叠气球最小右边界
        return result
