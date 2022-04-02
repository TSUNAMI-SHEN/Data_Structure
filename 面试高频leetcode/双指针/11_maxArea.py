class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针，从两端不断往内收缩
        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            h = min(height[right], height[left])
            area = max(area, h * (right - left))

            # 保留较高的一边
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area
            
