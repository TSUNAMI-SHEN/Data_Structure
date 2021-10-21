//从前往后逐一比较两个向量末项的大小，较大者填入nums1向量中
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int p1 = m - 1;
    int p2 = n - 1;
    int tail = m + n - 1;
    int cur;
    while(p2 >= 0)
    {
        if (p1 == -1)
        {
            cur = nums2[p2--];
        }
        //p2=-1，即nums2的数组提前耗尽，而本身nums1的数都已经就位，因此可以忽略此步的判断
        // else if (p2 == -1)
        // {
        //     cur = nums1[p1--];
        // }
        else if (nums1[p1] > nums2[p2])
        {
            cur = nums1[p1--];
        }
        else
        {
            cur = nums2[p2--];
        }
        nums1[tail--] = cur;
    }
    }
};
