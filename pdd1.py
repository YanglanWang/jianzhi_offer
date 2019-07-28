import sys
def f1(l1,l2):
    if len(l1)==0:
        return "NO"
    if len(l1)==1:
        return l1
    kehuan=[]
    for i in range(1,len(l1)-1):
        if not l1[i-1]<l1[i]<l1[i+1]:
            kehuan.append(i)
    final_result=[]
    final_list=[]
    for k in kehuan:
        below=l1[k-1]
        up=l1[k+1]
        result_list=[]
        for j in l2:
            if j>below and j<up:
                result_list.append(j)
        if len(result_list)!=0:
            final_result.append(max(result_list))
            tmp_list=l1[:]
            tmp_list[k] = max(result_list)
            final_list.append(tmp_list)

    if len(final_result)==0:
        print 'NO'
    max_final=final_result.index(max(final_result))
    return final_list[max_final]

if __name__=="__main__":
    A=[]
    for line in sys.stdin:
        A.append(line.split())
    # A=[1, 3, 6, 5, 10]
    # B=[2, 1,4, 5, 8, 9]
    # A=[20,1,23]
    # B=[50,26,7]
    # A=[1,7,3]
    # B=[2,9]
    # B=A
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j]=int(A[i][j])

    result=f1(A[0],A[1])
    if result=='NO':
        print('NO')
    else:
        for i in result:
            print i ,