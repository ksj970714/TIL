# 브루트포스, 백트래킹

import collections
from itertools import combinations

#입력

N, M = map(int,input().split())
mylab = []
for i in range(N):
    mylab.append(list(map(int,input().split())))

mydict = collections.defaultdict(list)

# 0, 2인 좌표를 리스트에 넣어준다.
# 0일 때 좌표는 벽 세울 위치를 잡는 조합을 만드는데 사용,
# 2일 때 좌표는 BFS 실시 시 최초의 큐에 넣어주기 위해.

for i in range(N):
    for j in range(M):
        if mylab[i][j] == 0:
            mydict[0].append([i, j])
        elif mylab[i][j] == 2:
            mydict[2].append([i, j])

#길이, 매번 재는것보다 변수 할당하는것이 시간적으로 이득이므로
#3을 빼주는 이유는 반드시 벽을 3개 세워야 하기 때문이다. (0 자리를 벽이 차지함)

mylen = len(mydict[0])-3

# 벽 3개 추가
# 이후 4방향 탐색하는 BFS 알고리즘, 0이 2로 바뀔 때 안전지대가 1개 사라짐.
# 따라서 hap -= 1을 해준다.

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