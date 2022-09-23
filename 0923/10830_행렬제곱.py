import math
from copy import deepcopy
N, B = map(int,input().split())
n = math.log2(B)
squarevec = []
n = int(n)
for i in range(n,-1,-1):
    if B >= (2**i):
        B -= 2**i
        squarevec.append(i)


veclist = []
whitevec = []
for i in range(N):
    whitevec.append([0]*N)

myvec = []
for i in range(N):
    myvec.append(list(map(int, input().split())))

veclist.append(myvec)

for i in range(n):
    newvec = deepcopy(whitevec[:])
    for j in range(N):
        for k in range(N):
            temp = 0
            for l in range(N):

                temp += (myvec[j][l]*myvec[l][k])

            newvec[j][k] = temp%1000


    myvec = deepcopy(newvec)
    veclist.append(deepcopy(myvec))

ans = deepcopy(whitevec[:])
for i in range(N):
    ans[i][i] = 1



for elements in squarevec:
    myvec = veclist[elements][:]

    tempvec = deepcopy(whitevec[:])

    for j in range(N):
        for k in range(N):
            temp = 0
            for l in range(N):

                temp += (ans[j][l] * myvec[l][k])

            tempvec[j][k] = temp % 1000

    ans = deepcopy(tempvec)

for i in range(N):
    print(*ans[i])


