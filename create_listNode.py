class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def create_lian(list_input,Circle_point_index):
    a = ListNode(list_input[0])
    if Circle_point_index==0:
        circle_point=a
    start=a
    for i in range(1,len(list_input)):
        b=ListNode(list_input[i])
        if i==Circle_point_index:
            circle_point=b
        a.next=b
        a=b
    if Circle_point_index==None:
        a.next=None
    else:
        a.next=circle_point

    return start