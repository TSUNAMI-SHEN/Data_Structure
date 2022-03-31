"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # first指针维护每一层的最左边节点
        first = root

        while first:
            # cur用来遍历一层中的所有节点
            cur = first
            while cur:
                if cur.left: cur.left.next = cur.right
                if cur.right and cur.next: cur.right.next = cur.next.left
                cur = cur.next  # 更新该层中的cur节点
            first = first.left
        
        return root
