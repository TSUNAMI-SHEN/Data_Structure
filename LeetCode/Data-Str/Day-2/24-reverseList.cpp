//反转链表：输入一个链表的头节点，反转该链表并输出反转后链表的头节点
//1.递归的方法：终止条件：cur = nullptr，即越过尾节点；2.递归后继节点；3.修改当前节点cur引用指向前驱节点pre（这一步实现反转，在回溯中执行操作）；4.返回反转链表的头节点res
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        return recur(head, nullptr);
    }
private:
    ListNode * recur(ListNode* cur, ListNode* pre){
        if (cur == nullptr) return pre;
        ListNode* res = recur(cur->next, cur);
        cur->next = pre;
        return res;
    }
};

//2.迭代的方法，原理见notability笔记
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *cur = head, *pre = nullptr;
        while(cur != nullptr){
            ListNode *tmp = cur->next;
            cur->next = pre;
            pre = cur;
            cur = tmp;
        }
        return pre;
    }
};
