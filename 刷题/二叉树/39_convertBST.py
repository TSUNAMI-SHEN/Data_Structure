# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = TreeNode()

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 转成有序数组，即从后往前的累加数组
        # 需要定义一个全局变量pre，用来保存cur节点的前一个节点的数值
        self.traversal(root)
        return root

    def traversal(self, root: TreeNode) -> None:
        if not root: return None
        self.traversal(root.right)  # 遍历右节点

        root.val += self.pre.val    # 中节点处理方式，当前的值加上pre的值
        self.pre = root

        self.traversal(root.left)   # 遍历左节点
