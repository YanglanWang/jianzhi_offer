import sys

if __name__=="__main__":
    A=[]
    for line in sys.stdin:
        A.append(line.split())

    N = int(A[0][0])
    M = int(A[0][1])
    t = [int(i) for i in A[1]]
    t.insert(0,0)
    relation =[ [int(j) for j in i] for i in A[2:]]
    dict_n = {}
    for i in relation:
        if i[0] not in dict_n:
            dict_n[i[0]] = 1
        else:
            dict_n[i[0]] += 1
    for i in range(1,N+1):
        if i not in dict_n.keys():
            dict_n[i]=0
    sequence = []
    for i in dict_n.keys():
        if len(sequence) == 0:
            sequence.append(i)
        else:
            k = 0
            while k < len(sequence) and dict_n[i] < dict_n[sequence[k]]:
                k += 1
            while k < len(sequence) and t[sequence[k]] <= t[i]:
                k += 1
            sequence.insert(k, i)
    for r in sequence:
        print r,