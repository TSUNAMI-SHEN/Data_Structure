class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 采用两次贪心的策略
        # 1.从左到右遍历，只比较右边孩子比左边大的情况
        # 2.从右到左遍历，只比较左边孩子比右边大的情况
        candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:   # 从左往右的情况，如果i的评分比i-1大，则i的糖要比i-1多一个
                candy[i] = candy[i-1] + 1
        for j in range(len(ratings)-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                candy[j] = max(candy[j], candy[j+1]+1)  # 需要确保相邻的孩子中评分高的获得更多的糖果，那么要保证第i个孩子的糖果数量既大于左边的，又大于右边的
        return sum(candy)
