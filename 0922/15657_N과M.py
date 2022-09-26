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
        if len(pow) == 0 :
            pow.append(mylist[i])
            length += 1
            su(length)
            length -= 1
            visited[i] = 0
            pow.pop()
        else:
            if pow[-1] > mylist[i]:
                continue
            else:
                pow.append(mylist[i])
                length += 1
                su(length)
                length -= 1
                visited[i] = 0
                pow.pop()
su(0)