//二叉搜索树的第k大节点
//二叉搜索树的中序遍历是递增的，则中序遍历逆序的第k个节点即所求的值
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
    int kthLargest(TreeNode* root, int k) {
        this->k = k;
        dfs(root);
        return res;
    }
private:
    int res, k;
    void dfs(TreeNode *root){
        if(root == nullptr) return;
        dfs(root->right);
        if(k==0) return;
        if(--k == 0) res = root->val;   #记录值，若到了第k个，即所求值
        dfs(root->left);
    }
};
