//按层输出每一节点
//新建一个临时表tmp，用来存储当前层的打印结果
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        queue<TreeNode*> que;
        int cnt = 0;
        if (root != NULL) que.push(root);
        while (!que.empty())
        {
            vector<int> tmp;
            for (int i = que.size(); i > 0; --i)
            {
                root = que.front();
                que.pop();
                tmp.push_back(root->val);
                if (root->left != NULL) que.push(root->left);
                if (root->right != NULL) que.push(root->right);
            }
            res.push_back(tmp);
        }
        return res;
    }
};
