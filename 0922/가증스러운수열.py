from collections import defaultdict

N = int(input())
mydict = defaultdict(int)
mylist = list(map(int,input().split()))
cur = 1

for i in range(N-1):
    if mylist[i+1] > mylist[i]:
        cur += 1
    else:
        cur = 1
    if mydict[cur] > my    list[i+1]:

