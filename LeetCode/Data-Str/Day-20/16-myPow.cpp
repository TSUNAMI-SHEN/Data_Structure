//数值的整数次幂
class Solution {
public:
    double myPow(double x, int n) {
        if (x == 0.0f) return 0.0;
        double res = 1;
        long b = n;
        if (b < 0){
            x = 1 / x;
            b = -b;
        }
        while (b > 0){
            if (b & 1 == 1) res *= x;
            x *= x;
            b >>= 1;
        }
        return res;
    }
};
