# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归的方法
# 如果左子树为空，右子树不为空，说明最小深度是 1 + 右子树的深度
# 右子树为空，左子树不为空，最小深度是 1 + 左子树的深度
# 如果左右子树都不为空，返回左右子树深度最小值 + 1 
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # if not root:
        #     return 0
        # if not root.left and not root.right:    # 根节点的左右孩子都为空
        #     return 1
        
        # min_depth = 10 ** 6

        # if root.left:
        #     min_depth = min(self.minDepth(root.left), min_depth)
        # if root.right:
        #     min_depth = min(self.minDepth(root.right), min_depth)
        # return min_depth + 1

        if root == None:
            return 0

        que = [(root, 1)]

        while que:
            cur, depth = que.pop(0)
            # 没有左右孩子，就是这一层了
            if cur.left == None and cur.right == None:
                return depth
            if cur.left:
                que.append((cur.left, depth+1))
            if cur.right:
                que.append((cur.right, depth+1))
        
        return 0
