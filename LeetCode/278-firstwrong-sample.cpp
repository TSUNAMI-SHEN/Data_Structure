//二分查找
//若isBadVersion为True，则第一个出错样品在当前判断样本的左侧；否则在当前判断样本的右侧
class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1;
        int right = n;
        while (left < right){
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)){
                right = mid;
            }
            else {
                left = mid + 1;
            }
        }
        return left;
    }
};
