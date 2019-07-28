import sys
def f2(a):
    for i in range(len(a)-1):
        find=False
        for j in range(i+1,len(a)):
            if a[i][-1]==a[j][0]:
                tmp=a[i+1]
                a[i+1]=a[j]
                a[j]=tmp
                find=True
                break
        if find==False:
            return 'false'
    if a[0][0]!=a[-1][-1]:
        return 'false'
    return 'true'






if __name__=="__main__":
    for line in sys.stdin:
        A=line.split()
    # A=['CAT','TIGER','RPC']
    result=f2(A)
    print(result)