//对称的二叉树
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        return root == nullptr || recur(root->left, root->right);
    }
private:
    bool recur(TreeNode* L, TreeNode* R)
    {
        if (L == nullptr && R == nullptr) return true;
        if (L == nullptr || R == nullptr || L->val != R->val) return false;
        return recur(L->left, R->right) && recur(L->right, R->left);
    }
};
