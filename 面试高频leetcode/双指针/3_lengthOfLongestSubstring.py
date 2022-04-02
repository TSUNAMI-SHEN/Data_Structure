class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashdic用来接收窗口中已有元素
        hashdic = set()
        n = len(s)

        # fast指针表示子串的右边界
        fast = -1
        ans = 0

        for i in range(n):
            # i维护的是子串的左边界，当左边界往右移动一位时，需要除去一个字符
            if i != 0:
                hashdic.remove(s[i-1])
            
            # 不断拓展右边界并判定hashdic是否已经存在该元素
            while fast + 1 < n and s[fast+1] not in hashdic:
                hashdic.add(s[fast+1])
                fast += 1
            
            ans = max(ans, fast-i+1)
        
        return ans

