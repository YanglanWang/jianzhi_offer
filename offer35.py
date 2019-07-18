# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if len(data) == 0 or len(data) == 1:
            return 0
        length = len(data)
        l_inner = [0] * len(data)
        data = [[i] for i in data]

        while len(data[0]) != length:
            data_new = []
            l_inner_new = []
            for i in range(len(data) // 2):
                list_combine, num_combine = self.count(data[2 * i], data[2 * i + 1])
                data_new.append(list_combine)
                l_inner_new.append(l_inner[2 * i] + l_inner[2 * i + 1] + num_combine)
            if len(data) % 2 != 0:
                data_new.append(data[2 * (i + 1)])
                l_inner_new.append(l_inner[2 * (i + 1)])
            data = data_new
            l_inner = l_inner_new
        return l_inner[0] % 1000000007

    def count(self,l1, l2):
        i = len(l1) - 1
        j = len(l2) - 1
        list_combine = []
        num_combine = 0
        while len(l1) != 0 and len(l2) != 0:
            if l1[i] > l2[j]:
                list_combine.insert(0,l1[i])
                del l1[-1]
                i = i - 1
                num_combine += j + 1
            else:
                list_combine.insert(0,l2[j])
                del l2[-1]
                j = j - 1
        if len(l1) == 0:
            list_combine=l2[:]+list_combine
        if len(l2) == 0:
            list_combine=l1[:]+list_combine
        return list_combine, num_combine

# count = 0
# class Solution:
#     def InversePairs(self, data):
#         global count
#         def MergeSort(lists):
#             global count
#             if len(lists) <= 1:
#                 return lists
#             num = int( len(lists)/2 )
#             left = MergeSort(lists[:num])
#             right = MergeSort(lists[num:])
#             r, l=0, 0
#             result=[]
#             while l<len(left) and r<len(right):
#                 if left[l] < right[r]:
#                     result.append(left[l])
#                     l += 1
#                 else:
#                     result.append(right[r])
#                     r += 1
#                     count += len(left)-l
#             result += right[r:]
#             result += left[l:]
#             return result
#         MergeSort(data)
#         return count%1000000007


a=Solution()
b=a.InversePairs([7,5,6,4])
print(b)