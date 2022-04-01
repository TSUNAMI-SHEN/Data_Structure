# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 找到插入节点的父节点，再与父节点的值进行比较，小于父节点的值则加在左子树，否则加在右子树上
        if not root:
            return TreeNode(val)
        
        parent = None
        cur = root

        while cur:
            # 利用二叉搜索树的性质，判断cur.val和val
            parent = cur
            if cur.val > val:
                cur = cur.left
            elif cur.val < val:
                cur = cur.right

        if parent.val > val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        
        return root

