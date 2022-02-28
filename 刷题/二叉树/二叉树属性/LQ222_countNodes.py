# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 利用递归的方法，也可以用层序遍历的方法
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.count(root)
        

    def count(self, node):
        if not node:
            return 0
        leftNum = self.count(node.left)
        rightNum = self.count(node.right)
        allNum = 1 +leftNum + rightNum
        return allNum
