import sys

N = int(input())
beyoung = [0]*(N+1)
for i in range(1,N+1):
    temp_list = list(map(int, sys.stdin.readline().split()))
    temp_max = 0
    if temp_list[1] == 0:
        temp_max = temp_list[0]

    for j in range(temp_list[1]):
        if temp_max < beyoung[temp_list[j+2]]+temp_list[0]:
            temp_max = beyoung[temp_list[j+2]]+temp_list[0]

    beyoung[i] = temp_max

print(max(beyoung))