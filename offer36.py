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
#     def FindFirstCommonNode(self, pHead1, pHead2):
#         if pHead1==None or pHead2==None:
#             return None
#         p1=pHead1
#         p2=pHead2
#         while p1!=p2:
#             if p1!=None:
#                 p1=p1.next
#             else:
#                 p1=pHead2
#             if p2!=None:
#                 p2=p2.next
#             else:
#                 p2=pHead1
#         return p1
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1==None or pHead2==None:
            return None
        p1,p2=pHead1,pHead2
        while p1!=p2:
           p1=p1.next if p1.next!=None else pHead2
           p2=p2.next if p2.next!=None else pHead1
        return p1

a=Solution()
p1=create_lianbiao([1,2,4,6,8])
p2=create_lianbiao([5,3])
index=3
i=0
p1_start=p1
while i<index:
    p1_start=p1_start.next
    i+=1
p2_start=p2
while p2_start.next!=None:
    p2_start=p2_start.next
p2_start.next=p1_start


c=a.FindFirstCommonNode(p1,p2)
print(c)