# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # 终止条件，遇到空节点返回0
        if not root:
            return 0
        # 单层逻辑，节点数=左子树的节点数+右子树的节点数+1（当前节点）
        left_num = self.countNodes(root.left)
        right_num = self.countNodes(root.right)

        return 1 + left_num + right_num
