# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 利用BST中序遍历特性，把树压缩成数组
        # 比较左子树所有节点小于中间节点，右子树所有节点大于中间节点
        candidate_list = []

        def traversal(root: TreeNode) -> None:
            nonlocal candidate_list
            if not root:
                return 
            traversal(root.left)
            candidate_list.append(root.val)
            traversal(root.right)
        
        def is_sorted(nums: list) -> bool:
            for i in range(1, len(nums)):
                if nums[i] <= nums[i-1]:
                    return False
            return True

        traversal(root)
        return is_sorted(candidate_list)
      
# 递归做法，BST的中序遍历节点数值是从小到大的
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        cur_max = -float("INF")

        def __isValidBST(root: TreeNode) -> bool:
            nonlocal cur_max

            if not root:
                return True
            
            is_left_valid = __isValidBST(root.left)
            if cur_max < root.val:
                cur_max = root.val
            else:
                return False
            is_right_vali = __isValidBST(root.right)

            return is_left_valid and is_right_vali
        return __isValidBST(root)
