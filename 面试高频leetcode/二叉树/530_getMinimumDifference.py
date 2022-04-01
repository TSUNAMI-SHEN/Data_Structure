# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # stack = []
        # cur = root
        # pre = None  # 需要有一个pre节点记录一下当前节点的前一节点，从而计算差值
        # result = float("inf")

        # while cur or stack:
        #     if cur:
        #         stack.append(cur)
        #         cur = cur.left  # 中序遍历，先将左节点都压入栈
        #     else:
        #         cur = stack.pop()   # 出栈，即输出中间节点
        #         if pre:
        #             result = min(result, cur.val - pre.val)
        #         pre = cur
        #         cur = cur.right # 最后压入右节点
        # return result

        st = []
        cur = root
        pre = None
        result = float('inf')

        while cur or st:
            if cur:
                st.append(cur)
                cur = cur.left
            else:
                cur = st.pop()
                if pre:
                    result = min(result, cur.val - pre.val)
                pre = cur
                cur = cur.right
            
        return result
