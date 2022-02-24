# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root: return None

        if root.val < low:
            return self.trimBST(root.right, low, high)  # 当前节点小于左界：返回右子树，替代左孩子，从而删除左子树整体
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        if low <= root.val <= high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
