# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归方法
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

# 借助栈结构，迭代方法
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()  # 将当前结点先pop出来
            result.append(node.val)

            # 先进入右节点、再进入左节点，保证出栈时先出左孩子，再出右孩子
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
