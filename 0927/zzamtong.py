#위상정렬 실시 후 그냥 다 더하면 된다.
#단, 자기랑 병렬인것 이 자기 앞에 올 수 있으므로 그 부분을 체크
#한 단계에서 큐에 들어가는게 2개이상이면 여러개의 답 존재
#연결되어있지 않은 그래프 제거. 어떻게?
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

    #세팅 완료
    #먼저 reversegraph를 탐색하며, 백준이가 마지막에 지어야 하는 건물을 짓기전에
    #선행되어야 하는 건물의 리스트와 최초 정점을 찾는다.


     #지나야 하는 점
    mydict = defaultdict(int)
    #위상정렬 실시 후, 다이나믹 프로그래밍.
    dq = deque([])
    for i in range(N):#진입차수가 0인 정점 찾기
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
