from collections import defaultdict

N = int(input())
mylist = list(map(int,input().split()))

mydict = defaultdict(int)

for i in range(N):
    mydict[mylist[i]] += 1

stack = [0]
answer = [0]*N

for idx in range(1,N):

    while stack:
        if mydict[mylist[stack[-1]]] < mydict[mylist[idx]]: #스택에서 빼줌
            temp = stack.pop()
            answer[temp] = mylist[idx]
        else:
            break

    stack.append(idx)

while stack:
    temp = stack.pop()
    answer[temp] = -1

print(*answer)
#끝까지 못 나간것 -1로 기록