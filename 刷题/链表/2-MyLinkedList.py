# 设计链表的五个接口
# 获取链表第index个节点的数值
# 在链表的最前面插入一个节点
# 在链表的最后面插入一个节点
# 在链表第index个节点前面插入一个节点
# 删除链表的第index个节点

class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self._head = ListNode(0)    # 虚拟头部节点
        self._count = 0         # 添加的节点数

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1
        :param index: 需要寻找的index-th节点
        :return: 返回需要找的节点的值
        """
        if 0 <= index <= self._count:
            node = self._head
            for _ in range(index+1):
                node = node.next
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value before the first element of the Linked list. After the insertion, the new node will be the first node
        :param val: 插入的值
        :return:
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list
        :param val: 插入的值
        :return:
        """
        self.addAtIndex(self._count, val)

    def addAtIndex(self, index: int, val:int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked
        list, the node will be appended to the end of linked list. If index is greater than the length, the node will
        not be inserted.
        :param index: 插入的位置
        :param val: 插入的值
        :return:
        """
        if index < 0:
            index = 0
        elif index > self._count:
            return

        # 添加节点后，计数需要累加
        self._count += 1

        add_node = ListNode(val)
        prev_node, cur_node = None, self._head
        for _ in range(index+1):
            prev_node, cur_node = cur_node, cur_node.next
        else:
            prev_node.next = add_node
            add_node.next = cur_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid
        :param index: 需要删除的位置
        :return:
        """
        if 0 <= index <= self._count:
            self._count -= 1
            prev_node, cur_node = None, self._head
            for _ in range(index+1):
                prev_node,  cur_node = cur_node, cur_node.next
            else:
                prev_node.next = cur_node.next
                cur_node.next = None    # 将删除的节点的指针域与后续节点断开
