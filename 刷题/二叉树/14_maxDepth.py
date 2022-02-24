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

# 递归法
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getdepth(root)
        
    def getdepth(self, node):   # 参数是需要处理的，传入的是节点
        if not node:    # 终止条件，节点为空
            return 0
        leftdepth = self.getdepth(node.left)
        rightdepth = self.getdepth(node.right)
        depth = 1 + max(leftdepth, rightdepth)  # 单层逻辑：求左、右子树的深度，再取最大值
        return depth    # 返回的是深度值

# N叉树的最大深度，遍历方法
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 0
        for i in range(len(root.children)):
            depth = max(depth, self.maxDepth(root.children[i]))
        return depth+1
