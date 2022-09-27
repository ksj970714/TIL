from itertools import combinations
from collections import deque
global N
N, M = map(int,input().split())

lab = []

for i in range(N):
    lab.append(list(map(int,input().split())))



#BFS 설계
def bfs(dq,space):
    for k in dq:
        mylab[k[0]][k[1]] = 1
    space -= len(dq)
    print(mylab)
    print('dq',dq)
    count = -1
    while dq:
        count += 1
        for i in range(len(dq)):
            temp = dq.popleft()
            r = temp[0]
            c = temp[1]
            if 0 < r:
                if mylab[r-1][c] == 0 or mylab[r-1][c] == 2:
                    mylab[r - 1][c] = 1
                    space -= 1
                    dq.append([r-1,c])
            if r < N-1:
                if mylab[r+1][c] == 0 or mylab[r+1][c] == 2:
                    mylab[r+1][c] = 1
                    space -= 1
                    dq.append([r+1,c])
            if 0 < c:
                if mylab[r][c-1] == 0 or mylab[r][c-1] == 2:
                    mylab[r][c-1] = 1
                    space -= 1
                    dq.append([r,c-1])
            if c < N-1:
                if mylab[r][c+1] == 0 or mylab[r][c+1] == 2:
                    mylab[r][c+1] = 1
                    space -= 1
                    dq.append([r,c+1])

    if space == 0:
        return count
    else:
        return float('inf')

#2인 위치 저장, 0의 갯수 저장
space = 0
virus = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append([i,j])
            space += 1
        elif lab[i][j] == 0:
            space += 1

print(space)
#2인 위치 조합 뽑아서 저장
virus = list(combinations(virus,M))

print(virus,space)

#각 조합별 확산 시켜보기(BFS 사용)
#0을 셌다가, 확산시마다 count를 줄여 0이 되면 탐색을 중단하는 방식
#BFS 한 사이클 돌때마다 타임 체크(time 변수에 저장.)
mymin = float('inf')
for test in range(len(virus)):
    # 2차원 리스트 깊은복사
    mylab = []
    for i in range(N):
        mylab.append(lab[i][:])

    mymin = min(mymin,bfs(deque(virus[test]),space))

if mymin == float('inf'):
    print(-1)
else:
    print(mymin)


