# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 头插法进行反转链表，参考：https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/fan-zhuan-lian-biao-ii-by-leetcode-solut-teyq/
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head

        for _ in range(left-1):
            pre = pre.next
            cur = cur.next
        
        for _ in range(right-left):
            tmp = cur.next
            cur.next = cur.next.next
            tmp.next = pre.next
            pre.next = tmp
        
        return dummy.next
