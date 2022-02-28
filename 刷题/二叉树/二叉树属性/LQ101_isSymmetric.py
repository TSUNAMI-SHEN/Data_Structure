# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归法
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)
    
    def compare(self, left, right):
        # 排除空节点情况
        if left == None and right != None: return False
        elif left != None and right == None: return False
        elif left == None and right == None: return True
        elif left.val != right.val: return False

        # 单层的逻辑
        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        isSame = outside and inside

        return isSame
# 队列迭代的方法，按照比较顺序添加节点，然后进行两两比较即可，用栈也可以实现
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        from collections import deque
        que = deque()
        que.append(root.left)
        que.append(root.right)
        while que:
            leftNode = que.popleft()
            rightNode = que.popleft()
            if not leftNode and not rightNode:
                continue
            
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            que.append(leftNode.left)
            que.append(rightNode.right)
            que.append(leftNode.right)
            que.append(rightNode.left)
        return True
