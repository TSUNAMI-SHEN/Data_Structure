# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        results = []

        if not root:
            return results
        
        from collections import deque
        que = deque([root])

        while que:
            size = len(que)
            sum_ = 0

            for _ in range(size):
                node = que.popleft()
                sum_ += node.val

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                
            results.append(sum_ / size)
        return results
