# 먼저 4000000 이하의 소수가 있는 벡터를 뽑아내야한다.
# 연속합 문제이므로, accmulate를 사용
# 이진 탐색으로 해당 벡터에서 연속합의 값을 구한다!
# accumulate, 이진탐색 이거 2개 같이 쓰는거 유용하다고 생각한다.

import itertools

def binarysearch(l,r,value):
    m = (l+r)//2
    print(l,r,m,value)
    if prime[m] == value:
        return 1

    if r - l <= 1:
        return 0

    elif prime[m] > value:
        return binarysearch(l, m-1, value)

    else:
        return binarysearch(m+1, r, value)

N = int(input())
eratos = [1]*(N+1)
eratos[0] = 0
eratos[1] = 0
prime = []
for i in range(int(N**0.5)+1):
    print('i',i)
    if eratos[i] == 1:
        prime.append(i) #소수벡터에 추가
        for j in range(N//i + 1):
            eratos[i*j] = 0

for i in range(int(N**0.5),N+1):
    if eratos[i] == 1:
        prime.append(i)  # 소수벡터에 추가

print(prime)

prime = list(itertools.accumulate(prime))

print(prime)
length = len(prime) - 1
count = 0

for elements in prime:
    print('try:',elements-N)

    if elements == N:
        count += 1

    elif elements >= N :
        count += binarysearch(0,length,elements - N)

print(count)