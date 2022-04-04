# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.merge(lists, 0, len(lists)-1)
    
    # 归并排序合并两个列表
    def mergeTwoLists(self, a: ListNode, b: ListNode):
        dummyHead = ListNode(-1)
        cur = dummyHead

        while a and b:
            if a.val < b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next
        cur.next = a if a else b
        return dummyHead.next
    
    # 不断划分列表，递归合并
    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        
        if left > right:
            return None
        
        mid = (left + right) // 2
        return self.mergeTwoLists(self.merge(lists, left, mid), self.merge(lists, mid+1, right))
