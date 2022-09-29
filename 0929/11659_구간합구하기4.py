from itertools import accumulate
import sys

N, M = map(int,input().split())
mylist = list(map(int,input().split()))
mynewlist = list(accumulate(mylist))

for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    if a == 1:
        print(mynewlist[b-1])
    else:
        print(mynewlist[b-1] - mynewlist[a-2])