from collections import deque

N, K = map(int,input().split())
dq = deque([N])
count = 1
flag = 0
visited = [0]*100001
while dq:
    if flag == 0:
        for i in range(len(dq)):

            temp = dq.popleft()
            if temp == K:
                flag = 1
                dq = []
                break
            if 0 <= temp - 1 and visited[temp - 1] == 0:
                dq.append(temp-1)
                visited[temp - 1] = count

            if temp + 1 < 100001 and visited[temp + 1] == 0:
                dq.append(temp+1)
                visited[temp + 1] = count

            if temp * 2 < 100001 and visited[temp * 2] == 0:
                dq.append(temp*2)
                visited[temp * 2] = count

    count += 1

print(visited[K])