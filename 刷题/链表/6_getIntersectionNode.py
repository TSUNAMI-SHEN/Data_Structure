# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 类似追赶问题，链表短的指针视为快指针
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        
        pointA = headA
        pointB = headB

        while pointA != pointB:
            if pointA == None:
                pointA = headB
            else:
                pointA = pointA.next
            if pointB == None:
                pointB = headA
            else:
                pointB = pointB.next
        
        return pointB

# 简化版的
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA = headA
        curB = headB

        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        
        return curA
        
