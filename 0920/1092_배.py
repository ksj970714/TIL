N = int(input())

crane = sorted(list(map(int, input().split())))

M = int(input())
work = [0] * N

box = sorted(list(map(int, input().split())))

if max(box) > max(crane):
    print(-1)
    quit()

# 계산을 하기 위해 필요한 리스트 만들어 주기.
# 어떤 박스가 있을 때 그 무게보다 크면서 가장 가까운 크레인에 += 1
# 예를 들면, 크레인이 1 5 10을 옮길 수 있을 때 무게가 6인 상자만 1개 있다면 [0, 1, 0]으로 입력된다.
# 0~2번 크레인이 존재하여 [0, 1, 0]일 때, 2번 크레인은 1번 크레인에 할당된 6번 박스를 옮길 수 있다.
# 0번 크레인은 1번 크레인이 해야 할 일을 하지 못한다.

idx = 0 ; i = 0 ; j = 0 ; temp = 0
count = 0
while idx < M:
    if box[i] <= crane[j]:
        temp += 1
        i += 1
        idx += 1
    else:
        work[j] = temp
        temp = 0
        j += 1
work[j] = temp

while M > 0:
    M -= len(work)
    for i in range(len(work)):
        work[i] -= 1
    # 일단 모든 크레인이 일 한 것으로 가정하고 모든 인덱스에 -1을 해준다.
    # 리스트의 뒤에서 앞으로 순회하며, 음수에 대한 처리를 해준다.
    # 뒤에 있는 게 음수인데 앞에 아직 처리할 수 있는게 남았으면, 앞에 있는 크레인이 할 일을 대신 처리한 것이고
    # 음수 앞에 처리할 게 없으면, 그냥 아무 일도 안 한 것!
    # 예를 들어, 크레인이 1 5 10이고, 상자가 6 6일 경우
    # 배열은 [0, 2, 0]=>[-1, 1, -1]이 된다
    # 여기서 0번 크레인은 옮길 수 있는 게 없으니 [0, 1, -1]
    # 1번 크레인은 일 했고, 2번 크레인은 1번 크레인이 할 수 있는 일을 해주는 것이 가능하다.
    # 따라서, 2번 크레인의 인덱스에 있는 -1를 1번 크레인의 인덱스에 더해준다: [0, 0, 0], 따라서 작업 완료
    for j in range(len(work)-1,0,-1):
        if work[j] < 0:
            work[j-1] += work[j]
            work[j] = 0
    if work[0] < 0 :
        M -= work[0]
        work[0] = 0
    count += 1

print(count)