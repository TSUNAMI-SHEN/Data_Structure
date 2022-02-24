# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 后序数组的最后一个元素为切割点，先切中序数组，根据中序数组，反过来切后序数组
        # 一层一层切下去，每次后序数组最后一个元素就是节点元素
        # 切割时中序数组和后序数组对应两部分的长度相等

        if not postorder:       # 特殊情况，树为空——递归终止
            return None
        
        # 第二步：后序遍历的最后一个节点就是当前的中间节点
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 第三步：找切割点
        separate_idx = inorder.index(root_val)

        # 第四步：进行切割inorder
        inorder_left = inorder[:separate_idx]
        inorder_right = inorder[separate_idx+1:]

        # 第五步：切割postorder
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):len(postorder)-1]

        # 第六步：递归
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root
