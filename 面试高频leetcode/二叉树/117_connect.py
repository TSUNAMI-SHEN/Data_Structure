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

        while first:
            dummyHead = Node(None)      # 为下一行创建一个虚拟头节点，相当于下一行所有节点链表的头节点（每一层都会创建）
            tail = dummyHead            # 为下一行维护一个尾节点指针
            cur = first
            while cur:                  # cur遍历每一层的所有节点
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                
                if cur.right:
                    tail.next = cur.right   # 这一步实现连接
                    tail = tail.next
                
                cur = cur.next              # 同一层移动到下一节点
            first = dummyHead.next          # 此处是换行操作，更新到下一行

        return root
