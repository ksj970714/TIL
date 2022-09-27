import sys
from collections import defaultdict
N = int(input())

mylist = []
for i in range(N):
    mylist.append(int(sys.stdin.readline()))


stack = [mylist[0]]
switch = 0 # 0이면 같음 1이면 증가 -1이면 감소
count = 0
length = 1
mydict = defaultdict(int)
mydict[mylist[0]] = 1

for i in range(1, N):
    while stack:
        print(stack, mylist[i],'count',count,'length',length,mydict)
        if stack[-1] < mylist[i]: #증가
            mydict[stack.pop()] -= 1
            count += 1
            length -= 1
        elif stack[-1] == mylist[i]: #같음 44 33에 대해
            #몇 개까지가 같은지 알아야 한다.
            count += mydict[mylist[i]] #이미 들어가있는 자신의 갯수만큼 더함
            if length != mydict[mylist[i]]:
                count += 1 #만약 앞에 뭐가 더 있을경우 더해줌.
            break
        else: #감소
            count += 1
            break
    stack.append(mylist[i])
    mydict[mylist[i]] += 1
    length += 1

print(count)