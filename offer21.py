# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # # write code here
        # pushTep=[]
        # if pushV==None:
        #     return False
        # if popV==None:
        #     return False
        # pushTep.append(pushV[0])
        # pushV.pop(0)
        # while len(pushTep)!=0:
        #     if len(pushV)!=0:
        #         while pushTep[-1]!=popV[0] :
        #             pushTep.append(pushV[0])
        #             pushV.pop(0)
        #         popV.pop(0)
        #         pushTep.pop(-1)
        #     else:
        #         while pushTep and pushTep[-1]==popV[0]:
        #             pushTep.pop(-1)
        #             popV.pop(0)
        #         if pushTep and pushTep[-1]!=popV[0]:
        #             return False
        # return True

        list_tmp = []
        if popV==None:
            return False
        if popV[0] not in pushV:
            return False
        while len(popV)!=0:
            tmp_node=popV[0]
            if tmp_node in pushV:
                tmp_index=pushV.index(tmp_node)
                for i in range(tmp_index+1):
                    list_tmp.append(pushV[i])
                for i in range(tmp_index,-1,-1):
                    pushV.pop(i)
                list_tmp.pop(-1)
                popV.pop(0)
            elif list_tmp[-1]==tmp_node:
                list_tmp.pop(-1)
                popV.pop(0)

            else:
                return False
        return True



a=Solution()
pushV,popV=[1],[2]
b=a.IsPopOrder(pushV,popV)
print(b)