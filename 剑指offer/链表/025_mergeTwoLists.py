# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        
        # 两个链表都非空的情况
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        # 若l1链表还非空，则直接加到后面链表上
        if l1:
            cur.next = l1
        
        # 若l2链表还非空，则直接加到后面链表上
        if l2:
            cur.next = l2
        
        return dummy.next
