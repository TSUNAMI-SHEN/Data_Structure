# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 终止条件，遇到空节点，返回
        if not root:
            return None
        
        # 当前节点的值小于low，则需要删除当前节点的左子树
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        # 当前节点的值大于high，则需要删除当前节点的右子树
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        # 如果当前节点在low-high之内，则对root的左右孩子节点进行裁剪
        if low <= root.val <= high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
