# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 递归的方法——无返回值
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 需要一个父节点，来完成赋值
        if not root:
            return TreeNode(val)
        
        parent = None

        def __traverse(cur: TreeNode, val: int) -> None:
            nonlocal parent
            if not cur:
                new_node = TreeNode(val)

                if parent.val > val:    # 如果父节点的值比val大，说明val这个节点需要加在左孩子上
                    parent.left = new_node
                else:
                    parent.right = new_node
                return
            parent = cur
            
            if cur.val < val:       # 如果当前节点值比val小，说明需要在右子树中加上该节点
                __traverse(cur.right, val)
            else:
                __traverse(cur.left, val)
            return
        
        __traverse(root, val)
        return root
        
        
# 递归法——有返回值
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 需要一个父节点，来完成赋值
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
        
        
        
# 迭代法
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)

        parent = None
        cur = root

        while cur:

            if cur.val < val:
                parent = cur
                cur = cur.right
            elif cur.val > val:
                parent = cur
                cur = cur.left
            
        # 跳出循环说明已经找到新的parent节点，直接加入val节点即可
        if parent.val > val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        
        return root
