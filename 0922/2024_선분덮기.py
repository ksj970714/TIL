import sys
M = int(input())
switch = 0
vec = [0]*(M+1)
while switch == 0:
    a, b = map(int,sys.stdin.readline().split())
    if a == 0 and b == 0:
        switch = 1
    if a < 0:
        a = 0
    if b < 0 :
        b = 0
    if a > M:
        a = M
    if b > M:
        b = M
    if vec[a] < b:
        vec[a] = b
count = 1
start = 0
end = vec[start]

while end < M :
    end = max(vec[start:end + 1])
    start = vec[start]
    count += 1
    if start >= end:
        count = 0
        break

print(count)