class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False
        
        map_s1 = Counter(s1)

        for i in range(len_s1):
            if s2[i] in map_s1:
                map_s1[s2[i]] -= 1
            if max(list(map_s1.values())) == 0:
                return True
        
        for p in range(len_s1, len_s2):
            if s2[p] in map_s1:
                map_s1[s2[p]] -= 1
            if s2[p-len_s1] in map_s1:
                map_s1[s2[p-len_s1]] += 1
            if max(list(map_s1.values())) == 0:
                return True
        
        return False
