class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        result = 0
        # 先遍历nums1， 再遍历nums2
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                result = max(result, dp[i][j])
        return result

# 滚动数组的情况
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [0] * (len(nums2)+1)
        result = 0
        
        for i in range(1, len(nums1)+1):
            for j in range(len(nums2), 0, -1):
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = dp[j-1] + 1
                else:
                    dp[j] = 0   # 如果不相等，则dp[j]变为0
                result = max(result, dp[j])
        return result
