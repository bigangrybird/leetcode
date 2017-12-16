#!/usr/bin/python
#coding=utf8
"""
# Author: qwqian
# Created Time : 2017-12-16 16:15:39

# File Name: add2Nums.py
# Description:

"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        lo = p = l1
        more = 0
        while l1 and l2:
            p.val = l1.val + l2.val + more
            l1 = l1.next
            l2 = l2.next
            more = p.val / 10
            p.val %= 10
            q = p
            p = p.next

        if l2:
            p = l2
            q.next = p

        while more:
            if not p:
                p = ListNode(0)
                q.next = p

            p.val = p.val + more
            more = p.val / 10
            p.val %= 10
            q = p
            p = p.next

        return lo
