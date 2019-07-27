# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
    #     if len(numbers)==1:
    #         return numbers[0]
    #     num_l = [str(number) for number in numbers]
    #     result = self.circle(num_l)
    #     result_l = []
    #     for i in result:
    #         string = ''.join(i)
    #         result_l.append(int(string))
    #     return min(result_l)
    #
    # def circle(self,num_l):
    #     if len(num_l) == 2:
    #         return [num_l, num_l[::-1]]
    #     ll = []
    #     for j in range(len(num_l)):
    #         for i in self.circle(num_l[0:j]+num_l[j+1:]):
    #             ll.append([num_l[j]] + i)
    #     return ll



        a = self.subMinNumber(numbers)
        return int(a[0])

    def subMinNumber(self, numbers):
        tmp = []

        if len(numbers) == 0:
            return None
        if len(numbers) == 1:
            return [str(numbers[0])]
        for i in range(len(numbers)):
            t = self.subMinNumber(numbers[0:i] + numbers[i + 1:])
            for j in t:
                tmp.append(str(numbers[i]) + j)
        tmp.sort()
        return tmp
        # return tmp

a=Solution()
b=a.PrintMinNumber([3,5,1])
print(b)