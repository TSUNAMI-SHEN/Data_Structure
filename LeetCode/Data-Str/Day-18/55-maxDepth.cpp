//求树的最大深度
//DFS，深度优先搜索，树的最大深度与左右子树的关系为 maxDepth = max(maxDepth(左子树), maxDepth(右子树))+1
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
    int maxDepth(TreeNode* root) {
        if (root == nullptr) return 0;
        return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};

//BFS，广度优先搜索，通过队列实现
//层序遍历，经过一层遍历之后层数+1
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) return 0;
        vector<TreeNode*> que;    //队列que为空时，说明遍历结束
        que.push_back(root);
        int res = 0;
        while(!que.empty()){  
            vector<TreeNode*> tmp;  //临时列表，存储下一层节点
            for(TreeNode* node : que){
                if (node->left != nullptr) tmp.push_back(node->left);
                if (node->right != nullptr) tmp.push_back(node->right);
            }
            que = tmp;
            res++;
        }
        return res;
    }
};
