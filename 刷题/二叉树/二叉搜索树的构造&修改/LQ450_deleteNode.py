# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 有五种情况
        # 第一种情况：如果没找到删除的节点，遍历到空节点直接返回了
        if not root: return root
        if root.val == key:
            # 第二种情况，左右孩子都为空，则直接删除即可
            if not root.left and not root.right:
                del root
                return None
            # 第三种情况，左孩子为空，右孩子不为空，则右孩子补位即可，返回右孩子为根结点
            elif not root.left and root.right:
                tmp = root
                root = root.right
                del tmp
                return root
            # 第四种情况，右孩子为空，左孩子不为空，则左孩子补位，返回左孩子为根结点
            elif root.left and not root.right:
                tmp = root
                root = root.left
                del tmp
                return root
            # 第五种情况，左右孩子都不为空
            else:
                v = root.right
                while v.left:
                    v = v.left
                v.left = root.left
                tmp = root
                root = root.right
                del tmp
                return root
        
        if root.val > key: root.left = self.deleteNode(root.left, key)      # 左递归
        if root.val < key: root.right = self.deleteNode(root.right, key)    # 右递归
        return root
