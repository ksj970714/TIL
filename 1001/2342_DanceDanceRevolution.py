mydp = [[float('inf')]*5 for i in range(5)]
# [[0]*5 for i in range(5)]

ddr = list(map(int,input().split()))

# 처리를 위해 첫번째 움직임은 하고 시작한다.
start = ddr.pop(0)
if start == 0:
    print(0)
    quit()
mydp[start][0] = 2
mydp[0][start] = 2

# 이동 시 들어가는 힘을 나타내줄 함수를 정의해준다.
def power(a,b):
    if a == 0 :
        return 2
    cha = abs(a-b)
    if cha == 0:
        return 1
    elif cha == 2:
        return 4
    else:
        return 3



for shift in ddr:
    # 종료 조건
    if shift == 0 :
        break
    temp = [[float('inf')] * 5 for i in range(5)]
    for r in range(5):
        for c in range(5):
            if mydp[r][c] != float('inf'):
                # 왼발, 오른발이 밟고있는 것과 같은 걸 밟아야 하면
                # 발의 이동은 없고, 힘의 소모만 있음
                if r == shift or c == shift:
                    temp[r][c] = min(mydp[r][c]+1,temp[r][c])
                else:
                    #왼발을 움직임.
                    temp[shift][c] = min(mydp[r][c] + power(r,shift),temp[shift][c])
                    #오른발을 움직임.
                    temp[r][shift] = min(mydp[r][c] + power(c,shift),temp[r][shift])
    mydp = []
    for i in range(5):
        mydp.append(temp[i][:])
    print(mydp)

mymin = float('inf')
for i in range(5):
    for j in range(5):
        if mymin > mydp[i][j]:
            mymin = mydp[i][j]
print(mymin)