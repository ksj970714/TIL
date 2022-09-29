from collections import deque

N, M = map(int,input().split())
dq = deque(list(range(1,N+1)))
mylist = list(map(int,input().split()))
count = 0

#위치 찾기, 위치 탐색 후 오른쪽으로 돌릴지 왼쪽으로 돌릴지 판단.
for i in range(M):
    print(dq)
    idx = dq.index(mylist[i])
    if idx > N//2:
        # 뒤에 있을 경우
        for j in range(N-idx-1):
            temp = dq.pop()
            dq.appendleft(temp)
            count += 1
        dq.pop()
        count += 1
        N -= 1
    else:
        for j in range(idx):
            temp = dq.popleft()
            dq.append(temp)
            count += 1
        dq.popleft()
        N -= 1
print(dq)
print(count)

