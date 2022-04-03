class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 归并排序利用了分治的思想来对序列进行排序。
        # 对一个长为n的待排序的序列，我们将其分解成两个长度为n/2的子序列
        # 每次先递归调用函数使两个子序列有序，然后我们再线性合并两个有序的子序列使整个序列有序
        self.merge_sort(nums, 0, len(nums)-1)
        return nums

    def merge_sort(self, nums, l, r):
        if l == r:
            return
        mid = (l + r) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid+1, r)

        # 创建一个临时数组用来接收排序的元素
        tmp = []
        i = l
        j = mid+1
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l:r+1] = tmp
        
