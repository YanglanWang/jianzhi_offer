
import create_listNode

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None:
            return None
        p1 = pHead
        p2 = pHead.next
        if p2==None:
            return None
        else:
            p2 = p2.next
        while p1 != p2:
            p1 = p1.next
            if p2 == None:
                return None
            else:
                p2 = p2.next
            if p2 == None:
                return None
            else:
                p2 = p2.next

        p1 = p1.next
        n = 1
        while p1 != p2:
            p1 = p1.next
            n += 1
        p1 = pHead
        p2 = pHead
        i = 0
        while i < n:
            p2 = p2.next
            i += 1
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

a=Solution()
pHead=create_listNode.create_lian([1,2],1)
print(a.EntryNodeOfLoop(pHead).val)

