#무식하게 짜보기

import sys, collections
'''
N = int(input())
mylist = [0]+list(map(int,input().split()))
M = int(input())
for i in range(M):
    S, E = map(int,sys.stdin.readline().split())
    cha = (E - S)//2 + 1

    for j in range(cha):
        if mylist[S+j] != mylist[E-j]:
            print(0)
            break
    else:
        print(1)
'''

# 조금 더 똑똑하게?
# 팰린드롬을 미리 구해둔다는 아이디어,
N = int(input())
mylist = [0]+list(map(int,input().split()))+[0]

mydict = collections.defaultdict(int)

for i in range(1, N): #홀수
    l, r = i, i
    while 0 < l and r < N+1:
        l -= 1
        r += 1
        if mylist[l] != mylist[r]:
            break
    mydict[i] = r-l-2

for i in range(1,N):
    l, r = i, i+1

    while 0 < l and r < N+1:
        print('*',l,r)
        if mylist[l] != mylist[r]:
            break
        l -= 1
        r += 1
    print(l,r)
    mydict[i+0.5] = r-l-2

print(mydict)

M = int(input())
for i in range(M):
    S, E = map(int,sys.stdin.readline().split())
    mid = (S+E)/2
    if mydict[mid] >= E - S:
        print(1)
    else:
        print(0)

#어거지로 풀었네..