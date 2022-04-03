import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 快速排序的主要思想：通过划分将待排序的序列分成前后两部分，其中前一部分的数据都比后一部分的数据要小，
        # 然后再递归调用函数对两部分的序列分别进行快速排序，以此整个序列达到有序
        self.randomized_quicksort(nums, 0, len(nums)-1)
        return nums

    def randomized_partition(self, nums, l, r):
        # 随机选取pivot，分界点，目标是partition后pivot左侧元素都比nums[pivot]小，右侧元素都比nums[pivot]大
        pivot = random.randint(l, r)
        # 先将pivot的元素移到nums末尾
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1

        # 遍历[l,r]区间内的元素，将小于pivot的元素往前移
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        
        # 返回pivot的下标
        return i

    # 递归调用函数，对分界点左右两部分进行快速排序
    def randomized_quicksort(self, nums, l, r):
        if l > r:
            return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid-1)
        self.randomized_quicksort(nums, mid+1, r)
    
