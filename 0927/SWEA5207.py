T = int(input())
global count

def binarysearch(vector,p,l,r,switch):

    global count
    m = (l+r)//2

    if vector[m] > p: #왼쪽
        if switch == 1:
            return
        else:
            switch = 1
            binarysearch(vector,p,l,m-1,switch)
            return
    elif vector[m] == p: #중앙

        count += 1
        return
    else: #오른쪽
        if switch == -1:
            return
        else:
            switch = -1
            binarysearch(vector,p,m+1,r,switch)
            return


for testcase in range(1,T+1):
    count = 0
    N, M = map(int,input().split())
    Nlist = sorted(list(map(int,input().split())))
    Mlist = list(map(int,input().split()))

    for i in range(M):
        binarysearch(Nlist,Mlist[i],0,N-1,0)
    print('#{} {}'.format(testcase,count))




