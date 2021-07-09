# -*- coding: utf-8 -*-
# @File  : leet_02.py
# @Author: FanyFull
# @Date  : 2021/7/9

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        tmp = res
        carry = 0
        while l1 != None and l2 != None:
            tmp.next = ListNode()
            tmp = tmp.next
            tmp.val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
        l3 = l1 if l1 != None else l2
        while l3 != None:
            tmp.next = ListNode()
            tmp = tmp.next
            tmp.val = (l3.val + carry) % 10
            carry = (l3.val + carry) // 10
            l3 = l3.next
        if carry != 0:
            tmp.next = ListNode()
            tmp = tmp.next
            tmp.val = carry
        return res.next

class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode()
        # 用 p 和 q 以将 l1 和 l2 保护起来
        p = l1
        q = l2
        curr = dummy_head
        carry = 0
        while p != None or q != None:
            x = p.val if p != None else 0
            y = q.val if q != None else 0
            sum = carry + x + y
            carry = sum // 10
            curr.next = ListNode(sum % 10, None)
            curr = curr.next
            if p != None:
                p = p.next
            if q != None:
                q = q.next
        if carry > 0:
            curr.next = ListNode(carry, None)
        return dummy_head.next

if __name__ == '__main__':
    # solution = Solution()
    solution = Solution2()
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))
    res = solution.addTwoNumbers(l1, l2)
    while res != None:
        print(res.val, end=' ')
        res = res.next
    print('\n-------')
    l1 = ListNode(0, None)
    l2 = ListNode(0, None)
    res = solution.addTwoNumbers(l1, l2)
    while res != None:
        print(res.val, end=' ')
        res = res.next
    print('\n------')
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9 ,None)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
    res = solution.addTwoNumbers(l1, l2)
    while res != None:
        print(res.val, end=' ')
        res = res.next
