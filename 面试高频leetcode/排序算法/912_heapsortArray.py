class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 堆排序思想：先将待排序的序列建成大根堆，使得每个父节点的元素大于等于它的子节点
        # 此时整个序列最大值即为堆顶元素，我们将其与末尾元素交换，使末尾元素为最大值，然后再调整堆顶元素使得剩下的n-1个元素仍为大根堆
        # 重复执行以上操作，即可得到有序的序列
        self.heap_sort(nums)
        return nums
    
    def max_heapify(self, heap, root, heap_len):
        p = root
        while p * 2 + 1 < heap_len:
            # l, r是p的左右节点，取较大者，再与root比较，使root的元素大于子节点元素
            l, r = p * 2 + 1, p * 2 + 2
            if heap_len <= r or heap[r] < heap[l]:      # heap_len <= r 对应于只有左孩子，没有右孩子
                nex = l
            else:
                nex = r
            
            # 如果根节点元素小于孩子元素，则交换
            if heap[p] < heap[nex]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break
    
    # 建立大根堆
    def build_heap(self, heap):
        for i in range(len(heap)-1, -1, -1):
            self.max_heapify(heap, i, len(heap))
    
    def heap_sort(self, nums):
        self.build_heap(nums)
        # 将堆顶元素（即最大值）放到nums的末尾，随后调整剩下的元素使其变成大根堆，重复取最大元素放到最后
        for i in range(len(nums)-1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, 0, i)
    
    
    
        
