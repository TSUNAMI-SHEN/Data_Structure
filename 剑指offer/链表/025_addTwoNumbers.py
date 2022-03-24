# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 利用栈结构
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = deque([])
        stack2 = deque([])

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        p = None

        while stack1 or stack2 or carry:
            num1 = stack1.pop() if stack1 else 0
            num2 = stack2.pop() if stack2 else 0
            ans = num1 + num2 + carry
            carry = ans // 10
            ans %= 10
            p = ListNode(ans, p)
        
        return p
