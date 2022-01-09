//跳台阶的方法，动态规划，与斐波那契数列只是初始状态不同
class Solution {
public:
    int numWays(int n) {
        int a = 1, b = 1, sum;
        for (int i = 0; i < n; i++)
        {
            sum = (a + b) % 1000000007;
            a = b;
            b = sum;
        }
        return a;
    }
};
