import sys

N, M = map(int,input().split())
c = {}
for i in range(N):
    a, b = sys.stdin.readline().split()
    c[a] = b.rstrip()

for j in range(M):
    print(c[sys.stdin.readline().rstrip()])
