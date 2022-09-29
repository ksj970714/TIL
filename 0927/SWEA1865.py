#병합 정렬

def mergesort(mylist):
    N  = len(mylist)
    if N <= 1:
        return
    mid = len(mylist)//2
    left = mylist[:mid]
    right = mylist[mid:]
    mergesort(left)
    mergesort(right)

    L = 0
    R = 0
    now = 0

    while L < len(left) and R < (len(right)):
        if left[L] < right[R]:
            mylist[now] = left[L]
            L += 1
            now += 1
        else:
            mylist[now] = right[R]
            R += 1
            now += 1
    while L < len(left):
        mylist[now] = left[L]
        L += 1
        now += 1
    while R < len(right):
        mylist[now] = right[R]
        R += 1
        now += 1

    print(mylist)

mergesort([2,3,4,5,6,1,7,8,9,10])
print(mylist)

T = int(input())
for testcase in range(1,T+1):
    pass