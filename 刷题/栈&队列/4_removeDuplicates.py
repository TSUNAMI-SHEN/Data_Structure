# 利用栈解决
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list()
        for item in s:
            if res and res[-1] == item:
                res.pop()
            else:
                res.append(item)
        return "".join(res)
        
# 使用双指针方法
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        slow = fast = 0
        length = len(s)

        while fast < length:
            res[slow] = res[fast]

            if slow > 0 and res[slow] == res[slow-1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
        return ''.join(res[0:slow])
