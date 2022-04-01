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
        
        # 终止条件，如果节点为空&当前节点等于p或q，则root即为祖先节点
        if not root or root == p or root == q:
            return root
        
        # 单层逻辑，采用后序遍历，因为需要从下往上遍历
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果left和right都不为空，即在左右子树里分别存在p、q，那么返回root
        if left and right:
            return root
        
        # 如果left不为空，right为空，说明root在left里
        if left:
            return left
        
        return right
