N = int(input())
fluid = list(map(int,input().split()))
fluid.sort()
mymin = float('inf')
l = 0 ; r = N-1

while r != l:
    if mymin > abs(fluid[l]+fluid[r]):
        mymin = abs(fluid[l]+fluid[r])
        myans = [fluid[l],fluid[r]]
    if mymin == 0:
        break


    if abs(fluid[l+1]+fluid[r]) > abs(fluid[l]+fluid[r-1]):
        r -= 1

    else:
        l += 1

print(*myans)