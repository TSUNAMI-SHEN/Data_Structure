# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 比较的是节点的高度
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.get_height(root) != -1:
            return True
        else:
            return False

    def get_height(self, root: TreeNode) -> int:
        if not root:
            return 0
        if (left_height := self.get_height(root.left)) == -1:   # -1用来标记是否为平衡二叉树
            return -1
        if (right_height := self.get_height(root.right)) == -1:
            return -1
        if abs(left_height - right_height) > 1:  # 如果左右子树的差值小于等于1，则返回当前二叉树的高度，否则返回-1
            return -1
        else:
            return 1 + max(left_height, right_height)  
