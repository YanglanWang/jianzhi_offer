# -*- coding:utf-8 -*-
import create_lianbiao
class RandomListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    # def Clone(self, pHead):
    #     pStart = pHead
    #     while pHead != None:
    #         pNew = RandomListNode(pHead.val, pHead.next, None)
    #         pHead.next = pNew
    #         pHead = pHead.next.next
    #     pHead = pStart
    #     while pHead != None:
    #         if pHead.random != None:
    #             pHead.next.random = pHead.random.next
    #         else:
    #             pHead = pHead.next
    #     pHead = pStart
    #     t = 0
    #     pCopy = pHead.next
    #     pCopystart = pCopy
    #     while pCopy.next != None:
    #         if t % 2 == 0 and t > 1:
    #             pHead.next = pHead.next.next
    #             pHead = pHead.next
    #         if t % 2 == 1 and t > 1:
    #             pCopy.next = pCopy.next.next
    #             pCopy = pCopy.next
    #         t += 1
    #     return pCopystart
    def Clone(self, pHead):
        start=pHead
        while pHead!=None:
            node=RandomListNode(pHead.val)
            node.next=pHead.next
            pHead.next=node
            pHead=pHead.next.next
        pHead=start
        while pHead!=None:
            if pHead.random!=None:
                pHead.next.random=pHead.random.next
            pHead=pHead.next.next
        pOrigin=start
        pHead=start.next
        pFlag=pHead
        while pHead.next!=None:
            pOrigin.next=pOrigin.next.next
            pOrigin=pOrigin.next
            pHead.next=pHead.next.next
            pHead=pHead.next
        pOrigin.next=None
        return pFlag

a=Solution()
b=create_lianbiao.create_random_lianbiao([1,3,8,4],[None,2,0,0])

c=a.Clone(b)
print(c)

# class Solution:
#     # 返回 RandomListNode
#     def Clone(self, pHead):
#         # write code here
#         if pHead == None:
#             return None
#         pStart = pHead
#         while pHead != None:
#             pNew = RandomListNode(pHead.label)
#             pNew.next = pHead.next
#             pHead.next = pNew
#             pHead = pHead.next
#         pHead = pStart
#         while pHead != None:
#             if pHead.random != None:
#                 pHead.next.random = pHead.random.next
#             pHead = pHead.next.next
#
#         pHead = pStart
#         pCopy = pHead.next
#         pCopystart = pCopy
#         while pCopy.next != None:
#             pHead.next = pHead.next.next
#             pHead = pHead.next
#             pCopy.next = pCopy.next.next
#             pCopy = pCopy.next
#         return pCopystart