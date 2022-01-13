//合并两个排序的链表
//新建一个空链表，然后依次比较链表的头元素大小，小的插入新的链表中
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* dum = new ListNode(0);
        ListNode* cur = dum;
        while(l1 != nullptr && l2 != nullptr)
        {
            if (l1->val < l2->val)
            {
                cur->next = l1;
                l1 = l1->next;
            }
            else
            {
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }
        cur->next = l1 != nullptr ? l1:l2;
        return dum->next;
    }
};
