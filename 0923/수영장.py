T = int(input())
for testcase in range(1,T+1):
    plan = list(map(int,input().split()))
    cost = list(map(int,input().split()))
    DP = [0]*12
# 일 - 달 비교

    for i in range(12):
        cost[i] = min(cost[i]*plan[0],plan[1])

#3달에 대해 DP 사용
    DP[0] = cost[0]
    DP[1] = sum(cost[0:2])
    DP[2] = min(sum(cost[0:3]),plan[2])

    for i in range(9):
        DP[i+3] = min(DP[i+2]+cost[i+3],DP[i]+plan[2])

#연간 비용 비교
    if DP[11]<plan[3]:
        print('#{} {}'.format(testcase,DP[11]))
    else:
        print('#{} {}'.format(testcase,plan[3]))