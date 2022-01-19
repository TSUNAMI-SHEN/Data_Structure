//扑克牌中的顺子
//是顺子的条件：1.不存在重复的牌（除了大小王）；2.排序后最大值减最小值（除joker外）要小于5
class Solution {
public:
    bool isStraight(vector<int>& nums) {
        int joker = 0;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size() - 1; i++)
        {
            if(nums[i] == 0) joker++;
            else if(nums[i] == nums[i+1]) return false;
        }
        return nums[4] - nums[joker] < 5;
    }
};
