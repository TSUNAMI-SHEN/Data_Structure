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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        first = root
        while first:    # 遍历每一层
            dummyHead = Node(None)
            tail = dummyHead
            cur = first
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right   # 这一步将左右节点连接起来
                    tail = tail.next        # 最后传递到该层的尾节点
                cur = cur.next              # cur同层移动到下一结点
            first = dummyHead.next          # 此处为换行操作，更新到下一层
        return root
