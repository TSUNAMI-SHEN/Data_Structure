# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 双指针的方法，只需要改变链表的next指针的指向
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur != None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
        
# 递归的方法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # reverse函数是不断的修改cur.next指针的指向，并不断向后移动
        def reverse(pre, cur):
            if not cur:
                return pre
            tmp = cur.next
            cur.next = pre

            return reverse(cur, tmp)
        
        return reverse(None, head)
