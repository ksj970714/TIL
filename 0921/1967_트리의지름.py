#어떤식으로 풀까
#리프노드에서 출발, 가지노드에 도달하면 체크, 갱신
#간선 메모해두고, 간선 n개가 다 들어가면 계산 -> 값 갱신(새로운 리프 노드가됨)
from collections import deque, defaultdict
import sys
N = int(input())
leaf = deque([])

visited = [0] * (N + 1)

my_max = 0
graph = defaultdict(list)
lenvector = defaultdict(list)
lenvectorlen = defaultdict(int)
is_leaf = defaultdict(int)
leaflen = [0] * (N + 1)  # 최하위 리프에서 거기 도달하기까지의 최댓값.
for i in range(N - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[b].extend([a, c])
    is_leaf[a] += 1
for i in range(1, N + 1):
    if is_leaf[i] == 0:
        leaf.append(i)

cur = -1
while leaf:
    # 값 구하기

    for i in range(len(leaf)):
        temp = leaf.popleft()
        if temp == 1:
            if my_max < leaflen[1]:
                my_max = leaflen[1]
            break

        lenvector[graph[temp][0]].append(leaflen[temp] + graph[temp][1])
        lenvectorlen[graph[temp][0]] += 1
        if lenvectorlen[graph[temp][0]] == is_leaf[graph[temp][0]]:
            leaflen[graph[temp][0]] = max(lenvector[graph[temp][0]])
            lenvector[graph[temp][0]].remove(leaflen[graph[temp][0]])
            leaf.append(graph[temp][0])
            for j in range(is_leaf[graph[temp][0]] - 1):
                if my_max < leaflen[graph[temp][0]] + lenvector[graph[temp][0]][j]:
                    my_max = leaflen[graph[temp][0]] + lenvector[graph[temp][0]][j]

print(my_max)