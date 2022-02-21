# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 采用双指针的方法，fast指针先走n+1步，从而当fast到链表末尾时，slow指针可以指向指定删除节点的上一节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode()
        dummy_head.next = head
        fast = dummy_head
        slow = dummy_head

        while n != 0:
            fast = fast.next
            n -= 1
        
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy_head.next
