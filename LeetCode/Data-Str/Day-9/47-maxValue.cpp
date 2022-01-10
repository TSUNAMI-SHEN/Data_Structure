//礼物的最大值
class Solution {
public:
    int maxValue(vector<vector<int>>& grid) {
        // int maxV = grid[0][0];
        int m = grid.size();
        int n = grid[0].size();
        for (int i = 1; i < n; i++)
        {
            grid[0][i] += grid[0][i-1];
        }
        for (int j = 1; j < m; j++)
        {
            grid[j][0] += grid[j-1][0];
        }
        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                grid[i][j] += max(grid[i-1][j], grid[i][j-1]);
            }
        }
        return grid[m-1][n-1];
    }
};
