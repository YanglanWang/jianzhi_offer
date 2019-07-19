class Solution:
    def jumpFloor(self, number):
        # write code here
        if number==1:
            return 1
        elif number==2:
            return 1+self.jumpFloor(number-1)
        else:
            return self.jumpFloor(number-1)+self.jumpFloor(number-2)

a=Solution()
print(a.jumpFloor(4))