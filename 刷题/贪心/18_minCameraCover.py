# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # 局部最优：让叶子节点的父节点安装尽量少的摄像头
        # 整体最优：全部摄像头数量所用最少
        # 遍历二叉树采用后序遍历，这样可以实现从下往上遍历
        result = 0

        def traversal(cur: TreeNode) -> int:
            nonlocal result

            # 空节点必须是有覆盖的状态
            if not cur:
                return 2

            left = traversal(cur.left)
            right = traversal(cur.right)
            
            # 左右孩子都有覆盖,说明相机在当前节点的孙子节点上，所以返回无覆盖状态
            if left == 2 and right == 2:
                return 0
            
            # 如果左右孩子中一个有覆盖，当前节点必须有摄像头，这样才能使另一个没有被覆盖的孩子覆盖到
            elif left == 0 or right == 0:
                result += 1     # 摄像头+1
                return 1
            
            # 如果左右节点至少有一个摄像头，则当前节点肯定是被覆盖的状态
            elif left == 1 or right == 1:
                return 2
        
        if traversal(root) == 0:
            result += 1
        
        return result

