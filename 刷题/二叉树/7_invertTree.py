# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归法
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left

        return root

# 深度优先算法
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        st = []
        st.append(root)

        while st:
            node = st.pop()

            node.left, node.right = node.right, node.left
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        
        return root

# 广度优先算法
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        
        from collections import deque
        que =  deque()

        if root:
            que.append(root)
        
        while que:
            size = len(que)
            for i in range(size):
                node = que.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return root
