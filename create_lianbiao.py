class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random=None

def create_lianbiao(ll):
    if len(ll)==0:
        return None
    a = ListNode(ll[0])
    if len(ll)==1:
        return a
    a.next=create_lianbiao(ll[1:])
    return a

global node_list
node_list=[]
def create_lianbiao_for_random(ll):
    if len(ll)==0:
        return None
    a = ListNode(ll[0])
    node_list.append(a)
    if len(ll)==1:
        return a
    a.next=create_lianbiao_for_random(ll[1:])
    return a

def create_random_lianbiao(ll1,ll2):
    lian1=create_lianbiao_for_random(ll1)
    START=lian1
    i=0
    while lian1!=None:
        if ll2[i]!=None:
            lian1.random=node_list[ll2[i]]
        lian1=lian1.next
        i+=1
    return START
