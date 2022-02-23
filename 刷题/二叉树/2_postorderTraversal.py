# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traversal(root: TreeNode):
            if root == None:
                return
            traversal(root.left)
            traversal(root.right)
            result.append(root.val)

        traversal(root)
        return result

# 迭代法
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        result = []
        stack = [root]

        while stack:

            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]
