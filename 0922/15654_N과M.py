N, M = map(int,input().split())
mylist = sorted(list(map(int,input().split())))

pow = []
visited = [0]*N
def su(length):

    if length == M:
        print(*pow)
        length -= 1

        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            pow.append(mylist[i])
            length += 1
            su(length)
            length -= 1
            visited[i] = 0
            pow.pop()
su(0)