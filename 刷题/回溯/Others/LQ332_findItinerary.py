class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets_dict = defaultdict(list)
        for item in tickets:
            tickets_dict[item[0]].append(item[1])
        '''
        tickets_dict里面的内容是这样的
         {'JFK': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})
        '''
        
        path = ['JFK']

        def backtracking(start_point):
            # 终止条件
            if len(path) == len(tickets) + 1:
                return True
            tickets_dict[start_point].sort()        # 对字典排序

            # 单层逻辑
            for _ in tickets_dict[start_point]:
                # 必须及时删除，避免出现死循环——找出第一个最小的机场，然后pop防止重复
                end_point = tickets_dict[start_point].pop(0)
                path.append(end_point)
                if backtracking(end_point):
                    return True
                path.pop()  # 回溯
                tickets_dict[start_point].append(end_point)
            
        backtracking("JFK")

        return path
