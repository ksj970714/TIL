import sys

N = int(input())
triangle = []
for i in range(N):
    triangle.append(list(map(int,sys.stdin.readline().split())))

mydp = [triangle[0][0]]

for i in range(1,N):
    temp = []
    temp.append(mydp[0]+triangle[i][0]) #왼쪽
    for j in range(1,i):
        temp.append(max(mydp[j]+triangle[i][j],mydp[j-1]+triangle[i][j]))
    temp.append(mydp[i-1]+triangle[i][i])#오른쪽
    mydp = temp

print(max(mydp))