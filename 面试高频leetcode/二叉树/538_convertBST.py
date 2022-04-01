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
        self.traversal(root)
        return root

    def traversal(self, root):
        # 采用后序遍历，逐渐累加
        
        # 终止条件，遇到空节点返回None
        if not root:
            return None
        
        # 单层逻辑
        self.traversal(root.right)

        # self.pre记录之前节点的总和
        root.val += self.pre.val
        self.pre = root

        self.traversal(root.left)    
