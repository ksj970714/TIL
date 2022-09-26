import collections
import sys

N,M = map(int,input().split())
mydict = collections.defaultdict(int)
count = 0
mylist = []

for i in range(N):
    mydict[sys.stdin.readline().rstrip()] = 1

for i in range(M):
    temp = sys.stdin.readline().rstrip()
    if mydict[temp] == 1:
        count += 1
        mylist.append(temp)

print(count)
for word in sorted(mylist):
    print(word)