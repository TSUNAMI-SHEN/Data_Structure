class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 按照身高高的people的k来插入
        people.sort(key=lambda x:(-x[0], x[1]))
        que = []
        for p in people:
            que.insert(p[1], p)
        return que
