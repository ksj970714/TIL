import sys

stair = []

N = int(input())
for i in range(N):
    stair.append(int(sys.stdin.readline()))

if len(stair) <= 2:
    print(sum(stair))
    quit()

sum1 = stair[0]
sum2 = stair[0]
maxval= [stair[0],stair[0]+stair[1],max(stair[0]+stair[2],stair[1]+stair[2])]

for i in range(N-3):
    sum1 = maxval[i+1]+stair[i+3]
    sum2 = maxval[i]+stair[i+2]+stair[i+3]

    maxval.append(max(sum1, sum2))


print(maxval[-1])