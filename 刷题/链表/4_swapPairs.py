# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 两两交换链表中的元素，图解参考notability
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = ListNode(next=head)   # 设置虚拟头节点
        pre = res
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next

            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next
        return res.next
