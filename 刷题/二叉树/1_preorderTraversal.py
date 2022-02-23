# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traversal(root:TreeNode):
            if root == None:  # 递归终止条件，当遇到叶子结点
                 return
            result.append(root.val)   # 处理单层的逻辑，中左右的顺序
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return result 
