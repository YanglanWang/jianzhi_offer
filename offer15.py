import create_lianbiao

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution:
    def ReverseList(self, pHead):
        # write code here
        if pHead==None or pHead.next==None:
            return pHead
        #last=None
        #while pHead!=None:
        #    tmp=pHead.next
        #    pHead.next=last
        #    last=pHead
        #    pHead=tmp
        #return last
        pHead_new=self.ReverseList(pHead.next)
        pHead.next.next=pHead
        pHead.next=None

        return pHead_new




a=Solution()
pHead=create_lianbiao.create_lianbiao([1,2,3])
b=a.ReverseList(pHead)
print(b)