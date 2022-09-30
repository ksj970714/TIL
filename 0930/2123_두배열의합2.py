from itertools import accumulate
from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

A = [0]+list(accumulate(A))
B = [0]+list(accumulate(B))

A_sum = []
B_sum = defaultdict(int)

for i in range(m+1):
    for j in range(i):
        B_sum[B[i]-B[j]] += 1

for i in range(n+1):
    for j in range(i):
        A_sum.append(A[i]-A[j])

mysum = 0

for i in range(len(A_sum)):
    C = T - A_sum[i]
    mysum += B_sum[C]

print(mysum)