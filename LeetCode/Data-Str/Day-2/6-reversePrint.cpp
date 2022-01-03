//从尾到头打印链表：输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）
//1.辅助栈的方法：遍历链表，逐次将元素压入辅助栈中，然后依次输出栈顶元素
class Solution {
public:
    vector<int> reversePrint(ListNode* head) {
        stack<int> s;
        while(head != nullptr){
            s.push(head->val);
            head = head->next;
        }
        vector<int> res;
        while(!s.empty()){
            res.push_back(s.top());
            s.pop();
        }
        return res;
    }
};

//2.递归方法：递归至链表末端，回溯时依次将节点值加入列表
class Solution {
public:
    vector<int> reversePrint(ListNode* head) {
        recur(head);
        return res;
    }
private:
    vector<int> res;
    void recur(ListNode* head) {
        if(head == nullptr) return;
        recur(head->next);
        res.push_back(head->val);
    }
};
