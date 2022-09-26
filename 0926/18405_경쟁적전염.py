from collections import defaultdict, deque

N, K = map(int,input().split())

def bfs(number, mylist): #1번 시행하는 BFS
    for i in range(len(mylist)):
        temp = mylist.popleft()
        r = temp[0]
        c = temp[1]
        if 0 < r and land[r-1][c] == 0:
            land[r - 1][c] = number
            point[number].append([r - 1, c])
        if r < N-1 and land[r+1][c] == 0:
            land[r + 1][c] = number
            point[number].append([r + 1, c])
        if 0 < c and land[r][c-1] == 0:
            land[r][c - 1] = number
            point[number].append([r , c-1])
        if c < N-1 and land[r][c+1] == 0:
            land[r][c + 1] = number
            point[number].append([r , c+1])
    return

land = []
for i in range(N):
    land.append(list(map(int,input().split())))

point = defaultdict(deque)

for i in range(N):
    for j in range(N):
        if land[i][j] != 0:
            point[land[i][j]].append([i,j])

S, X, Y = map(int,input().split())

for i in range(S):
    for j in range(1,K+1):
        bfs(j, point[j])

print(land[X-1][Y-1])
