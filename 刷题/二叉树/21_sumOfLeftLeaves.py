# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归法
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # 左叶子节点定义：如果左节点不为空，且左节点没有左右孩子，那么这个节点就是左叶子
        # 需要通过节点的父节点判断本节点的属性
        if not root:
            return 0
        left_left_leaves_sum = self.sumOfLeftLeaves(root.left)  # 左子树的左叶子节点
        right_left_leaves_sum = self.sumOfLeftLeaves(root.right)    # 右子树的左叶子节点
        cur_left_leaves_val = 0
        if root.left and not root.left.left and not root.left.right:
            cur_left_leaves_val = root.left.val
        return cur_left_leaves_val + left_left_leaves_sum + right_left_leaves_sum   # 中
      
      
# 迭代法，对左叶子节点进行判断，如果是加上值，其他逻辑与之前的相同
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        stack = []
        if root:
            stack.append(root)
        res = 0

        while stack:
            node = stack.pop()
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        return res
