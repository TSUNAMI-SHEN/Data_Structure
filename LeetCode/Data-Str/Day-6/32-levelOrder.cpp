//从上到下打印二叉树，层序遍历
//借助队列先进先出的特性，访问到当前节点时，先入队列并打印，然后将左右孩子顺序加入队列中
class Solution {
public:
    vector<int> levelOrder(TreeNode* root) {
        vector<int> res;
        if (!root) return res;
        queue<TreeNode*> que;
        que.push(root);
        while(!que.empty())
        {
            TreeNode* node = que.front();
            que.pop();
            res.push_back(node->val);
            if (node->left) que.push(node->left);
            if (node->right) que.push(node->right);
        }
        return res;
    }
};
