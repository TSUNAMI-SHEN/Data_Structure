# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res = []

        def traversal(root):
            # 终止条件，遇到空节点，或者遍历到第k个点
            if not root:
                return

            if self.k == 0:
                return

            traversal(root.right)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            traversal(root.left)

        self.k = k
        traversal(root)

        return self.res
