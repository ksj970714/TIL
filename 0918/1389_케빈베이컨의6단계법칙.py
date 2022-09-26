import sys
import collections
from collections import deque

N, M = map(int,input().split())
graph = collections.defaultdict(list)

for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
counts = []

for node in range(1,N+1):
    visited = [0] * (N + 1)
    visited[0] = 1
    visited[node] = 1
    count = 1
    bacon = 0

    dq = deque([node])
    while dq:
        for i in range(len(dq)):
            temp = dq.popleft()
            for j in graph[temp]:
                if visited[j] == 0:
                    visited[j] = 1
                    bacon += count
                    dq.append(j)

        count += 1
    counts.append(bacon)

minvalue = 500000
sol = 0
for i in range(len(counts)):
    if counts[i] < minvalue:
        sol = i
        minvalue = counts[i]

print(sol+1)