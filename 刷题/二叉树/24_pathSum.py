class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def traversal(cur_node, remain):
            if not cur_node.left and not cur_node.right and remain == 0:
                result.append(path[:])
                return
            if not cur_node.left and not cur_node.right: return

            if cur_node.left:
                path.append(cur_node.left.val)
                remain -= cur_node.left.val
                traversal(cur_node.left, remain)
                path.pop()
                remain += cur_node.left.val   # 这里的回溯不仅要将remain加回去，还需要把路径中的节点也删除

            if cur_node.right:
                path.append(cur_node.right.val)
                remain -= cur_node.right.val
                traversal(cur_node.right, remain)
                path.pop()
                remain += cur_node.right.val
        
        result, path = [], []
        if not root:
            return []
        path.append(root.val)
        traversal(root, targetSum-root.val)
        return result
