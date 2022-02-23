class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0:
            return False
        nxt = [0] * len(s)
        nxt =self.getNext(nxt, s)
        if nxt[-1] != -1 and len(s) % (len(s) - (nxt[-1]+1)) == 0:
            return True
        return False

    def getNext(self, nxt, s):
        nxt[0] = -1
        j = -1
        for i in range(1,len(s)):
            while j >= 0 and s[j+1] != s[i]:
                j = nxt[j]
            if s[j+1] == s[i]:
                j += 1
            nxt[i] = j
        return nxt


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return self.kmp(s+s, s)

    def kmp(self, query: str, pattern: str) -> bool:
        n, m = len(query), len(pattern)
        fail = [-1] * m
        for i in range(1, m):
            j = fail[i-1]
            while j >= 0 and pattern[j+1] != pattern[i]:
                j = fail[j]
            if pattern[j+1] == pattern[i]:
                j += 1
            fail[i] = j
        match = -1
        for i in range(1, n-1):
            while match >= 0 and pattern[match+1] != query[i]:
                match = fail[match]
            if pattern[match+1] == query[i]:
                match += 1
            if match == m - 1:
                return True
        return False
    
