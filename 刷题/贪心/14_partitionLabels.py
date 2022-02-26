class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = [0] * 26
        for i in range(len(s)):
            hash[ord(s[i]) - ord('a')] = i  # 记录每个字母出现的最远边界
        result = []
        left = 0
        right = 0
        for i in range(len(s)):
            right = max(right, hash[ord(s[i]) - ord('a')])  # 这一步比较是说明在切割好的区间内所有字母中最远出现的边界
            if i == right:
                result.append(right - left + 1)
                left = i + 1
            
        return result
