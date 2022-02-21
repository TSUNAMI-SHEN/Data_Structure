# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 迭代的方法，不断比较两个链表的值，较小的取出，最后直接加入较长的链表剩余的元素
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        pre = dummy_head

        while list1 and list2:

            if list1.val < list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                list2 = list2.next
            
            pre = pre.next
        if list1 != None:
            pre.next = list1
            
        if list2 != None:
            pre.next = list2
        
        return dummy_head.next
