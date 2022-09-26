#연결요소

#BFS탐색
from collections import deque
import collections
import sys

N, M = map(int,input().split())
graph = collections.defaultdict(list)
visited = [0]*(N+1)
visited[0] = 1
count = 0

for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


for point in range(N+1):
    if visited[point] == 0:

        dq = deque([point])
        while dq:
            for i in range(len(dq)):
                temp = dq.popleft()
                for j in range(len(graph[temp])):
                    if visited[graph[temp][j]] == 0:
                        visited[graph[temp][j]] = 1
                        dq.append(graph[temp][j])

        count += 1

print(count)
