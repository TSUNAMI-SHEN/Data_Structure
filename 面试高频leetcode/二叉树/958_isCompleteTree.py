# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # 采用层序遍历，记录节点的pos
        nodes = [(root, 1)]
        i = 0
        for node, pos in nodes:
            if node:
                nodes.append((node.left, pos*2))        # 左孩子节点的话pos*2
                nodes.append((node.right, pos*2+1))     # 右孩子节点的话pos*2+1
        return nodes[-1][1] == len(nodes)

