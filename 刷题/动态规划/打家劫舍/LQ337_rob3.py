# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        result = self.robTree(root)
        return max(result[0], result[1])
        

    def robTree(self, node):
        # 树形DP
        if node is None:
            return (0,0)    # 空节点时，偷不偷都返回0
        
        left = self.robTree(node.left)
        right = self.robTree(node.right)

        # 分两种情况考虑，偷当前节点&不偷当前节点
        val1 = node.val + left[1] + right[1]    # 偷当前节点，则不能偷子节点
        val2 = max(left[0], left[1]) + max(right[0], right[1])  # 不偷当前节点，子节点可偷也可不偷（左右节点都是），取其中较大的
        return (val1, val2)
