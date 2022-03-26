# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        def dfs(node, cur_num_str):
            
            # 终止条件，如果遇到叶子节点，则直接加上叶子节点的值
            if not node.left and not node.right:
                return int(cur_num_str + str(node.val))
            
            left_sum = dfs(node.left, cur_num_str+str(node.val)) if node.left else 0
            right_sum = dfs(node.right, cur_num_str+str(node.val)) if node.right else 0

            return left_sum + right_sum
        
        return dfs(root, '')
