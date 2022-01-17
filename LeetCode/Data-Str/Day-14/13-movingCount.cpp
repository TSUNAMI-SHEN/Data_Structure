//机器人的运动范围
//1.深度优先算法+剪枝
class Solution {
public:
    int movingCount(int m, int n, int k) {
        vector<vector<bool>> visited(m, vector<bool>(n,0));
        return dfs(0, 0, 0, 0, visited, m, n, k);
    }
private:
    int dfs(int i, int j, int si, int sj, vector<vector<bool>> & visited, int m, int n, int k){
        if(i >=m || j >= n|| k < si + sj || visited[i][j]) return 0;    //判断返回的标志
        visited[i][j] = true;   //标记当前的单元格已经被访问过
        return 1 + dfs(i+1, j, (i+1) % 10 != 0 ? si+1 : si-8, sj, visited, m, n, k) +
                    dfs(i, j+1, si, (j+1) % 10 != 0 ? sj+1 : sj-8, visited, m, n, k);     //不断深入搜索
    }
};

//2.广度优先算法
class Solution {
public:
    int movingCount(int m, int n, int k) {
        vector<vector<bool>> visited(m, vector<bool>(n,0));
        int res = 0;
        queue<vector<int>> que;
        que.push({0, 0, 0, 0});
        while(que.size() > 0){
            vector<int> x = que.front();
            que.pop();
            int i = x[0], j=x[1], si=x[2], sj=x[3];
            if(i >= m || j >= n || k < si + sj || visited[i][j]) continue;
            visited[i][j] = true;
            res++;      //队列中元素出列，res++，即记录符合的单元格个数
            que.push({i+1, j, (i+1) % 10 != 0 ? si+1 : si-8, sj});
            que.push({i, j+1, si, (j+1) % 10 != 0 ? sj+1 : sj-8});    //满足条件的单元格不断加入队列中
        }
        return res;
    }
};
