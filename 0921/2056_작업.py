#루트를 모두 큐에 삽입하고 BFS실시. 와! 쉽다!
#단방향 그래프니까, 방문처리 안해도된다! 더 좋다!
#단순 탐색이니까 거리가 들어가야 하는 건 조금 주의
import collections
from collections import deque, defaultdict
import sys
N = int(input())
graph = defaultdict(list)
time = defaultdict(int)

#현재 거리, 현재정접삽입 데크는 같이 움직인다.
dq = deque([])
total = defaultdict(int)
for i in range(1,N+1):
    temp_list = list(map(int,sys.stdin.readline().split()))
    time[i] = temp_list[0]

    if temp_list[1] == 0:
        total[i] = temp_list[0]
        dq.append(i)
    for j in range(temp_list[1]):
        graph[temp_list[2+j]].append(i)


mymax = 0

while dq: #갱신, A에서 B로 갈 때 time[A] + time[B]
    for i in range(len(dq)):
        temp = dq.popleft()
        if mymax < total[temp] :
            mymax = total[temp]
        for j in range(len(graph[temp])):
            templen = time[graph[temp][j]]
            if time[graph[temp][j]] + total[temp] > total[graph[temp][j]]:
                total[graph[temp][j]] = time[graph[temp][j]] + total[temp]
                dq.append(graph[temp][j])
print(mymax)

#BFS로 짜봤는데 실패, 문제의 주어진것을 최대한 잘 읽어보기