from collections import defaultdict, deque

N = int(input())
mydict = defaultdict(list)

mylist = list(map(int,input().split()))
for i in range(N):
    mydict[mylist[i]].append(i)

leaf = 0

V = int(input())

for i in range(N):
    if mydict[i] == [] or mydict[i] ==[V]:
        leaf += 1

dq = deque([V])
while dq:
    for i in range(len(dq)):
        temp = dq.popleft()
        if mydict[temp] == []:
            leaf -= 1
        dq.extend(mydict[temp])


print(leaf)