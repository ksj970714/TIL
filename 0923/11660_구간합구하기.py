import sys
N, M = map(int,input().split())
t = [0]*(N+1)
mylist = []
for i in range(N+1):
    mylist.append(t[:])

for i in range(1,N+1):
    temp = [0]
    temp.extend(list(map(int, sys.stdin.readline().split())))
    mylist[i][0] = mylist[i-1][0] + temp[0]
    for j in range(1,N+1):
        temp[j] += temp[j-1]
        mylist[i][j] = temp[j]+mylist[i-1][j]


for i in range(M):
    a,b,c,d = map(int,sys.stdin.readline().split())
    print(mylist[c][d]-mylist[a-1][d]-mylist[c][b-1]+mylist[a-1][b-1])