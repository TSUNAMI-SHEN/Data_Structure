//二维数组中的查找，数组每一行从左到右递增，每一列从上到下递增
//将数组旋转45°，可以看成二叉搜索树
class Solution {
public:
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
        int i = matrix.size() - 1, j = 0;
        while(i>=0 && j<matrix[0].size())
        {
            if(matrix[i][j] > target)
            {
                i--;
            }
            else if(matrix[i][j] < target)
            {
                j++;
            }
            else return true;
        }
        return false;
    }
};
