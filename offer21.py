# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        pushTep=[]
        if pushV==None:
            return False
        if popV==None:
            return False
        pushTep.append(pushV[0])
        pushV.pop(0)
        while len(pushTep)!=0:
            if len(pushV)!=0:
                while pushTep[-1]!=popV[0] :
                    pushTep.append(pushV[0])
                    pushV.pop(0)
                popV.pop(0)
                pushTep.pop(-1)
            else:
                while pushTep and pushTep[-1]==popV[0]:
                    pushTep.pop(-1)
                    popV.pop(0)
                if pushTep and pushTep[-1]!=popV[0]:
                    return False
        return True


a=Solution()
pushV,popV=[1,2,3,4,5],[4,5,3,2,1]
b=a.IsPopOrder(pushV,popV)
print(b)