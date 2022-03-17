class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # 超时
        # def compare(s, p):
        #     hash_s = [0] * 26
        #     hash_p = [0] * 26

        #     for i in range(len(s)):
        #         hash_s[ord(s[i])-ord('a')] += 1

        #     for j in range(len(p)):
        #         hash_p[ord(p[j])-ord('a')] += 1
            
        #     for i in range(26):
        #         if hash_p[i] != hash_s[i]:
        #             return False
        #     return True
        
        # res = []

        # for i in range(len(s)-len(p)+1):
        #     if compare(s[i:i+len(p)], p):
        #         res.append(i)
        # return res

        ans = []
        len_p = len(p)
        len_s = len(s)
        if len_p > len_s:
            return ans
        
        map_p = Counter(p)

        for i in range(len_p):
            if s[i] in map_p:
                map_p[s[i]] -= 1
            if max(list(map_p.values())) == 0:
                ans.append(0)


        for p in range(len_p, len_s):
            if s[p] in map_p:
                map_p[s[p]] -= 1
            if s[p-len_p] in map_p:
                map_p[s[p-len_p]] += 1
            if max(list(map_p.values())) == 0:
                ans.append(p-len_p+1)
        
        return ans
