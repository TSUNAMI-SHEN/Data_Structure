# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        que = deque()

        if root:
            que.append(root)
        
        while que:
            n = len(que)
            layersum = 0
            for _ in range(n):
                node = que.popleft()
                layersum += node.val
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            res.append(layersum/n)
        return res
