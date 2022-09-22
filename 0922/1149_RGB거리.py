import sys

N = int(input())
mylist = []

for i in range(N):
    mylist.append(list(map(int,sys.stdin.readline().split())))
ans = mylist[0]

for i in range(1,len(mylist)):
    R = min(mylist[i][0]+ans[1],mylist[i][0]+ans[2])
    G = min(mylist[i][1]+ans[0],mylist[i][1]+ans[2])
    B = min(mylist[i][2]+ans[0],mylist[i][2]+ans[1])
    ans = [R,G,B]

print(min(ans))