class Solution:
    def IsContinuous(self, numbers):
        # write code here
        # numbers.sort()
        # num_zero=[i for i in numbers if i==0]
        # num_nozero=[i for i in numbers if i>0]
        # mute=0
        # for i in range(len(num_nozero)-1):
        #
        #     mute+=num_nozero[i+1]-num_nozero[i]-1
        # if mute==0:
        #     return True
        # elif mute>0:
        #     if mute>len(num_zero):
        #         return False
        #     else:
        #         return True
        # else:
        #     return False
























        # king=[i for i in numbers if i==0]
        if len(numbers)==0:
            return False
        others=[i for i in numbers if i!=0]
        if len(list(set(others)))!=len(others):
            return False
        if max(others)-min(others)>4:
            return False
        return True


a=Solution()
b=a.IsContinuous([1,3,2,5,4])
print(b)