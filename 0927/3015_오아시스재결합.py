import sys
N = int(input())

mylist = []
for i in range(N):
    mylist.append(int(sys.stdin.readline()))


stack = [mylist[0]]
switch = 0 # 0이면 같음 1이면 증가 -1이면 감소
count = 0
length = 1

for i in range(1, N):
    while stack:
        print(stack,count)
        if stack[-1] < mylist[i]: #증가
            stack.pop()
            count += 1
            length -= 1
        elif stack[-1] == mylist[i]: #같음
            count += length
            break
        else: #감소
            count += 1
            break
    stack.append(mylist[i])
    length += 1

print(count)