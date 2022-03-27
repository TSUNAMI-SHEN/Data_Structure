# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:

        paths = []
        path = []

        def dfs(root, target):
            # 终止条件：遇到叶子节点
            if not root:
                return
            
            # 单层逻辑，先加入当前节点的值
            path.append(root.val)
            target -= root.val
            
            # 如果当前节点无左右孩子（即叶子节点，而且路径和等于target则找到一条路径
            if not root.left and not root.right and target == 0:
                paths.append(path[:])

            dfs(root.left, target)
            dfs(root.right, target)
            
            # 回溯，去掉当前节点
            path.pop()
        
        dfs(root, target)
        return paths
