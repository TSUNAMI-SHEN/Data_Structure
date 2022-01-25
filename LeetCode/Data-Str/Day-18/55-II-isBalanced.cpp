//判断是否为平衡二叉树
//1.先序遍历+判断深度（从顶至底），求出子树的深度，然后进行判断
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if (root == nullptr) return true;
        return abs(maxDepth(root->left) - maxDepth(root->right)) < 2 && isBalanced(root->left) && isBalanced(root->right);
    }
private:
    int maxDepth(TreeNode* root){
        if (root == nullptr) return 0;
        return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};

//2.后序遍历+剪枝（从底至顶），当检测出左右子树高度差大于1直接返回false
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return depth(root) != -1;
    }
private:
    int depth(TreeNode* root){
        if (root == nullptr) return 0;
        int left = depth(root->left);   # 得到左子树的深度
        if (left == -1) return -1;
        int right = depth(root->right);
        if (right == -1) return -1;
        return abs(left - right) <= 1 ? max(left, right) + 1 : -1;  # 进行判断，如果左右子树高度差大于1，则不是平衡树，直接返回false，否则返回左右子树中高度的较大值+1
    }
};
