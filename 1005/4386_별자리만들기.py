import sys, collections
from heapq import *
import math

N = int(input())
star = []
for i in range(N):
    a, b = map(float,sys.stdin.readline().split())
    star.append([a,b])

def length(a_list,b_list):
    return ((a_list[0]-b_list[0])**2+(a_list[1]-b_list[1])**2)**0.5

graph = collections.defaultdict(list)
for i in range(N):
    for j in range(N):
        if i != j:
            graph[i].append([length(star[i],star[j]), j])
print(graph)

visited = [0]*N
visited[0] = 1
myline = graph[0][:]
heapify(myline)
mysum = 0

point = 1
while point < N:
    temp = heappop(myline)
    print(temp)
    if visited[temp[1]] == 0:
        visited[temp[1]] = 1
        mysum += temp[0]
        myline.extend(graph[temp[1]])
        heapify(myline)
        point += 1

print(round(mysum,2))