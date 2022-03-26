# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.s = set()

    def findTarget(self, root: TreeNode, k: int) -> bool:

        # 递归遇到叶子节点仍未找到则返回False
        if root == None:
            return False
        
        # 如果目标值减去当前节点的值在集合中，则说明存在两个节点的值等于k，返回True
        if k - root.val in self.s:
            return True
        
        self.s.add(root.val)

        return self.findTarget(root.left, k) or self.findTarget(root.right, k)
