"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# 有多个孩子
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        results = []
        if not root:
            return results
        
        from collections import deque
        que = deque([root])

        while que:
            result = []

            for _ in range(len(que)):
                node = que.popleft()
                result.append(node.val)

                if node.children:
                    que.extend(node.children)
            results.append(result)
        return results
