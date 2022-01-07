//之字形输出层序遍历
//加个判断，当层数为奇数，则从左往右输出；当层数为偶数时，则从右往左输出；层数根据res的size获取
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> que;
        vector<vector<int>> res;
        if (root != NULL) que.push(root);
        while(!que.empty())
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
            if (res.size() % 2 == 1) reverse(tmp.begin(), tmp.end());
            res.push_back(tmp);
        }
        return res;
    }
};
