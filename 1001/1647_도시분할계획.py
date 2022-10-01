#프림 알고리즘
#노드에 대해 실시

import sys
from collections import defaultdict
from heapq import *

max_line = 0
hap = 0
mst = 0
graph = defaultdict(list)
V, E = map(int,input().split())
for i in range(E):
    x, y, weight = map(int,sys.stdin.readline().split())
    graph[x].append([weight, y])
    graph[y].append([weight, x])
    hap += weight

nodes = {1} #해시 테이블, 시간 복잡도 절약
lines = graph[1]
heapify(lines)
N = 0

while lines:
    print(N)
    weight, end = heappop(lines) #힙 구조를 유지하기 때문에,
    if end not in nodes:
        nodes.add(end)
        mst += weight
        max_line = max(max_line,weight)
        N += 1
        #프림 알고리즘에서의 시간 최적화를 위해 불필요한 탐색을 멈춤
        #이미 N-1개의 간선을 선택했을 시 최소 스패닝 트리가 완성되었으므로 중단.
        if N == V-1:
            break

        for edge in graph[end]:
            if edge[1] not in nodes: #이런식으로 모든 노드 탐색.
                heappush(lines,edge)

    # 힙 구조 때문에, heap에서 꺼낼 때 항상 가장 작은 것이 나온다는 것이 보장된다.

print(mst-max_line)
