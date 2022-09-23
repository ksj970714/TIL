from collections import defaultdict
import sys

N = int(input())
M = int(input())
graph = defaultdict(list)
for i in range(M):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])

p, q = map(int,input().split())

graph[p].sort(key = lambda x:x[1])
dijkstra = [float('inf')]*(N+1)
dijkstra[p] = 0
visited = [0]*(N+1)
visited[p] = 1 ; visited[0] = 1
visit = 1

# 1. 그래프에 있는 지점 넣어줌
for i in range(len(graph[p])):
    dijkstra[graph[p][i][0]] = graph[p][i][1]
print(dijkstra)
# visited에 들어있지 않은 것 중 최솟값 뽑음
