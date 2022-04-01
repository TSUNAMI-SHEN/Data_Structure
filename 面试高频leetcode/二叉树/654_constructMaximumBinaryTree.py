# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.construct(nums, 0, len(nums))

    def construct(self, nums, left, right):
        if left == right:
            return
        
        # 先找到最大值
        max_index = left
        for i in range(left+1, right):
            if nums[i] > nums[max_index]:
                max_index = i
        
        # 以当前最大值构造中节点
        root = TreeNode(nums[max_index])
        # 分治，构造左右子树
        root.left = self.construct(nums, left, max_index)
        root.right = self.construct(nums, max_index+1, right)

        return root
