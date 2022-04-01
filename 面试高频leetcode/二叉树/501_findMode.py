# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        # 采用中序遍历，利用中序遍历单调的特性，前后比较元素值是否相等
        st = []
        pre = None
        count = 0
        max_count = 0
        res = []

        cur = root

        while cur or st:
            # 先添加左节点
            if cur:
                st.append(cur)
                cur = cur.left
            else:
                cur = st.pop()

                if pre == None:
                    count = 1
                elif pre.val == cur.val:
                    count += 1
                else:
                    count = 1
                
                if count == max_count:
                    res.append(cur.val)

                # 如果count超过了之前的最大max_count，则说明众数元素需要更新
                if count > max_count:
                    max_count = count
                    res.clear()
                    res.append(cur.val)
                pre = cur
                cur = cur.right
        return res
