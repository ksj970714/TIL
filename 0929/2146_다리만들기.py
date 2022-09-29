import sys
from collections import deque,defaultdict
N = int(input())
mylist = []
for i in range(N):
    mylist.append(list(map(int,sys.stdin.readline().split())))

# 각 섬 분류

num = 2
dx = [1,-1,0,0]
dy = [0,0,1,-1]
dq = deque([])
mydict = defaultdict(list)

#번호 붙이기

for i in range(N):
    for j in range(N):
        if mylist[i][j] == 1 :
            dq.append([i,j])
            mylist[i][j] = num

            while dq:
                temp = dq.popleft()
                r = temp[0]
                c = temp[1]
                mydict[num].append([r, c])
                for i in range(4):
                    if 0 <= r + dx[i] < N and 0 <= c + dy[i] < N and mylist[r + dx[i]][c + dy[i]] == 1:
                        dq.append([r + dx[i],c + dy[i]])
                        mylist[r + dx[i]][c + dy[i]] = num

            num += 1

keys = list(mydict.keys())

#queue
mincount = 2000
for key in keys:
    visited = []
    for i in range(N):
        visited.append([0] * N)
    depth = 0
    flag = 0
    dq = deque(mydict[key])
    count = 0
    while dq and flag == 0 and count < mincount:
        for i in range(len(dq)):

            temp = dq.popleft()
            r = temp[0]
            c = temp[1]
            visited[r][c] = 1
            for i in range(4):
                if 0 <= r + dx[i] < N and 0 <= c + dy[i] < N and mylist[r + dx[i]][c + dy[i]] == 0 and visited[r + dx[i]][c + dy[i]] == 0:
                    dq.append([r + dx[i], c + dy[i]])
                    visited[r + dx[i]][c + dy[i]] = 1
                elif 0 <= r + dx[i] < N and 0 <= c + dy[i] < N and visited[r + dx[i]][c + dy[i]] == 0 and mylist[r + dx[i]][c + dy[i]] != key:
                    flag = 1
                    mincount = min(mincount, count)
            if flag == 1:
                break
        count += 1


print(mincount)