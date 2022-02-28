# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def traversal(root: TreeNode):
            if root == None:
                return
            traversal(root.left)
            result.append(root.val)
            traversal(root.right)
        
        traversal(root)
        return result

# 迭代法
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack = []
        cur = root
        while cur or stack:
            # 先迭代访问最底层的左子树节点
            if cur:
                stack.append(cur)
                cur = cur.left
            # 到达最左节点后处理栈顶节点
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right

        return result
