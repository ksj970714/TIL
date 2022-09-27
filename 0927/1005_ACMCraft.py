#위상정렬 실시 후, DP 실시
#왜 정렬 후 하는가? 앞에 있는 것을 모두 갱신해줘야, 비로소 뒤에 있는것을 갱신가능.

from collections import defaultdict, deque

import sys

T = int(input())
for test in range(T):
    graph = defaultdict(list)
    graphlen = defaultdict(int) #진입차수
    N, K = map(int,input().split())
    time = [0]
    time.extend(list(map(int,input().split())))
    for i in range(K):
        a, b = map(int,sys.stdin.readline().split())
        graphlen[b] += 1
        graph[a].append(b)
    W = int(input())

    #지나야 하는 점
    mydict = defaultdict(int)
    #위상정렬 실시 후, 다이나믹 프로그래밍.
    dq = deque([])
    for i in range(N): #진입차수가 0인 정점 찾기
        if graphlen[i+1] == 0:
            dq.append(i+1)
        mydict[i+1] = 1
    topology = []

    while dq:
        for i in range(len(dq)):
            temp = dq.popleft()
            topology.append(temp)
            for elements in graph[temp]:
                graphlen[elements] -= 1 #간선 제거
                if graphlen[elements] == 0:
                    dq.append(elements)
    new = time[:]

    for i in range(N):
        if topology[i] == W:
            print(new[W])
            break
        for elements in graph[topology[i]]:
            new[elements] = max(time[elements]+new[topology[i]],new[elements])
