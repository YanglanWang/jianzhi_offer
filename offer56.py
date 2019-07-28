# -*- coding:utf-8 -*-
import create_listNode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        # value = {}
        # pTimes = pHead
        # while pTimes != None:
        #     if pTimes.val not in value.keys():
        #         value[pTimes.val] = 1
        #     else:
        #         value[pTimes.val] += 1
        #     pTimes = pTimes.next
        #
        # pTimes = pHead
        # pleft = None
        # while pTimes != None:
        #     if value[pTimes.val] > 1:
        #         if pleft == None:
        #             pTimes = pTimes.next
        #             pHead = pTimes
        #         else:
        #             pleft.next = pTimes.next
        #             pTimes = pTimes.next
        #     else:
        #         pleft = pTimes
        #         pTimes = pTimes.next
        # return pHead
        if pHead==None:
            return None
        if pHead.next==None:
            return pHead
        while pHead!=None and pHead.next!=None:
            if pHead.next.val==pHead.val:
                while pHead.next!=None and pHead.next.val==pHead.val:
                    pHead=pHead.next
                pHead=pHead.next
            else:
                break
        if pHead==None:
            return None
        pHead.next=self.deleteDuplication(pHead.next)
        return pHead

a=Solution()
pHead=create_listNode.create_lian([1,1,1,1,1],None)

b=a.deleteDuplication(pHead)
while b!=None:
    print(b.val)
    b=b.next