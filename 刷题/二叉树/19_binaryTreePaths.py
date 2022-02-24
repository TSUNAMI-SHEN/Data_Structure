# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归法
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 要做回溯，得先删除节点，然后再加入新的节点
        path = ''
        result = []
        if not root: return result
        self.traversal(root, path, result)
        return result
        
    
    def traversal(self, cur: TreeNode, path: str, result: List[str]) -> None:
        path += str(cur.val)
        # 若当前节点为leave，直接输出
        if not cur.left and not cur.right:
            result.append(path)
        
        if cur.left:
            self.traversal(cur.left, path + '->', result)
        if cur.right:
            self.traversal(cur.right, path + '->', result)

# 迭代法
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = deque([root])
        path_st = deque()
        result = []
        path_st.append(str(root.val))

        while stack:
            cur = stack.pop()
            path = path_st.pop()

            # 如果当前节点为叶子节点，添加路径到结果中
            if not cur.left and not cur.right:
                result.append(path)
            if cur.right:
                stack.append(cur.right)
                path_st.append(path + '->' + str(cur.right.val))        # 每次函数调用完时，path依然是没有加上->的，回溯到上一步再加上
            if cur.left:
                stack.append(cur.left)
                path_st.append(path + '->' + str(cur.left.val))
        return result
