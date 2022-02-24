# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归法
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def isornot(root, targetsum) -> bool:
            if not root.left and not root.right and targetsum == 0:
                return True
            if not root.left and not root.right and targetsum != 0:
                return False
            
            if root.left:
                targetsum -= root.left.val  # 左节点
                if isornot(root.left, targetsum): return True   # 递归，处理左节点
                targetsum += root.left.val  # 回溯
            if root.right:
                targetsum -= root.right.val # 右节点
                if isornot(root.right, targetsum): return True     # 递归，处理右节点
                targetsum += root.right.val # 回溯
            return False

        if root == None:
            return False
        else:
            return isornot(root, targetSum - root.val)
          
# 迭代，层序遍历
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = []
        stack.append([root, root.val])

        while stack:
            cur_node, path_sum = stack.pop()

            if not cur_node.left and not cur_node.right and path_sum == targetSum:    # 叶子节点，判断路径值与target是否相等
                return True
            
            if cur_node.left:
                stack.append([cur_node.left, path_sum+cur_node.left.val])
            
            if cur_node.right:
                stack.append([cur_node.right, path_sum+cur_node.right.val])
            
        return False
