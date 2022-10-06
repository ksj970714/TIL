import itertools

N, S = map(int,input().split())
mylist = list(map(int,input().split()))
newlist = [0]+list(itertools.accumulate(mylist)) #인덱스 0부터 그 시점까지의 합을 구한 리스트

#투 포인터 알고리즘 사용

left = 0
right = 1
minlength = float('inf')

while right <= N:
    if left == right:
        minlength = 1
        break

    if newlist[right]-newlist[left] < S:
        right += 1

    else:
        minlength = min(minlength, right - left)
        left += 1


if minlength == float('inf'):
    print(0)
else:
    print(minlength)

#반례
'''
1. 하나의 점으로 만족되는경우
ex) 
10 15
1 2 3 10 15 7 1 2 3 4

2. 답이 없는 경우
ex) 
10 100
1 2 3 4 5 6 7 8 9 10

3. 처음에 만족하는게 나오고, 그 뒤에 더 짧은 수열이 나올경우
10 20
10 1 8 1 17 1 1 12 10 10 
ex)
'''