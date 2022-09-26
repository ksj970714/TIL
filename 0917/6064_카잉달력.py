T = int(input())
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
import math
for testcase in range(T):
    m, n, x, y = map(int,input().split())
    lcm = math.lcm(m,n)
    if n == y:
        y = 0
    hae = -1
    a = x
    b = x%n
    cur = x

    while cur <= lcm:
        if b == y:
            hae = cur
            break
        else:
            b += m
            b = b % n
            cur += m
    print(hae)





