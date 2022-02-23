class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = dict()


        # 收集a+b的元素值及其对应个数
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in hashmap:
                    hashmap[n1+n2] += 1
                else:
                    hashmap[n1+n2] = 1
            
        count = 0
        
        # 若c+d=-a+b则count+1，统计所有的a+b
        for n3 in nums3:
            for n4 in nums4:
                if -n3 - n4 in hashmap:
                    count += hashmap[-n3-n4]
        
        return count
