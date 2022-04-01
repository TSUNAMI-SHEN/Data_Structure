# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 记录节点、节点的深度以及节点的位置
        que = [(root, 0, 0)]

        cur_depth = left = ans = 0
        for node, depth, pos in que:
            if node:
                que.append((node.left, depth+1, pos*2))     # 往左子树走的话，左孩子节点pos是当前节点pos的两倍
                que.append((node.right, depth+1, pos*2+1))  # 往右子树走的话，右孩子节点pos是当前节点pos的两倍加1
                # 判断是否在当前层，如果在则left更新为节点的pos
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                ans = max(pos-left+1, ans)
        return ans
            
