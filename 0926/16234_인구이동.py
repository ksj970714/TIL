from collections import deque

# 0. 입력
N, L, R = map(int,input().split())
land = []
for i in range(N):
    land.append(list(map(int,input().split())))

# 설계는 크게 두 단계, 국경 열기, 이동하기 두개를 구현.
# 국경 열기
# visited & BFS
temp = [0]*N

visited = []
for i in range(N):
    visited.append(temp[:])

def bfs(dq):
    templist = []
    while dq:
        for i in range(len(dq)):
            temp = dq.popleft()
            r = temp[0]
            c = temp[1]
            templist.append([r,c])
            if 0 < r:
                if visited[r-1][c] == 0 and L <= abs(land[r][c]-land[r-1][c]) <= R:
                    visited[r-1][c] = 1
                    dq.append([r-1,c])
            if r < N-1:
                if visited[r+1][c] == 0 and L <= abs(land[r][c]-land[r+1][c]) <= R:
                    visited[r+1][c] = 1
                    dq.append([r+1,c])
            if 0 < c:
                if visited[r][c-1] == 0 and L <= abs(land[r][c] - land[r][c-1]) <= R:
                    visited[r][c-1] = 1
                    dq.append([r, c-1])
            if c < N-1:
                if visited[r][c+1] == 0 and L <= abs(land[r][c] - land[r][c+1]) <= R:
                    visited[r][c+1] = 1
                    dq.append([r, c+1])

    temptemp = []
    for i in range(len(templist)):
        temptemp.append(templist[i][:])
    solve.append(temptemp[:])
    return

def moving(solve):
    for i in range(len(solve)):
        hap = 0
        for j in range(len(solve[i])):
            hap += land[solve[i][j][0]][solve[i][j][1]]
        hap = hap//len(solve[i])
        for j in range(len(solve[i])):
            land[solve[i][j][0]][solve[i][j][1]] = hap
    return

solve = []
answer = 0
while True:
    visited = []
    solve = []
    for i in range(N):
        visited.append(temp[:])
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                dq = deque([[i,j]])
                visited[i][j] = 1
                bfs(dq)
    if len(solve) == N*N:
        break
    moving(solve)
    answer += 1

print(answer)

# 이동하기
# 리스트의 인덱스들을 합치기