# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        import collections
        res_dic = collections.defaultdict(int)

        def traversal(node):
            if not node:
                return 0

            tmp_sum = traversal(node.left) + node.val + traversal(node.right)
            res_dic[tmp_sum] += 1       # 用来记录每个节点的子树元素和
            return tmp_sum
        
        if not root:
            return []
        
        traversal(root)
        max_cnt = 0
        for cnt in res_dic.values():
            max_cnt = max(max_cnt, cnt)
        return [key for key, cnt in res_dic.items() if cnt==max_cnt]
