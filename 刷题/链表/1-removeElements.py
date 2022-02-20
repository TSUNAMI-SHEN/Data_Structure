# 设置虚拟头结点，可以采用统一的逻辑来移除链表的结点
class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next  # 删除cur.next结点
            else:
                cur = cur.next
        return dummy_head.next
