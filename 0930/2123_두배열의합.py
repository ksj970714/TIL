from itertools import accumulate

def binarysearch(start,end,C): #B에서 찾는 이진탐색 코드
    count = 0
    print(start,end)
    if end - start <= 1 :
        if B[end] == C:
            count += 1
        if B[start] == C:
            count += 1
        return count #못 찾음
    mid = (start+end)//2
    if B[mid] < C:
        count += binarysearch(mid, end, C)
    elif B[mid] > C:
        count += binarysearch(start, mid, C)
    else:
        count += 1
        temp1 = mid-1
        temp2 = mid+1
        while 0 <= temp1 < length and C == B[temp1]:
            count += 1
            temp1 -= 1
        while 0 < temp2 < length and C == B[temp2]:
            count += 1
            temp2 += 1
    return count



T = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

A = [0]+list(accumulate(A))
B = [0]+list(accumulate(B))

A_sum = []
B_sum = []

for i in range(m+1):
    for j in range(i):
        B_sum.append(B[i]-B[j])

for i in range(n+1):
    for j in range(i):
        A_sum.append(A[i]-A[j])

B = sorted(B_sum)


global length
length = len(B)
mysum = 0

for i in range(len(A_sum)):
    C = T - A_sum[i] # 이분 탐색으로 해당 temp와 결합 가능한 것 찾음
    print('C',C)
    print(B)
    mysum += binarysearch(0,length-1,C)
    print('count',mysum)

print(mysum)