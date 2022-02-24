# 递归法
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.compare(p, q)

    def compare(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        elif not tree1 and tree2:
            return False
        elif tree1 and not tree2:
            return False
        elif tree1.val != tree2.val:
            return False

        leftSide = self.compare(tree1.left, tree2.left)
        rightSide = self.compare(tree1.right, tree2.right)
        isSame = leftSide and rightSide
        return isSame
