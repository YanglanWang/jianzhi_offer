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