#프림 알고리즘
#노드에 대해 실시

import sys
from collections import defaultdict
from heapq import *

mst = 0
graph = defaultdict(list)
V, E = map(int,input().split())
for i in range(E):
    x, y, weight = map(int,sys.stdin.readline().split())
    graph[x].append([weight, y])
    graph[y].append([weight, x])

nodes = {1} #해시 테이블, 시간 복잡도 절약
lines = graph[1]
heapify(lines)

while lines:
    weight, end = heappop(lines) #힙 구조를 유지하기 때문에,
    if end not in nodes:
        nodes.add(end)
        mst += weight

        for edge in graph[end]:
            if edge[1] not in nodes: #이런식으로 모든 노드 탐색.
                heappush(lines,edge)
    # 힙 구조 때문에, heap에서 꺼낼 때 항상 가장 작은 것이 나온다는 것이 보장된다.

print(mst)

