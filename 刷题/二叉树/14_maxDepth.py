# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        results = []
        if not root:
            return 0       
        from collections import deque
        que = deque([root])
        
        while que:
            result = []
            n = len(que)

            for _ in range(n):
                node = que.popleft()
                result.append(node.val) 
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            results.append(result)
        return len(results)   
