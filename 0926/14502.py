# 브루트포스, 백트래킹

import collections
from itertools import combinations

#탐색
def count(lab,M,N):
    cnt = 0
    for i in range(M):
        for j in range(N):
            if lab[i][j] == 0:
                cnt += 1
    return cnt

N, M = map(int,input().split())
mylab = []
for i in range(N):
    mylab.append(list(map(int,input().split())))

mydict = collections.defaultdict(list)

#0, 2인 좌표 싹 다 탐색
for i in range(N):
    for j in range(M):
        if mylab[i][j] == 0:
            mydict[0].append([i, j])
        elif mylab[i][j] == 1:
            mydict[1].append([i, j])
        else:
            mydict[2].append([i, j])
# 길이

mylen = len(mydict[0])-3

#추가

mycom = list(combinations(mydict[0],3))
maxhap = 0
for walls in mycom:
    hap = mylen
    lab = []
    for i in range(N):
        lab.append(mylab[i][:])

    for wall in walls:
        lab[wall[0]][wall[1]] = 1

    dq = collections.deque(mydict[2])
    while dq:
        temp = dq.popleft()
        r = temp[0]
        c = temp[1]
        if 0 < r:
            if lab[r - 1][c] == 0:
                lab[r - 1][c] = 2
                dq.append([r - 1, c])
                hap -= 1
        if r < N - 1:
            if lab[r + 1][c] == 0:
                lab[r + 1][c] = 2
                dq.append([r + 1, c])
                hap -= 1
        if 0 < c:
            if lab[r][c - 1] == 0:
                lab[r][c - 1] = 2
                dq.append([r, c - 1])
                hap -= 1
        if c < M - 1:
            if lab[r][c + 1] == 0:
                lab[r][c + 1] = 2
                dq.append([r, c + 1])
                hap -= 1
    if maxhap < hap:
        maxhap = hap

print(maxhap)