# 采用复制新节点，然后再进行链表分离
# 原节点1的随机指针指向原节点3，新节点1的随机指针指向的是原节点3的next
# 原节点3的随机指针指向原节点2，新节点3的随机指针指向的是原节点2的next

# 原节点i的随机指针(如果有的话)，指向的是原节点j，那么新节点i的随机指针，指向的是原节点j的next

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        p = head
        # 第一步，在每个原节点后面创建一个新节点
        # 1->1'->2->2'->3->3'
        while p:
            new_node = Node(p.val,None,None)
            new_node.next = p.next
            p.next = new_node
            p = new_node.next
        p = head
        # 第二步，设置新节点的随机节点
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        # 第三步，将两个链表分离
        p = head
        dummy = Node(-1,None,None)
        cur = dummy
        while p:
            cur.next = p.next
            cur = cur.next
            p.next = cur.next
            p = p.next
        return dummy.next
