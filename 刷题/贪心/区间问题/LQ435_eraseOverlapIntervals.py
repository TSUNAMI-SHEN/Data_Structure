class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 局部最优：优先选取右边界小的区间，所以从左向右遍历，留给下一个区间的空间大一些，从而尽量避免交叉
        # 全局最优：选取最多的非交叉区间
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x:x[1])
        count = 1
        end = intervals[0][1]   # 记录非交叉区间的个数
        for i in range(1, len(intervals)):
            if end <= intervals[i][0]:  # 说明没有交叉，count+1，区间覆盖的范围更新为intervals[i][1]
                count += 1
                end = intervals[i][1]
        return len(intervals) - count
