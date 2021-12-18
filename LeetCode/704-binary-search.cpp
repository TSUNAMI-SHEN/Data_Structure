//二分查找
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int lo = 0;
        int hi = nums.size() - 1;
        while (lo <= hi){
            int mid = (lo + hi) / 2;
            int num = nums[mid];
            if (num == target){
                return mid;
            }
            else if (num < target){
                lo = mid + 1;
            }
            else{
                hi = mid - 1;
            }
        }
        return -1;
    }
};
