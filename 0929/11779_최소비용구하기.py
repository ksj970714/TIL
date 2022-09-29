#다익스트라 알고리즘
import sys
from collections import defaultdict
import heapq

N = int(input())
M = int(input())
graph = defaultdict(list)

for i in range(M):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c]) # 그래프의 딕셔너리 표현

S, G = map(int,input().split())


def dijkstra(start):
    distance = [float('inf')]*(N+1)
    distanceway = [[]]*(N+1)
    queue = []
    heapq.heappush(queue,[0,start,[start]]) #거리, 시작지점 삽입

    while queue:
        current_distance, current_destination, way = heapq.heappop(queue)

        if distance[current_destination] < current_distance:
            continue

        for i in graph[current_destination]:
            cost = current_distance + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                distanceway[i[0]] = way + [i[0]]
                heapq.heappush(queue,[cost,i[0], way+[i[0]]])
    return distance, distanceway


print(dijkstra(S)[0][G])
print(len(dijkstra(S)[1][G]))
print(*dijkstra(S)[1][G])