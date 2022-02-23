class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(needle)
        b = len(haystack)
        if a == 0:
            return 0
        next = self.getNext(a, needle)
        p = -1
        for j in range(b):
            while p >= 0 and needle[p+1] != haystack[j]:    # 模式串与文本串出现不匹配，因为前缀表已经往前移一位了，所以只需关注冲突位置即可
                p = next[p]
            if needle[p+1] == haystack[j]:
                p += 1
            if p == a - 1:
                return j-a+1
        return -1

    # def getnext(self,a,needle):
    #     next=['' for i in range(a)]
    #     k=-1
    #     next[0]=k
    #     for i in range(1,len(needle)):
    #         while (k>-1 and needle[k+1]!=needle[i]):
    #             k=next[k]
    #         if needle[k+1]==needle[i]:
    #             k+=1
    #         next[i]=k
    #     return next    
    def getNext(self, a, needle):
        next = ['' for i in range(a)]
        k = -1  # k是前缀末尾，也是i之前的最长相等前后缀的长度
        next[0] = k
        for i in range(1, len(needle)):
            while (k>-1 and needle[k+1]!=needle[i]):
                k = next[k]
            if needle[k+1] == needle[i]:
                k += 1
            next[i] = k
        return next
