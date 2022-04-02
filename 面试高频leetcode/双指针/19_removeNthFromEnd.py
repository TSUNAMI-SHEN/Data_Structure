# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 设置一个虚拟节点，方便删除操作
        dummy = ListNode()
        dummy.next = head

        fast = dummy
        slow = dummy

        # 快指针先走n步
        while n > 0:
            fast = fast.next
            n -= 1
        
        # 同时移动fast和slow，直至fast为空
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next
