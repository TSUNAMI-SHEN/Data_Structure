# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:
            return head

        # 统计链表的长度
        cur = head
        n = 1
        while cur.next:
            cur = cur.next
            n += 1
        

        # 如果k是长度的倍数，则直接返回head，add表示原链表的末尾节点到旋转后链表的末尾节点的距离
        add = n - k % n
        if add == n:
            return head
        
        # 将链表变成环，此时cur指向原链表的tail节点
        cur.next = head
        # 找到旋转后链表的tail节点
        while add:
            cur = cur.next
            add -= 1
        # ret是旋转后链表的head节点
        ret = cur.next
        # 将环形链表截断
        cur.next = None

        return ret

        
