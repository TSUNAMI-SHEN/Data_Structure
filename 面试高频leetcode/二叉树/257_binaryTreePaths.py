# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # stack = deque([root])
        # path_st = deque()
        # result = []
        # path_st.append(str(root.val))

        # while stack:
        #     cur = stack.pop()
        #     path = path_st.pop()

        #     # 如果当前节点为叶子节点，添加路径到结果中
        #     if not cur.left and not cur.right:
        #         result.append(path)
        #     if cur.right:
        #         stack.append(cur.right)
        #         path_st.append(path + '->' + str(cur.right.val))
        #     if cur.left:
        #         stack.append(cur.left)
        #         path_st.append(path + '->' + str(cur.left.val))
        # return result
        path = ''
        result = []
        if not root:
            return []
        self.traversal(root, path, result)
        return result
        
    def traversal(self, cur: TreeNode, path: str, result: List[str]) -> None:
        path += str(cur.val)

        # 终止条件
        if not cur.left and not cur.right:
            result.append(path)
        
        # 单层逻辑
        if cur.left:
            self.traversal(cur.left, path+'->', result)
        if cur.right:
            self.traversal(cur.right, path+'->', result)
