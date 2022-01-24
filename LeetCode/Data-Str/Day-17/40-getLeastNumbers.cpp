//获取数组最小的k个数
//利用快速排序的方法，将数组分成两部分，当划分的哨兵索引等于k时即可以获得最小的k个数
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k) {
        if (k >= arr.size()) return arr;
        return quickSort(arr, 0, arr.size()-1, k);
    }
private:
    vector<int> quickSort(vector<int>& arr, int l, int r, int k){
        int i = l, j = r;
        while (i < j){
            while (i < j && arr[j] >= arr[l]) j--;
            while (i < j && arr[i] <= arr[l]) i++;
            swap(arr[i], arr[j]);
        }
        swap(arr[i], arr[l]);
        if (k < i) return quickSort(arr, l, i-1, k);
        if (k > i) return quickSort(arr, i+1, r, k);
        vector<int> res;
        res.assign(arr.begin(), arr.begin()+k);
        return res;
    }
};
