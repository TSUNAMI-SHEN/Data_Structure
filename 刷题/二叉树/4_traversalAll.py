# 对待处理的节点做标记
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                if node.right:  # 添加右节点（空节点不入栈）
                    st.append(node.right)

                st.append(node) # 添加中节点
                st.append(None) # 中节点访问过，但是还没处理，加入空节点作为标记
                
                if node.left:   # 添加左节点（空节点不入栈）
                    st.append(node.left)
            else:   # 只有遇到空节点时，才将下一个节点放进结果集
                node = st.pop()
                result.append(node.val)
        return result
