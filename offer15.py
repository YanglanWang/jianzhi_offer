# import create_listNode

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_lianbiao(ll):
    if len(ll)==0:
        return None
    a = ListNode(ll[0])
    if len(ll)==1:
        return a
    a.next=create_lianbiao(ll[1:])
    return a


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
pHead=create_lianbiao([1,2,3])
b=a.ReverseList(pHead)
print(b)