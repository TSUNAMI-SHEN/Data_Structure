# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 终止条件，遇到空节点&节点的值等于目标值，返回该节点
        if not root or root.val == val:
            return root
        
        # 单层逻辑
        # 如果当前节点的值小于目标值，则往右子树搜索
        if root.val < val:
            return self.searchBST(root.right, val)
        # 如果当前节点的值大于目标值，则往左子树搜索
        if root.val > val:
            return self.searchBST(root.left, val)
        
