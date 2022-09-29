import sys
from collections import deque,Counter


T = int(input())

for test in range(T):
    flag = 0
    N, M = map(int,sys.stdin.readline().split())
    mylist = list(map(int,sys.stdin.readline().split()))

    dq = deque(list(range(N)))
    mylength = len(dq)
    mylist = deque(mylist)
    mydict = Counter(mylist)
    count = 0
    temp = 1000
    flag = 0

    for i in range(9,0,-1):
        if flag == 1:
            break
        while mydict[i] != 0:
            print('dq',dq)
            print('mylist',mylist)
            if mylist[0] == i:
                count += 1
                temp = dq.popleft()
                mylist.popleft()
                mydict[i] -= 1
            else:
                dq.append(dq.popleft())
                mylist.append(mylist.popleft())

            if temp == M :
                print(count)
                flag = 1
                break



