# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def traversal(root):
            
        #     # 递归终止条件
        #     if not root:
        #         return

        #     # 单层逻辑
        #     traversal(root.left)            
        #     res.append(root.val)
        #     traversal(root.right)

        # traversal(root)
        # return res
            
        res = []    
        st = []

        if root:
            st.append(root)
        
        while st:
            node = st.pop()
            if node != None:
                # 先加入右节点，空节点不入栈
                if node.right:
                   st.append(node.right)

                st.append(node)     # 添加中节点
                st.append(None)     # 中节点访问过了，但是还没处理，加入空节点作为标记

                # 再加入左节点，空节点不入栈
                if node.left:
                    st.append(node.left)
            
            # 遇到空节点时候，下一个节点即之前访问过但未处理的中节点，将其加入结果集中
            else:
                node = st.pop()
                res.append(node.val)
        
        return res
