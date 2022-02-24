# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 找到一个节点，发现左子树出现节点p，右子树出现节点q，或者左子树出现q，右子树出现p，那么该节点就是节点p和q的最近公共祖先
        # 需要从下往上遍历——通过后序遍历实现
        # 必须要遍历整棵二叉树，即使已经找到结果了，依然要把其他节点遍历完，因为要使用递归函数的返回值做逻辑判断
        # 如果返回值left为空，right不为空，则返回right传给上一层
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:      # 如果left和right都不为空，那么root即为最近公共节点
            return root
        if left:        # 如果左节点不为空，则返回左子树的
            return left
        return right
