import collections
F, S, G, U, D = map(int,input().split())

# 총 F층
# S층이 Start, G층으로 이동
# U는 업 D는 다운

count = 0
cur = S

cha = G - S
if cha == 0 :
    print(0)
    quit()
    cur = 0
elif cha < 0:
    if D == 0 :
        print('use the stairs')
        quit()
    else:
        count += abs(cha)//D
        cur = S - count*D
else:
    if U == 0:
        print('use the stairs')
        quit()
    else:
        count += cha // U
        cur = S + count * U

mydict = collections.defaultdict(int)

while True:
    if mydict[cur] == 1:
        print('use the stairs')
        break
    else:
        mydict[cur] = 1
    if cur < G :
        if cur + U <= F:
            cur += U
        else:
            cur -= D
            if cur < 0:
                print('use the stairs')
                break
    elif cur == G:
        print(count)
        break
    else:
        if cur - D > 0:
            cur -= D
        else:
            cur += U
            if cur > F:
                print('use the stairs')
                break
    count += 1
