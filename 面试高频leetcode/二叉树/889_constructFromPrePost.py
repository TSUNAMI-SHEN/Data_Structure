# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:   return root

        # 确定左分支的长度，因为数值唯一，所以preorder[1] = postorder[L-1]
        L = postorder.index(preorder[1]) + 1
        root.left = self.constructFromPrePost(preorder[1:L+1], postorder[:L])
        root.right = self.constructFromPrePost(preorder[L+1:], postorder[L:-1])
        return root
