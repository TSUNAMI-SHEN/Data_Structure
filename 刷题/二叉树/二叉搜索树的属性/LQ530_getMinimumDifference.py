class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # 将二叉搜索树转换成有序数组，再进行计算
        res = []
        r = float("inf")

        def bulidaList(root):
            if not root:
                return None
            if root.left: bulidaList(root.left)
            res.append(root.val)
            if root.right: bulidaList(root.right)
            return res
        bulidaList(root)
        for i in range(len(res)-1):
            r = min(abs(res[i]-res[i+1]), r)
        return r
      
# 迭代，中序遍历      
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = []
        cur = root
        pre = None  # 需要有一个pre节点记录一下当前节点的前一节点，从而计算差值
        result = float("inf")

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left  # 中序遍历，先将左节点都压入栈
            else:
                cur = stack.pop()   # 出栈，即输出中间节点
                if pre:
                    result = min(result, cur.val - pre.val)
                pre = cur
                cur = cur.right # 最后压入右节点
        return result
