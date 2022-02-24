# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 递归法
class Solution:
    def __init__(self):
        self.pre = TreeNode()
        self.count = 0
        self.max_count = 0
        self.result = []
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return None
        self.search_BST(root)
        return self.result


    def search_BST(self, cur: TreeNode) -> None:        # 按照中序遍历的思想
        if not cur:
            return None
        self.search_BST(cur.left)
        # 第一个节点
        if not self.pre:
            self.count = 1
        elif self.pre.val == cur.val:
            self.count += 1     # 如果与前一个结点数值相同，则count+1
        else:
            self.count = 1  # 如果与前一个不相等，则count变为1
        self.pre = cur  # pre更新

        if self.count == self.max_count:
            self.result.append(cur.val)
        if self.count > self.max_count:
            self.max_count = self.count
            self.result = [cur.val]     # 如果最大频率改变了，那么需要先清空之前的result，然后重新记录
        self.search_BST(cur.right)


# 迭代法，中序遍历的思想
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        stack = []
        cur = root
        pre = None
        maxCount, count = 0, 0
        res = []

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre == None:
                    count = 1
                elif cur.val == pre.val:
                    count += 1
                else:
                    count = 1
                if count == maxCount:
                    res.append(cur.val)
                if count > maxCount:
                    maxCount = count
                    res.clear()
                    res.append(cur.val)
                pre = cur
                cur = cur.right
        return res
