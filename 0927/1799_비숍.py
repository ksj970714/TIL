'''
기본적인 아이디어는, 오른쪽 위에서 오는 대각선은 r+c가 모두 같고
왼쪽 위에서 오는 대각선은 r-c가 전부 같다.
따라서, r+c가 같은 것은 하나만 올 수 있고,
방문체크는 N-queen에서 한 것을 응용하여 r-c를 key로 가지는 딕셔너리로 해준다.

또한, 시간단축을 위해 하나의 아이디어가 더 필요한데
바로 비숍의 경우, Queen과 다르게 검은 칸에 있는 비숍이 흰 칸에 있는 비숍을
절대로 공격할 수 없다는 점이다.
따라서, r+c = 홀수인 칸, r+c=  짝수인 칸을 따로 나눠 depth를 2 씩 늘리며
백트래킹 해준다음 둘의 최댓값끼리 더하면, 시간 복잡도를 매우 크게 감소시키는 것이 가능하다.
'''

from collections import defaultdict

N = int(input())

pan = []
daegak = defaultdict(int)
for i in range(N):
    pan.append(list(map(int,input().split())))

def backtracking(depth):
    global count
    global maxcount
    if depth >= N * 2 - 1 :

        maxcount = max(count, maxcount)
        return
    if depth < N:
        for i in range(depth+1):
            if pan[i][depth-i]== 1 and daegak[depth-(2*i)] == 0: #넣을 수 있을때

                daegak[depth - (2 * i)] = 1
                pan[i][depth - i] = 0
                count += 1
                backtracking(depth + 2) #해당 칸에 집어넣을 수 있다면, 집어넣고 재귀 깊이+2
                count -= 1 #재귀를 빠져나올 때, 바꿔놓았던 변수들을 안 넣었을때로 돌려 놓는다.
                pan[i][depth - i] = 1
                daegak[depth - (2 * i)] = 0


    else:
        for i in range(depth-N+1,N):
            if pan[i][depth-i] == 1 and daegak[depth-(2*i)] == 0:
                daegak[depth - (2 * i)] = 1
                pan[i][depth - i] = 0
                count += 1
                backtracking(depth + 2)
                count -= 1
                daegak[depth - (2 * i)] = 0
                pan[i][depth - i] = 1
    backtracking(depth + 2) # 이게 있는 이유는, 해당 우상-좌하 대각선에 안 넣었어도
    # 다음 단계를 진행했을때 최댓값이 있을 수 있기 때문.,
    # 만약, 이 한 줄이 없으면 pan[0][0] = 0일 경우 프로그램이 더 진행되지 않고 꺼져버린다.
    # 해당 줄에 넣지 않아도 코드가 돌아갈 수 있게 만드는 방법
    maxcount = max(count,maxcount) #리턴되기 직전 maxcount를 갱신 해준다.
    return

count = 0
maxcount = 0
backtracking(0)
a = maxcount
count = 0
maxcount = 0
backtracking(1)
b = maxcount
print(a+b)