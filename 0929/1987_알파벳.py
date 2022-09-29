# hash table인 set 이용
import sys

R, C = map(int,sys.stdin.readline().split())
myarray = [list(map(lambda a : ord(a)-65,input())) for _ in range(R)]
myset = [0]*26

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

myset[myarray[0][0]] = 1
mymax = 0
def dfs(r,c,count):
    global mymax
    mymax = max(mymax,count)
    for i in range(4):
        x, y = r + dx[i], c + dy[i]
        if 0 <= x < R and 0 <= y < C and myset[myarray[x][y]] != 1 :
            myset[myarray[x][y]] = 1
            dfs(x,y,count+1)
            myset[myarray[x][y]] = 0
dfs(0,0,1)
print(mymax)