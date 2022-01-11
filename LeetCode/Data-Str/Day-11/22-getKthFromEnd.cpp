//链表中倒数第k个节点
//构建距离为k的双指针，然后遍历链表，当前面的节点为末节点时，后面的节点即是从末节点开始的倒数第k个节点
class Solution {
public:
    ListNode* getKthFromEnd(ListNode* head, int k) {
        ListNode *former = head, *latter = head;
        for (int i = 0; i < k; i++)
        {
            if(former == nullptr) return nullptr;
            former = former->next;
        }
        while (former != nullptr)
        {
            former = former->next;
            latter = latter->next;
        }
        return latter;
    }
};
