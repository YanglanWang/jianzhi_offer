class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        # list_origin=range(n)
        # list_m=range(m)
        # i=0
        # a=list_m.index(m-1)
        # while len(list_origin)>1:
        #     list_remove = []
        #     for i in range(len(list_origin)):
        #         if i%m==a:
        #             list_remove.append(list_origin[i])
        #
        #     # index_start=list_m[(i+1)%m]
        #     list_m=list_m[(i+1)%m:]+list_m[:(i+1)%m]
        #     a=list_m.index(m-1)
        #     list_origin=[i for i in list_origin if i not in list_remove]
        # return list_origin[0]
        people=range(n)
        m_list=range(m)
        i=0
        while len(people)>1:
            new_people=[]
            index=m_list.index(m-1)
            for i in range(len(people)):
                if i%m!=index:
                    new_people.append(people[i])
            m_list=m_list[(i%m+1)%m:]+m_list[:(i%m+1)%m]
            people=new_people
        return people[-1]



a=Solution()
b=a.LastRemaining_Solution(5,2)
print(b)