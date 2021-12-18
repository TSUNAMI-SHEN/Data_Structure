//Boyer-Moore投票算法
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int maj = 0;
        int count = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (count == 0)
            {
                maj = nums[i];
            }
            if (maj == nums[i])
            {
                count += 1;
            }
            else
            {
                count -= 1;
            }
        }
        return maj;
    }
};
