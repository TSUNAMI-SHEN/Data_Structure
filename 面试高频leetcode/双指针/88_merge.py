class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1
        l1 = m - 1
        l2 = n - 1

        while l1 >= 0 or l2 >= 0:
            if l1 == -1:
                nums1[p] = nums2[l2]
                l2 -= 1
            elif l2 == -1:
                nums1[p] = nums1[l1]
                l1 -= 1
            elif nums1[l1] > nums2[l2]:
                nums1[p] = nums1[l1]
                l1 -= 1
            else:
                nums1[p] = nums2[l2]
                l2 -= 1
            p -= 1
        

            
