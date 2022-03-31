# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        return self.traversal(nums, 0, n-1)


        # 中序遍历，中节点为nums的中间点，递归构造其左右子树
    def traversal(self, nums: List[int], left: int, right: int):
        if left > right:
            return None
        
        # 总是选择中间位置左边的数字作为根结点
        mid = left + (right-left) // 2

        node = TreeNode(nums[mid])

        node.left = self.traversal(nums, left, mid-1)
        node.right = self.traversal(nums, mid+1, right)

        return node
        
