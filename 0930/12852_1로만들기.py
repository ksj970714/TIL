from collections import deque
N = int(input())

# BFS 구현

#[숫자, 문자]

dq = deque([[N,str(N),0]])
while dq:
    for i in range(len(dq)):
        temp = dq.popleft()
        number = temp[0]
        word = temp[1]
        count = temp[2]

        if number == 1:
            dq = []
            print(count)
            print(word.lstrip())

            break

        if number % 3 == 0:
            dq.append([number // 3, word+' {}'.format(number//3), count+1])

        if number % 2 == 0:
            dq.append([number // 2, word+' {}'.format(number//2), count+1])

        dq.append([number - 1, word+' {}'.format(number-1), count+1])
