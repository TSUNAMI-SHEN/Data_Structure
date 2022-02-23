# 将字符串分成两段，前后两端分别翻转，最后再将整段字符串进行翻转
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:

        s = list(s)
        self.reverse_string(s, 0, n-1)
        self.reverse_string(s, n, len(s)-1)
        self.reverse_string(s, 0, len(s)-1)
        return ''.join(s)


    def reverse_string(self, s, left, right):
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return None
