class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        ans = list()
        stk = list()    # 用来记录路径节点

        def dfs(x: int):
          # 终止条件：如果到达n-1，则添加路径并终止
            if x == len(graph) - 1:
                ans.append(stk[:])
                return
            
            for y in graph[x]:
                stk.append(y)
                dfs(y)
                stk.pop()
        
        stk.append(0) # 从0号出发
        dfs(0)
        return ans
