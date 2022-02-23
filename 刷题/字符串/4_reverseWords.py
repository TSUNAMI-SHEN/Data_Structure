class Solution:
    def reverseWords(self, s: str) -> str:
        l = self.trim_spaces(s)
        self.reverse_string(l, 0, len(l)-1)
        self.reverse_each_word(l)
        return ''.join(l)

        
    # 删除多余的空格
    def trim_spaces(self, s):
        n = len(s)
        left = 0
        right = n - 1

        while left <= right and s[left] == ' ': # 删除开头的空格
            left += 1
        while left <= right and s[right] == ' ':    # 删除结尾的空格
            right -= 1
        
        tmp = []
        while left <= right:        # 删除单词之间的空格
            if s[left] != ' ':
                tmp.append(s[left])
            elif tmp[-1] != ' ':
                tmp.append(s[left])
            left += 1
        return tmp
    
    # 反转字符数组
    def reverse_string(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return None


    # 反转每个单词
    def reverse_each_word(self, nums):
        start = 0
        end = 0
        n = len(nums)
        while start < n:
            while end < n and nums[end] != ' ':     # 先确定单词的长度，再调用反转字符数组的函数进行反转单词
                end += 1
            self.reverse_string(nums, start, end-1)
            start = end + 1
            end += 1
        return None
