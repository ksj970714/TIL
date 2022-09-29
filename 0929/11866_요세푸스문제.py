from collections import deque

N, K = map(int,input().split())

# 제거를 N번 pop, enque로 구현.

vector = deque(list(range(1,N+1)))

myword = '<'

for i in range(N-1):
    for j in range(K-1):
        temp = vector.popleft()
        vector.append(temp)
    temp = vector.popleft()
    myword += str(temp) +', '

myword += str(vector.popleft()) + '>'

print(myword)
