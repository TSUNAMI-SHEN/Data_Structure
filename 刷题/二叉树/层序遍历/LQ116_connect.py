"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# 层次遍历
# 在单层遍历的时候记录一下本层的头部节点，然后在遍历的时候让前一个节点指向本节点就可以了
# 链表法
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        first = root
        while first:
            cur = first
            while cur:  # 遍历一层的节点
                if cur.left: cur.left.next = cur.right      # 找左节点的next
                if cur.right and cur.next: cur.right.next = cur.next.left   # 找右节点的next
                cur = cur.next  # cur同层移动到下一结点
            first = first.left  # 从本层拓展到下一层
        return root
   
