# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 将原链表分成大小两个链表，再进行拼接
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        bigHead = ListNode(-1)
        bigTail = bigHead
        smallHead = ListNode(-1)
        smallTail = smallHead

        while head != None:
            if head.val < x:
                smallTail.next = head
                smallTail = head
            else:
                bigTail.next = head
                bigTail = head
            head = head.next
        smallTail.next = bigHead.next
        bigTail.next = None

        return smallHead.next
