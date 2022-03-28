"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # 整体采用中序遍历的框架
        def dfs(cur):
            if not cur: return
            dfs(cur.left)

            if self.pre:
                self.pre.right, cur.left = cur, self.pre    # 修改当前节点的left指向前驱节点，前驱节点的right指向当前节点
            else:
                self.head = cur
            # 更新前驱节点
            self.pre = cur

            dfs(cur.right)

        if not root: return
        self.pre = None     # 指示前驱节点
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
