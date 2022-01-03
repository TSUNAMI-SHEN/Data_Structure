/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/
//35-复杂链表的复制
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) return nullptr;
        Node* cur = head;
        //1.复制各节点，并构建拼接链表
        while(cur != nullptr)
        {
            Node* tmp = new Node(cur->val);
            tmp->next = cur->next;
            cur->next = tmp;
            cur = tmp->next;
        }
        //2.构建各新节点的random指向
        cur = head;
        while(cur != nullptr)
        {
            if(cur->random != nullptr)
                cur->next->random = cur->random->next;
            cur = cur->next->next;
        }
        //3.拆分链表
        cur = head->next;
        Node* pre = head, *res = head->next;
        while(cur->next != nullptr)
        {
            pre->next = pre->next->next;
            cur->next = cur->next->next;
            pre = pre->next;
            cur = cur->next;
        }
        pre->next = nullptr;
        return res;
    }
};
