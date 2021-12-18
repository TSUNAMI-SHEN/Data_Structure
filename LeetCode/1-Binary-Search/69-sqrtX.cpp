//二分查找求x的开方
class Solution {
public:
    int mySqrt(int x) {
        int left = 1;
        int right = x;
        int ans = x;
        while (left <= right){
            int mid = left + (right - left) / 2;
            if ((long long)mid * mid <= x)      //小心mid * mid溢出
            {
                ans = mid;
                left = mid + 1;
            }
            
            else
            {
                right = mid - 1;
            }
        }
        return ans;
    }
};
