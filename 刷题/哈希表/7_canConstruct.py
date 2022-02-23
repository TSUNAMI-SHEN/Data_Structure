class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0] * 26

        for i in range(len(magazine)):
            arr[ord(magazine[i]) - ord('a')] += 1
        
        for i in range(len(ransomNote)):
            arr[ord(ransomNote[i]) - ord('a')] -= 1

            if arr[ord(ransomNote[i]) - ord('a')] < 0:  # 遇到匹配的删除，若最后ransomNote中还有剩余，说明不符合要求
                return False
        return True
