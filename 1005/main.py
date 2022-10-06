# 사이클
# 반례
# 1 3 4 5 2 (1만 왕따)
T = int(input())
for _ in range(T):
    N = int(input())
    count = N
    visited = [0]*(N+1)
    visited[0] = 1
    stack = []
    mylist = [0]+list(map(int,input().split()))
    for i in range(1,N+1):
        if visited[i] == 0 :
            stack = [i]
            visited[i] = 1
            next = mylist[i]
            if i == next:
                count -= 1
                continue

            elif visited[next] == 1:
                continue
            while visited[next] == 0:
                stack.append(next)
                visited[next] = 1
                next = mylist[next]

            while stack:
                temp = stack.pop()
                count -= 1
                if temp == next:
                    break
            while stack:

                temp = stack.pop()
                visited[temp] = 1

    print(count)