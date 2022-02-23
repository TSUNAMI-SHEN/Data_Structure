# 创建一个长度为26的哈希表，将元素出现的次数记录在对应的索引下面
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in range(len(s)):
            record[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            record[ord(s[i]) - ord('a')] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
                break
        return True
