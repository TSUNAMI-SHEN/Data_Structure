//旋转数组的最小数字
//方法1：因为原来数组是升序的，所以旋转后，最小值的位置前后逆序的元素所在的位置
class Solution {
public:
    int minArray(vector<int>& numbers) {
        int n = numbers.size() - 1;
        int res = numbers[0];
        for (int i = 1; i <= n; i++)
        {
            if (numbers[i] < numbers[i-1])
            {
                res = numbers[i];
            }
        }
        return res;
    }
};

//二分法查找
class Solution {
public:
    int minArray(vector<int>& numbers) {
        int i = 0, j = numbers.size() - 1;
        while(i < j)
        {
            int m = (i + j) / 2;
            if (numbers[m] > numbers[j]) i = m + 1;
            else if (numbers[m] < numbers[j]) j = m;
            else j--;
        }
        return numbers[i];
    }
};
