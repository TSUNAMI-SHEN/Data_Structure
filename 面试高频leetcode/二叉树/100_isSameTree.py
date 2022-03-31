# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 终止条件
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            # 单层逻辑，比较左右子树是否相等，需要同时成立才返回True（即and连接）
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

