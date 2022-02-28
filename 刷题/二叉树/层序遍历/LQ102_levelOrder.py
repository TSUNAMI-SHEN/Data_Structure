# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 广度优先算法
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
        return results
# 递归法，DFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(root, depth):
            if not root: return []  # 终止调节，节点为空
            if len(res) == depth: res.append([])
            # 单层需要处理的逻辑，将当前节点加入队列中，并将左右孩子按左、右顺序加入队列
            res[depth].append(root.val) 
            if root.left: helper(root.left, depth+1)
            if root.right: helper(root.right, depth+1)
        helper(root, 0)
        return res
