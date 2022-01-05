//03-找出数组中重复的数字
//Way-1：先进行排序，则重复数字必然相邻，遍历比较前后元素即可得到重复元素
class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        int res = 0;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for (int i = 1; i < n; i++)
        {
            if (nums[i] == nums[i-1])
            {
                res = nums[i];
            }
        }
        return res;
    }
};

//Way-2：创建哈希表，若元素存在则为true，存入哈希表中，若找到重复元素则返回
class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        unordered_map<int, bool> map;
        for (int num : nums)
        {
            if(map[num]) return num;
            map[num] = true;
        }
        return -1;
    }
};

//Way-3：原地交换的方法，将nums中的元素交换到相应索引位置
class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        int i = 0;
        while(i < nums.size())
        {
            if (nums[i] == i)
            {
                i++;
                continue;
            }
            if (nums[nums[i]] == nums[i])
            {
                return nums[i];
            }
            swap(nums[i], nums[nums[i]]);
        }
        return -1;
    }
};
