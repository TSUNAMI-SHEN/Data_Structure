# 递归法
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # 使用前序遍历，然后记录深度最大的叶子节点，此时就是树的最后一行最左边的值
        max_depth = -float("INF")
        leftmost_val = 0

        def traverse(root, cur_depth):
            nonlocal max_depth, leftmost_val
            
            if not root.left and not root.right:
                if cur_depth > max_depth:
                    max_depth = cur_depth
                    leftmost_val = root.val
            if root.left:
                cur_depth += 1  # 深度加1
                traverse(root.left, cur_depth)
                cur_depth -= 1  # 回溯
            if root.right:
                cur_depth += 1
                traverse(root.right, cur_depth)
                cur_depth -= 1
        traverse(root, 0)
        return leftmost_val
        
        
# 层序遍历，找到最后一行，输出第一个元素即可
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        que = deque()
        if root:
            que.append(root)
        result = 0
        while que:
            n = len(que)
            for i in range(n):
                if i == 0:
                    result = que[i].val
                cur = que.popleft()
                
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return result
