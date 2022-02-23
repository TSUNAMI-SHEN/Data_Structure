# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 将层序遍历结果翻转一下即可
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        results = []
        if not root:
            return results
        from collections import deque
        que = deque([root])

        while que:
            size = len(que)
            result = []
            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)

                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(result)
        
        results.reverse()
        return results
