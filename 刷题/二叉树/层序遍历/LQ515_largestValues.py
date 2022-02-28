# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        if not root:
            return results
        
        from collections import deque
        que = deque([root])
        
        while que:
            list1 = []
            length = len(que)

            for _ in range(length):
                node = que.popleft()
                list1.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            results.append(max(list1))
        return results
