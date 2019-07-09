# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        pStart = pHead
        while pHead != None:
            pNew = RandomListNode(pHead.val, pHead.next, None)
            pHead.next = pNew
            pHead = pHead.next.next
        pHead = pStart
        while pHead != None:
            if pHead.random != None:
                pHead.next.random = pHead.random.next
            else:
                pHead = pHead.next
        pHead = pStart
        t = 0
        pCopy = pHead.next
        pCopystart = pCopy
        while pCopy.next != None:
            if t % 2 == 0 and t > 1:
                pHead.next = pHead.next.next
                pHead = pHead.next
            if t % 2 == 1 and t > 1:
                pCopy.next = pCopy.next.next
                pCopy = pCopy.next
            t += 1
        return pCopystart

a=Solution()
a.Clone([1,2,3,4])


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return None
        pStart = pHead
        while pHead != None:
            pNew = RandomListNode(pHead.label)
            pNew.next = pHead.next
            pHead.next = pNew
            pHead = pHead.next.nejavascript:void(0);
            xt
        pHead = pStart
        while pHead != None:
            if pHead.random != None:
                pHead.next.random = pHead.random.next
            pHead = pHead.next.next

        pHead = pStart
        pCopy = pHead.next
        pCopystart = pCopy
        while pCopy.next != None:
            pHead.next = pHead.next.next
            pHead = pHead.next
            pCopy.next = pCopy.next.next
            pCopy = pCopy.next
        return pCopystart