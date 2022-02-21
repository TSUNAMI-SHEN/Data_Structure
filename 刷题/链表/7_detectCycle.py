# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 1.判断是否有环——在环中相当于追赶问题，slow和fast一定会相遇
# 2.求入口——见notability
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                p = head
                q = slow
                while p != q:
                    p = p.next
                    q = q.next
                return p
        return None
